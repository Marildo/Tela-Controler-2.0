import { Pagination } from 'src/app/shared/models/pagination';
import { Produto } from '@entity/produto';
import { Component, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { ProdutoService } from './produto.service';


@Component({
  selector: 'ut-produtos',
  templateUrl: './produtos.component.html',
  styleUrls: ['./produtos.component.scss']
})
export class ProdutosComponent implements OnInit {

  public loading = false;
  public editing = false
  public produtos: Array<Produto> = []
  public pagination: Pagination = new Pagination()
  public displayedColumns = ['codigo', 'nome', 'preco','estoque', 'unidade', 'action']
  public formCadastro: FormGroup

  constructor(private produtoService: ProdutoService) {
    this.formCadastro = this.produtoService.fomrService.buildForm('produtos')
  }

  ngOnInit(): void {
    this.onLoad()
  }

  private onLoad(page: number = 1, text: string = '') {
    this.loading = true
    this.produtos = []
    let size = 10
    this.produtoService.load(page, size, text)
      .subscribe(resp => {
        this.produtos = resp.data
        console.log(this.produtos)
        this.pagination = resp.pagination
        this.loading = false
      })
  }


  public addItem() {
    this.openForm({
      id: 0,
      nome: '',
      cod_barras: 0,
      codigo: '',
      pr_custo: 0,
      pr_venda_vista: 0.1,
      pr_venda_prazo: 0.1,
      estoque: 0,
      estoque_minimo: 0,
      qtd_embalagem:1,
      ativo: true
    })
  }

  public editItem(produto: Produto) {
    this.openForm(produto)
  }

  public deleteItem(_id: number) {

  }

  onChangePage(page: number) {
    this.onLoad(page)
  }

  onSearch(text: string) {
    this.onLoad(1, text)
  }


  private openForm(produto: Produto) {

  }

}
