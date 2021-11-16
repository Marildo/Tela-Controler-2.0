import { FlexLayoutModule } from '@angular/flex-layout';
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { SharedModule } from '../../shared/shared.module';
import { ProdutoEditComponent } from './produtos/produto-edit/produto-edit.component';
import { ProdutosListComponent } from './produtos/produtos-list/produtos-list.component';
import { ProdutosComponent } from './produtos/produtos.component';
import { SetoresComponent } from './setores/setores.component';
import { UnidadesComponent } from './unidades/unidades.component';




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
    SharedModule
  ]
})
export class ProdutosModule { }
