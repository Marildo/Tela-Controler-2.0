import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { SharedModule } from '../../shared/shared.module';
import { ProdutosComponent } from './produtos/produtos.component';
import { SetoresComponent } from './setores/setores.component';
import { UnidadesComponent } from './unidades/unidades.component';
import { ProdutoEditComponent } from './produtos/produto-edit/produto-edit.component';




@NgModule({
  declarations: [
    SetoresComponent,
    ProdutosComponent,
    UnidadesComponent,
    ProdutoEditComponent,
  ],
  imports: [
    CommonModule,
    SharedModule
  ]
})
export class ProdutosModule { }
