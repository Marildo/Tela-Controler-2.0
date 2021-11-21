import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RouterModule } from '@angular/router';

import { DetailComponent } from './components/detail/detail.component';
import { BaseInputComponent } from './components/forms/inputs/base-input/base-input.component';
import { InputListComponent } from './components/forms/inputs/input-list/input-list.component';
import { InputNumberComponent } from './components/forms/inputs/input-number/input-number.component';
import { InputTextComponent } from './components/forms/inputs/input-text/input-text.component';
import { PageTitleComponent } from './components/page-title/page-title.component';
import { PaginationComponent } from './components/pagination/pagination.component';
import { QuestionComponent } from './components/question/question.component';
import { SpinnerComponent } from './components/spinner/spinner.component';
import { ToobarComponent } from './components/toobar/toobar.component';
import { FlexWidth } from './directives/flex-width.directive';
import { MaterialModule } from './modules/material.module';
import { PipesModule } from './pipes/pipes/pipes.module';



@NgModule({
  declarations: [
    DetailComponent,
    SpinnerComponent,
    PageTitleComponent,
    ToobarComponent,
    PaginationComponent,
    QuestionComponent,
    BaseInputComponent,
    InputTextComponent,
    InputNumberComponent,
    InputListComponent,
    FlexWidth
   ],
  imports: [
    CommonModule,
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    RouterModule,


    MaterialModule,
    PipesModule
  ],
  exports:[
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    RouterModule,

    MaterialModule,
    PipesModule,
    DetailComponent,
    SpinnerComponent,
    ToobarComponent,
    PageTitleComponent,
    PaginationComponent,
    QuestionComponent,
    BaseInputComponent,
    InputTextComponent,
    InputNumberComponent,
    InputListComponent,

    FlexWidth,
  ]
})
export class SharedModule { }
