import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'ut-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss']
})
export class MenuComponent implements OnInit {


  @Output() toogleMenu = new EventEmitter<void>();

  constructor() {

  }

  ngOnInit(): void {
  }

  onToogleMenu() {
    this.toogleMenu.emit()
  }

}
