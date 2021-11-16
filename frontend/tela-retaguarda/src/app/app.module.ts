import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DashboardComponent } from './pages/dashboard/dasboard.component';
import { IndexComponent } from './pages/index/index.component';
import { LoginComponent } from './pages/login/login.component';
import { NotFoundComponent } from './pages/others/not-found/not-found.component';
import { ProdutosModule } from './pages/produtos/produtos.module';
import { TemplateModule } from './pages/template/template.module';
import { SharedModule } from './shared/shared.module';



@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    IndexComponent,
    DashboardComponent,
    NotFoundComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    TemplateModule,
    SharedModule,
    ProdutosModule
  ],
  providers: [
  ],
  exports: [

  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

// TODO - Unsubscribe from RxJS Observables
// TODO - Use Lazy Loading
// TODO - Ajustar tamanho de campo do front com backend, se possivel carregar do back uma lista e salvar em json e deixar automatico
