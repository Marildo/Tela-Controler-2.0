import { Component, Input, OnChanges, OnInit, SimpleChange } from '@angular/core';

@Component({
  selector: 'ut-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.scss']
})
export class DetailComponent implements OnInit, OnChanges {

  @Input() id = `id-${Math.floor(Math.random() * 1000)}`
  @Input() sumary = ''
  @Input() closed = true

  constructor() { }

  ngOnInit(): void {
  }

  ngOnChanges(changes: { [property: string]: SimpleChange }) {
    let changeClosed: SimpleChange = changes['closed'];
    this.toggleDetail(changeClosed.currentValue)
  }

  private toggleDetail(closed:boolean):void{
    const detail = document.getElementById(this.id) as HTMLDetailsElement
    if (detail){
      detail.open = ! closed
    }
  }
}
