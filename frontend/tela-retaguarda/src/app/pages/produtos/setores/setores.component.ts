import { Component, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { Setor } from 'src/app/shared/models/entity/setor';
import { Pagination } from 'src/app/shared/models/pagination';

import { NotifyService } from './../../../core/services/notify.service';
import { QuestionService } from './../../../shared/components/question/question.service';
import { SetorService } from './setor.service';

@Component({
  selector: 'ut-setores',
  templateUrl: './setores.component.html',
  styleUrls: ['./setores.component.scss']
})
export class SetoresComponent implements OnInit {

  public loading = false;
  public editing = false
  public setores: Array<Setor> = []
  public pagination: Pagination = new Pagination()
  public displayedColumns = ['id', 'nome', 'ativo', 'action']
  public error = ''
  public titleForm = ''
  public formCadastro: FormGroup


  constructor(private notify: NotifyService,
    private questionService: QuestionService,
    private setorService: SetorService) {

    this.formCadastro = setorService.formService.buildForm('setores')
  }

  ngOnInit(): void {
    this.onLoad()
  }

  private onLoad(page: number = 1, text: string = '') {
    this.loading = true
    this.setores = []
    let size = 10
    this.setorService.load(page, size, text)
      .subscribe(resp => {
        this.setores = resp.data
        this.pagination = resp.pagination
        this.loading = false
      })
  }

  public addItem() {
    this.openForm({ id: 0, nome: '', ativo: true })
  }

  public editItem(setor: Setor) {
    this.openForm(setor)
  }

  public deleteItem(_id: number) {
    this.questionService.confirm('Confirma a exclusão do Setor ?')
      .then(() => {
        this.setorService.delete(_id).subscribe(() => {
          this.notify.success('Unidade removida com sucesso!')
          this.setores = this.setores.filter(item => item.id != _id)
          this.pagination.total--
        })
      }).catch(() => { })
  }

  onChangePage(page: number) {
    this.onLoad(page)
  }

  onSearch(text: string) {
    this.onLoad(1, text)
  }

  onSave() {
    this.setorService.save(this.formCadastro.value)
      .subscribe(
        () => {
          this.formCadastro.reset()
          this.notify.success('Operacao realizada com sucesso!')
          this.editing = false
        },
        resp_error => {
          this.error = resp_error.error.data.error.description
        }
      )
  }

  onCancel() {
    this.formCadastro.reset()
    this.editing = false
  }

  private openForm(setor: Setor) {
    this.titleForm = setor.id === 0 ? 'Novo Setor' : 'Alterando Setor'
    this.formCadastro.setValue(setor)
    this.editing = true
  }
}
