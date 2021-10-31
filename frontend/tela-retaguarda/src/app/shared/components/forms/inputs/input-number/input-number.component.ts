import { BaseInputComponent } from './../base-input/base-input.component';
import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'ut-input-number',
  templateUrl: './input-number.component.html',
  styleUrls: ['./input-number.component.scss']
})
export class InputNumberComponent extends BaseInputComponent implements OnInit {

  @Input() max = "0"
  @Input() min = "0"
  @Input() step = "1"

  constructor() {
    super()
  }

  ngOnInit(): void {
  }
}
