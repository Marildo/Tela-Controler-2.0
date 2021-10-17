import { HttpClientModule } from '@angular/common/http'
import { NgModule } from '@angular/core'
import { FormsModule, ReactiveFormsModule } from '@angular/forms'
import { BrowserModule } from '@angular/platform-browser'
import { BrowserAnimationsModule } from '@angular/platform-browser/animations'

import { AppRoutingModule } from './app-routing.module'
import { AppMaterialModule } from './shared/app-material.module'

import { AppComponent } from './app.component'
import { LoginComponent } from './auth/login/login.component'
import { DashboardComponent } from './pages/dashboard/dasboard.component'
import { IndexComponent } from './pages/index/index.component'
import { ProdutosComponent } from './pages/produtos/produtos.component'
import { ContentComponent } from './pages/template/content/content.component'
import { FooterComponent } from './pages/template/footer/footer.component'
import { HeaderComponent } from './pages/template/header/header.component'
import { MenuComponent } from './pages/template/menu/menu.component'
import { TemplateComponent } from './pages/template/template/template.component'
import { UnidadesComponent } from './pages/unidades/unidades.component';
import { UnidadeFormComponent } from './pages/unidades/unidade.form/unidade.form.component'


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
