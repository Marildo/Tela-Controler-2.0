import { Component, Input, OnInit } from '@angular/core';
import { BaseInputComponent } from '../base-input/base-input.component';

@Component({
  selector: 'ut-input-date',
  templateUrl: './input-date.component.html',
  styleUrls: ['./input-date.component.scss']
})
export class InputDateComponent  extends BaseInputComponent implements OnInit {


  constructor(){
    super()
  }

  ngOnInit(): void {

  }


  getDateValue(){
    return "2021-01-01 01:01:01"
  }
}
