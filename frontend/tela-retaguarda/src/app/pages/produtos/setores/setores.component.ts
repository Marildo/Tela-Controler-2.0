import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'ut-setores',
  templateUrl: './setores.component.html',
  styleUrls: ['./setores.component.scss']
})
export class SetoresComponent implements OnInit {

  loading = false

  constructor() { }

  ngOnInit(): void {
  }

  addSetor(){

  }

  onSearch(text: string) {
    console.log(text)
  }
}
