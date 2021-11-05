import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { SharedModule } from './../../shared/shared/shared.module';
import { ProdutosComponent } from './produtos/produtos.component';
import { SetoresComponent } from './setores/setores.component';
import { UnidadesComponent } from './unidades/unidades.component';



@NgModule({
  declarations: [
    SetoresComponent,
    ProdutosComponent,
    UnidadesComponent,
  ],
  imports: [
    CommonModule,
    SharedModule
  ]
})
export class ProdutosModule { }
