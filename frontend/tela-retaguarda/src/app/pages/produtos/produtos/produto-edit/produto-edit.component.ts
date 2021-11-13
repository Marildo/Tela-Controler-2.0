import { ProdutoService } from './../produto.service';
import { FormGroup } from '@angular/forms';
import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'ut-produto-edit',
  templateUrl: './produto-edit.component.html',
  styleUrls: ['./produto-edit.component.scss']
})
export class ProdutoEditComponent implements OnInit, OnDestroy {

  public formCadastro: FormGroup;
  public id: any
  private paramsSubcription: Subscription

  constructor(private activeRoute: ActivatedRoute, private produtoService: ProdutoService) {
    this.formCadastro = this.produtoService.fomrService.buildForm('produtos')
    this.paramsSubcription = this.activeRoute.params.subscribe(
      (params: any) => {
        this.id = params['id']
      }
    )
  }

  ngOnInit(): void {

  }

  ngOnDestroy(): void {
    this.paramsSubcription.unsubscribe()
  }
}
