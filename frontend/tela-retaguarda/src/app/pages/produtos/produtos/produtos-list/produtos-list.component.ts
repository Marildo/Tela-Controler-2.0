import { Router } from '@angular/router';
import { ProdutoService } from './../produto.service';
import { Pagination } from './../../../../shared/models/pagination';
import { Produto } from '@entity/produto';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'ut-produtos-list',
  templateUrl: './produtos-list.component.html',
  styleUrls: ['./produtos-list.component.scss']
})
export class ProdutosListComponent implements OnInit {

  public produtos: Array<Produto> = []
  public pagination: Pagination = new Pagination()
  public displayedColumns = ['codigo', 'nome', 'preco','estoque', 'unidade', 'action']

  constructor(private router:Router, private produtoService: ProdutoService) { }

  ngOnInit(): void {
    this.onLoad()
  }

  private onLoad(page: number = 1, text: string = '') {
    this.produtos = []
    let size = 7
    // this.produtoService.onLoaded.next(true)
    this.produtoService.load(page, size, text)
      .subscribe(resp => {
        this.produtos = resp.data
        this.pagination = resp.pagination
        // this.produtoService.onLoaded.next(false)
      })
  }



  public onNewItem(produto: Produto) {
  this.openForm(produto)
}


  onChangePage(page: number) {
    this.onLoad(page)
  }

  onSearch(text: string) {
    this.onLoad(1, text)
  }

  public editItem(produto: Produto) {
   // this.openForm(produto)
  }


  public deleteItem(_id: number) {

  }


  private openForm(produto: Produto) {
    this.produtoService.onLoaded.subscribe().unsubscribe()
    this.router.navigate(['/produtos/edit', 1])
  }

}
