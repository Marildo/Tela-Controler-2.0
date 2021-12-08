import { BaseInputComponent } from './../base-input/base-input.component';
import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'ut-input-checkbox',
  templateUrl: './input-checkbox.component.html',
  styleUrls: ['./input-checkbox.component.scss']
})
export class InputCheckboxComponent extends BaseInputComponent implements OnInit {

  @Input() checked = false

  constructor(){
    super()
  }

  ngOnInit(): void {
  }

  getDivClass():string {
    if (this.isError()){
      return 'error-checkbox'
   }
       return this.isFocused ? 'focused-checkbox' : ''
  }
}
