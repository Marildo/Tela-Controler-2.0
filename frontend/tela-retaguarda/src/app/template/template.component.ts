import { Component, OnInit, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'ut-template',
  templateUrl: './template.component.html',
  styleUrls: ['./template.component.scss']
})
export class TemplateComponent implements OnInit {

  

  constructor() { }

  ngOnInit(): void {
  }

  onToogleMenu() {
    console.log('testsss')
  }

}
