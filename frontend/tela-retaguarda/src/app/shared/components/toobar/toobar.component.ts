import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { FormControl } from '@angular/forms';
import { debounceTime, distinctUntilChanged, map, tap } from 'rxjs/operators';

@Component({
  selector: 'ut-toobar',
  templateUrl: './toobar.component.html',
  styleUrls: ['./toobar.component.scss']
})
export class ToobarComponent implements OnInit {

  @Input() title = ''
  @Input() loading = false
  @Input() icon = ''

  @Output() eventSearch = new EventEmitter<string>()
  @Output() eventNew = new EventEmitter<any>()

  public search = new FormControl()

  constructor() {
    this.search.valueChanges
      .pipe(
        map(v => v.trim()),
        debounceTime(200), // esperar 200 ms
        distinctUntilChanged(), // somente se o valor mudar
        tap(a => console.log(a)),
      ).subscribe(text => this.eventSearch.emit(text))
  }

  ngOnInit(): void {

  }

  onNew(){
    this.eventNew.emit()
  }

}
