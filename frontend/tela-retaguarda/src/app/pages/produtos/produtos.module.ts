import { NgxCurrencyModule } from 'ngx-currency';
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { SharedModule } from '../../shared/shared.module';
import { ProdutoEditComponent } from './produtos/produto-edit/produto-edit.component';
import { ProdutosListComponent } from './produtos/produtos-list/produtos-list.component';
import { ProdutosComponent } from './produtos/produtos.component';
import { SetoresComponent } from './setores/setores.component';
import { UnidadesComponent } from './unidades/unidades.component';


export const customCurrencyMaskConfig = {
  align: "right",
  allowNegative: true,
  allowZero: true,
  decimal: ",",
  precision: 2,
  prefix: "R$ ",
  suffix: "",
  thousands: ".",
  nullable: true
};


@NgModule({
  declarations: [
    SetoresComponent,
    ProdutosComponent,
    UnidadesComponent,
    ProdutoEditComponent,
    ProdutosListComponent,
  ],
  imports: [
    CommonModule,
    SharedModule,

    NgxCurrencyModule.forRoot(customCurrencyMaskConfig)
  ]
})
export class ProdutosModule { }
