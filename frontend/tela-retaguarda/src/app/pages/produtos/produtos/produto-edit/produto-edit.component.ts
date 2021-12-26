import { TelaResponse } from './../../../../shared/models/tela-response';
import { ProdutoService } from './../produto.service';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Subscription, Observable, of } from 'rxjs';
import { PipeEnum } from 'src/app/shared/pipes/pipes-enum';

@Component({
  selector: 'ut-produto-edit',
  templateUrl: './produto-edit.component.html',
  styleUrls: ['./produto-edit.component.scss']
})
export class ProdutoEditComponent implements OnInit, OnDestroy {

  public formCadastro: FormGroup;
  public formCalculate: FormGroup;
  public error: any

  public id: any
  private paramsSubcription: Subscription
  public obsUnidades: Observable<TelaResponse> = of()
  public obsSetores: Observable<TelaResponse> = of()

  constructor(
    private activeRoute: ActivatedRoute,
    private produtoService: ProdutoService,
    private formBuilder: FormBuilder,
    private router: Router
  ) {
    this.formCadastro = this.produtoService.fomrService.buildForm('produtos')
    this.formCalculate = this.formBuilder.group({
      gerar_codigo: [false],
      pr_sugerido: [0.01],
      custo_venda: [0.01],
      markup_real: [0.01],
      markup_desejado: [0.01],
    })

    this.paramsSubcription = this.activeRoute.params.subscribe(
      (params: any) => {
        this.id = params['id']
        this.produtoService.loadById(this.id).subscribe(res => this.formCadastro.setValue(res.data))
      }
    )
  }

  ngOnInit(): void {
    // TODO - Deixar um valor  - quando for para trazer todos os dados, porem filtrar apenas ativos
    this.obsUnidades = this.produtoService.unidadeService.load(1, 1000)
    this.obsSetores = this.produtoService.setorService.load(1, 1000)

    // this.produtoService.onLoaded.next(true)


  }
  onSave() {
    Object.keys(this.formCadastro.controls).forEach(item => {
      const control = this.formCadastro.get(item)
      control?.markAsDirty();
    })

    const data = this.formCadastro.value
    delete data['ultima_venda']
    delete data['ultima_compra']
    if (!data['id']) {
      data.id = 0
    }

    this.produtoService.save(data).subscribe(
      (resp) => {
        this.router.navigate(['/produtos'])
      },
      (erro) => {
        this.error = erro.error.data
      })
  }

  onCancel() {
    this.router.navigate(['/produtos'])
  }

  ngOnDestroy(): void {
    this.paramsSubcription.unsubscribe()
  }

  getPipeDate(): PipeEnum {
    return PipeEnum.DateTime
  }
}
