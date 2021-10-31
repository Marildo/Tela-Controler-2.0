import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './pages/login/login.component';
import { DashboardComponent } from './pages/dashboard/dasboard.component';
import { IndexComponent } from './pages/index/index.component';
import { ProdutosComponent } from './pages/produtos/produtos.component';
import { TemplateModule } from './pages/template/template.module';
import { UnidadeFormComponent } from './pages/unidades/unidade.form/unidade.form.component';
import { UnidadesComponent } from './pages/unidades/unidades.component';
import { AppMaterialModule } from './shared/modules/app-material.module';
import { NotFoundComponent } from './pages/others/not-found/not-found.component'
import { ToobarComponent } from './shared/components/toobar/toobar.component';
import { SpinnerComponent } from './shared/components/spinner/spinner.component';
import { PaginationComponent } from './shared/components/pagination/pagination.component';
import { QuestionComponent } from './shared/components/question/question.component';
import { YesNoPipe } from './shared/pipes/yes-no.pipe';



@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    IndexComponent,
    DashboardComponent,
    ProdutosComponent,
    UnidadesComponent,
    UnidadeFormComponent,
    NotFoundComponent,
    ToobarComponent,
    SpinnerComponent,
    PaginationComponent,
    QuestionComponent,
    YesNoPipe,

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
