import { NotFoundComponent } from './pages/others/not-found/not-found.component';
import { UnidadesComponent } from './pages/unidades/unidades.component';
import { ProdutosComponent } from './pages/produtos/produtos.component';
import { IndexComponent } from './pages/index/index.component';
import { LoginComponent } from './auth/login/login.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './pages/dashboard/dasboard.component';
import { AuthGuard } from './auth/auth.guard';

const routes: Routes = [
  {
    path: '', component: IndexComponent,
    canActivate: [AuthGuard],
    children: [
      { path: '' , redirectTo: 'dashboard', pathMatch:'full'},
      { path: 'dashboard', component: DashboardComponent },
      { path: 'produtos', component: ProdutosComponent },
      { path: 'unidades', component: UnidadesComponent },
      { path: '**', component: NotFoundComponent }
    ]
  },
  { path: 'login', component: LoginComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
