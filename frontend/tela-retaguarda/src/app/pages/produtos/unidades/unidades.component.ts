import { Component, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { NotifyService } from 'src/app/core/services/notify.service';
import { Unidade } from 'src/app/shared/models/entity/unidade';
import { Pagination } from 'src/app/shared/models/pagination';

import { QuestionService } from '../../../shared/components/question/question.service';
import { UnidadeService } from './unidade.service';



@Component({
  selector: 'ut-unidades',
  templateUrl: './unidades.component.html',
  styleUrls: ['./unidades.component.scss']
})
export class UnidadesComponent implements OnInit {


  public loading = false;
  public editing = false
  public unidades: Array<Unidade> = []
  public pagination: Pagination = new Pagination()
  public displayedColumns = ['id', 'unid', 'descricao', 'fracionavel','ativo', 'action']
  public error = ''
  public titleForm = ''
  public formCadastro: FormGroup


  constructor(
    private notify: NotifyService,
    private questionService: QuestionService,
    private unidadeService: UnidadeService) {

     this.formCadastro = this.unidadeService.fomrService.buildForm('unidades')
  }


  ngOnInit(): void {
    this.onLoad()
  }

  private onLoad(page: number = 1, text: string = '') {
    this.loading = true
    this.unidades = []
    let size = 10
    this.unidadeService.load(page, size, text)
      .subscribe(resp => {
        this.unidades = resp.data
        this.pagination = resp.pagination
        this.loading = false
      })
  }

  public addUnidade() {
    this.openForm({ id: 0, descricao: '', unid: '', fracionavel: false, ativo: true })
  }

  public editUnidade(unidade: Unidade) {
    this.openForm(unidade)
  }

  public deleteUnidade(_id: number) {
    this.questionService.confirm('Confirma a exclusão da Unidade ?')
      .then(() => {
        this.unidadeService.delete(_id).subscribe(() => {
          this.notify.success('Unidade removida com sucesso!')
          this.unidades = this.unidades.filter(item => item.id != _id)
          this.pagination.total--
        })
      }).catch(() => {})
  }

  onChangePage(page: number) {
    this.onLoad(page)
  }

  onSearch(text: string) {
    this.onLoad(1, text)
  }

  onSave(){
    this.unidadeService.save(this.formCadastro.value)
    .subscribe(
      () =>{
        this.notify.success('Operacao realizada com sucesso!')
        this.editing = false
        this.formCadastro.reset()
      },
      resp_error => {
        // TODO - tratar erros de forma generica
        console.log(resp_error.error.data[0]  )
        this.error = resp_error.error.data.error.description
      }
    )
  }

  onCancel(){
    this.formCadastro.reset()
    this.editing = false
  }

  private openForm(unidade: Unidade) {
    this.titleForm = unidade.id === 0 ? 'Nova Unidade':'Alterando Unidade'
    this.formCadastro.setValue(unidade)
    this.editing = true

    // this.unidades.push(result)
  }

}
