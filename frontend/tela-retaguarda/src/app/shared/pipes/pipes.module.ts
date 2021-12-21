import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { TrimPipe } from './trim.pipe';
import { YesNoPipe } from './yes-no.pipe';



@NgModule({
  declarations: [
    YesNoPipe,
    TrimPipe
  ],

  imports: [
    CommonModule
  ],
  exports: [
    YesNoPipe,
    TrimPipe
  ]
})
export class PipesModule { }
