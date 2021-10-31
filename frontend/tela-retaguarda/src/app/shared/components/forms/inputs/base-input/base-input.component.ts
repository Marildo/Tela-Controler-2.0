import { FormGroup } from '@angular/forms';
import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'ut-base-input',
  templateUrl: './base-input.component.html',
  styleUrls: ['./base-input.component.scss']
})
export class BaseInputComponent implements OnInit {

  @Input() formGroup: FormGroup
  @Input() controlName = ''
  @Input() title = ''
  @Input() readonly = false

  constructor() {
    this.formGroup = new FormGroup({})
  }

  ngOnInit(): void {
  }

  getErrors(): Array<string> {
    const control = this.formGroup.controls[this.controlName]
    const errors = ['']

    if (control.status === 'VALID')
      return errors

    const required = control.errors?.required ?? false
    if (required)
      errors.push('Campo obrigatório')

    const minlength = control.errors?.minlength ?? false
    if (minlength)
      errors.push(`Tamanho mínino de ${minlength.requiredLength} caracteres`)

    const maxlength = control.errors?.maxlength ?? false
    if (maxlength)
      errors.push(`Tamanho máximo de ${maxlength.requiredLength} caracteres`)

    return errors
  }

}
