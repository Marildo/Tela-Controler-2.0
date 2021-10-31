import { Component, Input, OnInit } from '@angular/core';
import { BaseInputComponent } from './../base-input/base-input.component';

@Component({
  selector: 'ut-input-text',
  templateUrl: './input-text.component.html',
  styleUrls: ['./input-text.component.scss']
})
export class InputTextComponent  extends BaseInputComponent implements OnInit {

  @Input() maxlength = "255"
  @Input() minlength = "0"

  constructor(){
    super()
  }

  ngOnInit(): void {
  }
}
