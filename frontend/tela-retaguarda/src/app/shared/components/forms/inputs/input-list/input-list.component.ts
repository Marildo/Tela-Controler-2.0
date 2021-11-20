import { TelaResponse } from './../../../../models/tela-response';
import { tap, debounceTime, distinctUntilChanged } from 'rxjs/operators';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';
import { BaseInputComponent } from './../base-input/base-input.component';
import { Component, OnInit, Input } from '@angular/core';
import {  Observable, of } from 'rxjs';

@Component({
  selector: 'ut-input-list',
  templateUrl: './input-list.component.html',
  styleUrls: ['./input-list.component.scss']
})
export class InputListComponent extends BaseInputComponent implements OnInit {

  @Input() dataSourceObservable: Observable<TelaResponse> = of()

  field_aux = new FormControl()
  dataList:Array<any> = []

  constructor(private formBuilder: FormBuilder) {
    super()
  }

  ngOnInit(): void {
    this.dataSourceObservable.subscribe(resp => this.dataList = resp.data)

    const originalField = this.formGroup.controls[this.controlName]
    if (originalField?.validator)
     this.field_aux.validator = originalField.validator

    this.field_aux.valueChanges
      .pipe(
        // map(v => v.trim()),
         debounceTime(200),
         distinctUntilChanged(),
        tap(a => console.log(a)),
      ).subscribe(value => {
        const item = this.dataList.filter(i => i.unid === value)
        const newValue = item.length > 0 ? item[0] : ""
        this.formGroup.get(this.controlName)?.setValue(newValue)
      })

  }

}
