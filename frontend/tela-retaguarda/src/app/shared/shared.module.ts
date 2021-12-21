import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RouterModule } from '@angular/router';
import { NgxCurrencyModule } from 'ngx-currency';
import { InputDateComponent } from 'src/app/shared/components/forms/inputs/input-date/input-date.component';
import { DetailComponent } from './components/detail/detail.component';
import { BaseInputComponent } from './components/forms/inputs/base-input/base-input.component';
import { InputCheckboxComponent } from './components/forms/inputs/input-checkbox/input-checkbox.component';
import { InputListComponent } from './components/forms/inputs/input-list/input-list.component';
import { InputMoneyComponent } from './components/forms/inputs/input-money/input-money.component';
import { InputNumberComponent } from './components/forms/inputs/input-number/input-number.component';
import { InputTextComponent } from './components/forms/inputs/input-text/input-text.component';
import { PageTitleComponent } from './components/page-title/page-title.component';
import { PaginationComponent } from './components/pagination/pagination.component';
import { QuestionComponent } from './components/question/question.component';
import { SpinnerComponent } from './components/spinner/spinner.component';
import { ToobarComponent } from './components/toobar/toobar.component';
import { FlexWidth } from './directives/flex-width.directive';
import { MaterialModule } from './modules/material.module';
import { PipesModule } from './pipes/pipes.module';



// TODO - Muda para um arquivo de configuracao
export const customCurrencyMaskConfig = {
  align: "right",
  allowNegative: true,
  allowZero: true,
  decimal: ",",
  precision: 2,
  prefix: "R$ ",
  suffix: "",
  thousands: ".",
  nullable: true
};


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
    InputDateComponent,
    InputNumberComponent,
    InputMoneyComponent,
    InputListComponent,
    InputCheckboxComponent,

    FlexWidth,
    InputMoneyComponent,
    InputCheckboxComponent,
   ],
  imports: [
    CommonModule,
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    RouterModule,


    MaterialModule,
    PipesModule,

    NgxCurrencyModule.forRoot(customCurrencyMaskConfig)
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
    InputDateComponent,
    InputNumberComponent,
    InputMoneyComponent,
    InputListComponent,
    InputCheckboxComponent,

    FlexWidth,
  ]
})
export class SharedModule { }
