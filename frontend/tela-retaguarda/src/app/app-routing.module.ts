import { ProdutosComponent } from './produtos/produtos.component';
import { IndexComponent } from './index/index.component';
import { LoginComponent } from './auth/login/login.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dasboard.component';

const routes: Routes = [
  {
    path: '', component: IndexComponent,
    children: [
      { path: 'dashboard', component: DashboardComponent },
      { path: 'produtos', component: ProdutosComponent }

    ]
  },
  { path: 'login', component: LoginComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
