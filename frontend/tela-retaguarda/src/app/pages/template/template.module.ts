import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './../../app-routing.module';
import { AppMaterialModule } from './../../shared/modules/app-material.module';
import { ContentComponent } from './content/content.component';
import { FooterComponent } from './footer/footer.component';
import { HeaderComponent } from './header/header.component';
import { MenuComponent } from './menu/menu.component';
import { TemplateComponent } from './template/template.component';


@NgModule({
  declarations: [
    TemplateComponent,
    HeaderComponent,
    ContentComponent,
    FooterComponent,
    MenuComponent
  ],

  imports: [
    CommonModule,
    AppRoutingModule,
    AppMaterialModule
  ],
  exports: [
    TemplateComponent
  ]
})
export class TemplateModule { }
