import { BaseInputComponent } from './../base-input/base-input.component';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'ut-input-money',
  templateUrl: './input-money.component.html',
  styleUrls: ['./input-money.component.scss']
})
export class InputMoneyComponent  extends BaseInputComponent implements OnInit {

  isFocused = false
  options = {}

  constructor() {
    super()
  }

  ngOnInit(): void {
   this.options =  "{ prefix: 'R$ ', thousands: '.', decimal: ',' }"
  }

  setFocus(target:any){
    console.log(target)
    target.select()
    this.isFocused = true
  }

  lossFocus(){
    this.isFocused = false
  }

  getDivClass():string {
    if (this.isError()){
       return 'error'
    }
     return this.isFocused ? 'focused' : ''
  }
}
