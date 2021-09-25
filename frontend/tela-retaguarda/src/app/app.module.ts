import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http'

//import { MatSliderModule } from '@angular/material/slider';
//import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import {MatBadgeModule} from '@angular/material/badge';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoginComponent } from './auth/login/login.component';
import { IndexComponent } from './index/index.component';
import { TemplateComponent } from './template/template.component';
import { MenuComponent } from './template/menu/menu.component';
import { HeaderComponent } from './template/header/header.component';
import { DashboardComponent } from './dashboard/dasboard.component';
import { ContentComponent } from './template/content/content.component';
import { FooterComponent } from './template/footer/footer.component';
import { ProdutosComponent } from './produtos/produtos.component';




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
    ProdutosComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FormsModule,
    HttpClientModule,

    // MatSliderModule,
    MatIconModule,
    MatFormFieldModule,
    MatInputModule,
    // MatToolbarModule,
    MatButtonModule,
    MatBadgeModule
 ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
