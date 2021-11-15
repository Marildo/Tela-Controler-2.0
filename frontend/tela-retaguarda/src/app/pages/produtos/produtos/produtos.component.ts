import { Component, OnInit } from '@angular/core';
import { ProdutoService } from './produto.service';


@Component({
  selector: 'ut-produtos',
  templateUrl: './produtos.component.html',
  styleUrls: ['./produtos.component.scss']
})
export class ProdutosComponent implements OnInit {

  public loading = false;

  constructor(private produtoService: ProdutoService) {

  }

  ngOnInit(): void {
    this.produtoService.onLoaded.subscribe(resp => {
      this.loading = resp
    })
  }
}
