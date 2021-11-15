import { Route } from  '@angular/router/router';
import { ProdutoEditComponent } from './produtos/produto-edit/produto-edit.component';
import { ProdutosListComponent } from './produtos/produtos-list/produtos-list.component';
import { ProdutosComponent } from './produtos/produtos.component';

export const produtosRoute:Route = {
  path: 'produtos',
  component: ProdutosComponent,
  children: [
    {
      path: '',
      component: ProdutosListComponent
    },
    {
      path: 'edit/:id',
      component: ProdutoEditComponent
    }
  ]
}

