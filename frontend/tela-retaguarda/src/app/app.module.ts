import { HttpClientModule } from '@angular/common/http'
import { NgModule } from '@angular/core'
import { FormsModule, ReactiveFormsModule } from '@angular/forms'
import { BrowserModule } from '@angular/platform-browser'
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'

import { AppRoutingModule } from './app-routing.module'
import { AppMaterialModule } from './shared/app-material.module'

import { AppComponent } from './app.component'
import { LoginComponent } from './auth/login/login.component'
import { DashboardComponent } from './dashboard/dasboard.component'
import { IndexComponent } from './index/index.component'
import { ProdutosComponent } from './produtos/produtos.component'
import { ContentComponent } from './template/content/content.component'
import { FooterComponent } from './template/footer/footer.component'
import { HeaderComponent } from './template/header/header.component'
import { MenuComponent } from './template/menu/menu.component'
import { TemplateComponent } from './template/template.component'
import { UnidadesComponent } from './unidades/unidades.component';
import { UnidadeFormComponent } from './unidades/unidade.form/unidade.form.component'


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    IndexComponent,
    TemplateComponent,
    MenuComponent,
    HeaderComponent,
    DashboardComponent,
    ContentComponent,
    FooterComponent,
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
    AppMaterialModule
 ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
