import { Subscription, of } from 'rxjs';
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
    this.produtoService.onLoaded.subscribe( resp => {
      if (this.loading != resp){
        this.loading = resp
        console.log('resp', resp)
      }
    })
  }

  ngAfterViewInit(){

  }

  ngOnInit(): void {

  }
}
