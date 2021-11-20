import { TelaResponse } from './../../../../shared/models/tela-response';
import { ProdutoService } from './../produto.service';
import { FormGroup } from '@angular/forms';
import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription, Observable } from 'rxjs';

@Component({
  selector: 'ut-produto-edit',
  templateUrl: './produto-edit.component.html',
  styleUrls: ['./produto-edit.component.scss']
})
export class ProdutoEditComponent implements OnInit, OnDestroy {

  public formCadastro: FormGroup;
  public id: any
  private paramsSubcription: Subscription
  public  obsUnidades:  Observable<TelaResponse>

  constructor(private activeRoute: ActivatedRoute, private produtoService: ProdutoService) {
    this.formCadastro = this.produtoService.fomrService.buildForm('produtos')
    this.paramsSubcription = this.activeRoute.params.subscribe(
      (params: any) => {
        this.id = params['id']
      }
    )

    this.obsUnidades = this.produtoService.unidadeService.load(1,1000)
    // TODO - Deixar um valor  - quando for para trazer todos os dados, porem filtrar apenas ativos
  }

  ngOnInit(): void {


  }
  onSave(){
    console.log(this.formCadastro.controls)
    console.log(this.formCadastro.value)
  }

  ngOnDestroy(): void {
    this.paramsSubcription.unsubscribe()
  }
}
