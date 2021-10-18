import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './auth/login/login.component';
import { DashboardComponent } from './pages/dashboard/dasboard.component';
import { IndexComponent } from './pages/index/index.component';
import { ProdutosComponent } from './pages/produtos/produtos.component';
import { TemplateModule } from './pages/template/template.module';
import { UnidadeFormComponent } from './pages/unidades/unidade.form/unidade.form.component';
import { UnidadesComponent } from './pages/unidades/unidades.component';
import { AppMaterialModule } from './shared/modules/app-material.module';




@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    IndexComponent,
    DashboardComponent,
    ProdutosComponent,
    UnidadesComponent,
    UnidadeFormComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    TemplateModule,
    AppMaterialModule
  ],
  providers: [
  ],
  exports: [
    AppMaterialModule
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
