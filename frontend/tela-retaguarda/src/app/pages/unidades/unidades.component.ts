
import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { debounceTime, distinctUntilChanged, map, tap } from 'rxjs/operators';
import { NotifyService } from 'src/app/core/services/notify.service';
import Unidade from 'src/app/shared/models/entity/unidade';
import { Pagination } from 'src/app/shared/models/pagination';
import { UnidadeFormComponent } from './unidade.form/unidade.form.component';
import { UnidadeService } from './unidade.service';


@Component({
  selector: 'ut-unidades',
  templateUrl: './unidades.component.html',
  styleUrls: ['./unidades.component.scss']
})
export class UnidadesComponent implements OnInit {


  public loading = false;
  public unidades: Array<Unidade> = []
  public pagination: Pagination = new Pagination()
  public displayedColumns = ['id', 'unid', 'descricao', 'fracionavel', 'action']
  public search = new FormControl()
  // private search$: Observable<any>


  constructor(
    private dialog: MatDialog,
    private notify: NotifyService,
    private unidadeService: UnidadeService) {

    this.search.valueChanges
      .pipe(
        map(v => v.trim()),
        debounceTime(200), // esperar 200 millesegundo
        distinctUntilChanged(), // somente se o valor mudar
        tap(a => console.log(a)),
      ).subscribe(text => this.onLoad(0, text))
  }


  ngOnInit(): void {
    this.onLoad()
  }

  private onLoad(page: number = 1, text: string = '') {
    this.loading = true
    this.unidades = []
    let size = 12
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
    this.unidadeService.delete(_id).subscribe(() => {
      this.notify.success('Unidade removida com sucesso!')
      this.unidades = this.unidades.filter(item => item.id != _id)
    })
  }

  private openForm(unidade: Unidade) {
    const dialogRef = this.dialog.open(UnidadeFormComponent, {
      data: unidade,
      width: '400px'
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log(result, this.unidades.length)
      if (result != undefined) {
        // TODO - Validar antes de inserir
        this.unidades.push(result)

        this.unidades.forEach(console.log)
      }

    });
  }

  onChangePage(page:number){
    this.onLoad(page)
  }

  onSearch(text: string) {
    this.onLoad(1, text)
  }

  // TODO - Deixa dinamico de acordo com o icone do menu
  get_icon(): string {
    return 'straighten'
  }
}
