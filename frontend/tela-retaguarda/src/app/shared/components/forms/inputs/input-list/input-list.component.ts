import { Component, Input, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Observable, of } from 'rxjs';
import { debounceTime, distinctUntilChanged, tap } from 'rxjs/operators';
import { TelaResponse } from './../../../../models/tela-response';
import { BaseInputComponent } from './../base-input/base-input.component';

@Component({
  selector: 'ut-input-list',
  templateUrl: './input-list.component.html',
  styleUrls: ['./input-list.component.scss']
})
export class InputListComponent extends BaseInputComponent implements OnInit {

  @Input() displayField: string = ''
  @Input() dataSourceObservable: Observable<TelaResponse> = of()

  dataList_id:string=''

  field_aux = new FormControl()
  dataList:Array<any> = []

  constructor() {
    super()
  }

  ngOnInit(): void {
    this.dataList_id = this.title+'_list'
    this.dataSourceObservable.subscribe(resp => this.dataList = resp.data)


    this.field_aux.valueChanges
      .pipe(
        // map(v => v.trim()),
         debounceTime(200),
         distinctUntilChanged(),
        // tap(a => console.log(a)),
      ).subscribe(value => {
        const item = this.dataList.filter(i => i[this.displayField] === value)
        const newValue = item.length > 0 ? item[0] : ""
        this.formGroup.get(this.controlName)?.setValue(newValue)
      })

    const originalField = this.formGroup.controls[this.controlName]
    if (originalField?.validator)
    this.field_aux.validator = originalField.validator

      originalField.valueChanges.subscribe(v => {
        this.field_aux.setValue(v[this.displayField])
      })
  }

}
