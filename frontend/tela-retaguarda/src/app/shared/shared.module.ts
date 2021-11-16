import { FlexLayoutModule } from '@angular/flex-layout';
import { RouterModule } from '@angular/router';
import { PageTitleComponent } from './components/page-title/page-title.component';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { SpinnerComponent } from './components/spinner/spinner.component';
import { ToobarComponent } from './components/toobar/toobar.component';
import { DetailComponent } from './components/detail/detail.component';
import { BaseInputComponent } from './components/forms/inputs/base-input/base-input.component';
import { InputNumberComponent } from './components/forms/inputs/input-number/input-number.component';
import { InputTextComponent } from './components/forms/inputs/input-text/input-text.component';
import { PaginationComponent } from './components/pagination/pagination.component';
import { QuestionComponent } from './components/question/question.component';
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
  ],
  imports: [
    CommonModule,
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    RouterModule,
    FlexLayoutModule,


    MaterialModule,
    PipesModule
  ],
  exports:[
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    RouterModule,
    FlexLayoutModule,

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
  ]
})
export class SharedModule { }
