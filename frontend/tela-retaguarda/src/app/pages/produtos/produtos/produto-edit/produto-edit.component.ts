import { TelaResponse } from './../../../../shared/models/tela-response';
import { ProdutoService } from './../produto.service';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription, Observable , of} from 'rxjs';

@Component({
  selector: 'ut-produto-edit',
  templateUrl: './produto-edit.component.html',
  styleUrls: ['./produto-edit.component.scss']
})
export class ProdutoEditComponent implements OnInit, OnDestroy {

  public formCadastro: FormGroup;
  public formCalculate:FormGroup;
  error: any

  public id: any
  private paramsSubcription: Subscription
  public  obsUnidades:  Observable<TelaResponse> = of()
  public  obsSetores:  Observable<TelaResponse> = of()

  constructor(
    private activeRoute: ActivatedRoute,
    private produtoService: ProdutoService,
    private formBuilder: FormBuilder,
  ){
    this.paramsSubcription = this.activeRoute.params.subscribe(
      (params: any) => {
        this.id = params['id']
      //  produtoService.loadById()
      }
    )

    this.formCadastro = this.produtoService.fomrService.buildForm('produtos')
    this.formCalculate = this.formBuilder.group({
      gerar_codigo:[false],
      pr_sugerido: [0.01],
      custo_venda:[0.01],
      markup_real:[0.01],
      markup_desejado:[0.01],
    })

  }

  ngOnInit(): void {
    // TODO - Deixar um valor  - quando for para trazer todos os dados, porem filtrar apenas ativos
    this.obsUnidades = this.produtoService.unidadeService.load(1,1000)
    this.obsSetores = this.produtoService.setorService.load(1,1000)

    // this.produtoService.onLoaded.next(true)

  }
  onSave(){
    const data = this.formCadastro.value
     if (!data['id']){
       data.id = 0
     }
     this.produtoService.save(data).subscribe(
       (resp) => {
         console.log(resp.data)
     },
     (erro) => {
       this.error = erro.error.data
     } )
  }

  ngOnDestroy(): void {
    this.paramsSubcription.unsubscribe()
  }
}
