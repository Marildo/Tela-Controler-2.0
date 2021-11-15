import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from './core/auth/auth.guard';
import { DashboardComponent } from './pages/dashboard/dasboard.component';
import { IndexComponent } from './pages/index/index.component';
import { LoginComponent } from './pages/login/login.component';
import { NotFoundComponent } from './pages/others/not-found/not-found.component';
import { produtosRoute } from './pages/produtos/produtos.router';
import { SetoresComponent } from './pages/produtos/setores/setores.component';
import { UnidadesComponent } from './pages/produtos/unidades/unidades.component';

const routes: Routes = [
  {
    path: '', component: IndexComponent,
    canActivate: [AuthGuard],
    children: [
      { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
      { path: 'dashboard', component: DashboardComponent },
      produtosRoute,
      { path: 'unidades', component: UnidadesComponent },
      { path: 'setores', component: SetoresComponent },
    ]
  },

  { path: 'login', component: LoginComponent },
  { path: '**', component: NotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
