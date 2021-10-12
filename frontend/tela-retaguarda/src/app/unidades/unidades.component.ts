import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog'

import { Unidade, TelaResponse, Pagination } from './model';
import { UnidadeService } from './unidade.service';
import { UnidadeFormComponent } from './unidade.form/unidade.form.component'
import { NotifyService } from '../shared/notify.service';

@Component({
  selector: 'ut-unidades',
  templateUrl: './unidades.component.html',
  styleUrls: ['./unidades.component.scss']
})
export class UnidadesComponent implements OnInit {


  public loading = false;
  public unidades: Array<Unidade> = []
  public pagination: Pagination =  new Pagination()
  public displayedColumns = ['id', 'unid', 'descricao', 'fracionavel', 'action']
  public pages: [number]= [1]


  constructor(
    private dialog: MatDialog,
    private notify: NotifyService,
    private unidadeService: UnidadeService) { }


  ngOnInit(): void {
    this.onload()
  }

  private onload(page: number = 1) {
    this.loading = true
    this.unidades = []
    let size = 5
    this.unidadeService.load(page, size)
      .subscribe(resp => {
        this.unidades = resp.data
        this.pagination = resp.pagination
        this.loading = false


        this.pages = [0]
        this.pages.shift()

        let end = 1
        let items_before = 0
        for (let index = this.pagination.page ; index >= end && items_before < 5; index--) {
          console.log(index)
          items_before++
          this.pages.push(index)
        }


        let x =  this.pagination.page + 5 < 10 ? 10  :this.pagination.page + 5
        end = this.pagination.total_pages < x  ? this.pagination.total_pages : x
        console.log('End =>', end)
        for (let index = this.pagination.page +1; index <= end; index++) {
          console.log(index)
          this.pages.push(index)
        }
        this.pages.sort((c,n) => c - n)

        // TODO - Enquanto menor que 10 inserir novamente
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

  onChangePage(flag: number) {
    let nextPage = this.pagination.page + flag
    this.onload(nextPage)
  }

  onloadPage(page:number){
    this.onload(page)
  }

  disabled_previous(){
    return this.pagination.page === 1
  }

  disabled_next(){
    return this.pagination.page === this.pagination.total_pages
  }
}
