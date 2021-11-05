import { YesNoPipe } from './../yes-no.pipe';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';



@NgModule({
  declarations: [
    YesNoPipe
  ],

  imports: [
    CommonModule
  ],
  exports: [
    YesNoPipe
  ]
})
export class PipesModule { }
