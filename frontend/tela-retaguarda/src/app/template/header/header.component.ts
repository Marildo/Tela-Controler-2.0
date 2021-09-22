import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'ut-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  @Output() toogleMenu = new EventEmitter<void>();
  public expanded:Boolean 
  public iconMenu:string 

  constructor() {
    this.expanded =  true;
    this.iconMenu = 'menu'
  }

  ngOnInit(): void {
  }

  onToogleMenu() {
    this.toogleMenu.emit()
    this.expanded = !this.expanded
    this.iconMenu = this.expanded ? 'menu_open' : 'menu'
  }

}
