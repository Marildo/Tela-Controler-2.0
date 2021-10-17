import { AuthService } from '../../../auth/auth.service';
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

  constructor(private auth: AuthService) {
    this.expanded =  true;
    this.iconMenu = 'menu'
  }

  ngOnInit(): void {
  }

  public onToogleMenu() {
    this.toogleMenu.emit()
    this.expanded = !this.expanded
    this.iconMenu = this.expanded ? 'menu_open' : 'menu'
  }

  public getUserName(){
    return this.auth.getUserName()
  }

  public onLogout() {
    this.auth.onLogout()
  }
}
