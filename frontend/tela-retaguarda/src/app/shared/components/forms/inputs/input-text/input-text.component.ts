import { DatePipe } from '@angular/common';
import { Component, Input, OnInit, PipeTransform } from '@angular/core';
import { PipeEnum } from 'src/app/shared/pipes/pipes-enum';
import { TrimPipe } from 'src/app/shared/pipes/trim.pipe';
import { BaseInputComponent } from './../base-input/base-input.component';

@Component({
  selector: 'ut-input-text',
  templateUrl: './input-text.component.html',
  styleUrls: ['./input-text.component.scss']
})
export class InputTextComponent extends BaseInputComponent implements OnInit {

  @Input() maxlength = "255"
  @Input() minlength = "0"
  @Input() pipeType: PipeEnum = PipeEnum.Undefined

  constructor() {
    super()
  }

  ngOnInit(): void {
  }

  getValue(): string {
    const value = this.formGroup.controls[this.controlName].value
    let result = undefined
    switch (this.pipeType) {
      case PipeEnum.DateTime:
        result = new DatePipe("pt-br").transform(value, "d/M/yyy H:mm:ss") || ''
        break;
    }


    return result || value
  }
}
