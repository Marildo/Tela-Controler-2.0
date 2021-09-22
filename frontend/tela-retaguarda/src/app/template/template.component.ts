import { Component, OnInit, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'ut-template',
  templateUrl: './template.component.html',
  styleUrls: ['./template.component.scss']
})
export class TemplateComponent implements OnInit {

  public expandMenu:Boolean

  constructor() { 
    this.expandMenu = true
  }

  ngOnInit(): void {
  }

  onToogleMenu() {
    this.expandMenu = !this.expandMenu
  }

}
