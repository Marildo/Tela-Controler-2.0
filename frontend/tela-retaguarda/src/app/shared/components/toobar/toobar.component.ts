import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Router } from '@angular/router';
import { debounceTime, distinctUntilChanged, map, tap } from 'rxjs/operators';
import { MenuService } from './../../../core/services/menu.service';

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

  constructor(private router: Router, private menuService: MenuService) {
    this.search.valueChanges
      .pipe(
        map(v => v.trim()),
        debounceTime(200), // esperar 200 ms
        distinctUntilChanged(), // somente se o valor mudar
        tap(a => console.log(a)),
      ).subscribe(text => this.eventSearch.emit(text))
  }

  ngOnInit(): void {
     if (this.icon == ''){
       this.icon =  this.menuService.getIconByPath(this.router.routerState.snapshot.url)
     }
  }

  onNew(){
    this.eventNew.emit()
  }

}
