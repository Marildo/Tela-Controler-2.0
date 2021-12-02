import { BaseInputComponent } from './../base-input/base-input.component';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'ut-input-money',
  templateUrl: './input-money.component.html',
  styleUrls: ['./input-money.component.scss']
})
export class InputMoneyComponent  extends BaseInputComponent implements OnInit {

  @Input() prefix = ''

  options = {}

  constructor() {
    super()
  }

  ngOnInit(): void {
   this.options =  { prefix: this.prefix, thousands: '.', decimal: ',' }
  }
}
