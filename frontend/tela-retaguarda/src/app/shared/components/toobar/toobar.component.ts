import { map, debounceTime, distinctUntilChanged, tap } from 'rxjs/operators';
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'ut-toobar',
  templateUrl: './toobar.component.html',
  styleUrls: ['./toobar.component.scss']
})
export class ToobarComponent implements OnInit {

  @Input() title = ''
  @Output() eventSearch = new EventEmitter<String>()
  @Output() eventNew = new EventEmitter<any>()

  public search = new FormControl()

  constructor() {
    this.search.valueChanges
      .pipe(
        map(v => v.trim()),
        debounceTime(200), // esperar 200 millesegundo
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
