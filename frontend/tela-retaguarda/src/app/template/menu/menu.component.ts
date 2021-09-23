import { animate, state, style, transition, trigger } from '@angular/animations';
import { Component, Input, OnInit, SimpleChange } from '@angular/core'

@Component({
  selector: 'ut-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss'],
  animations: [
    trigger('toggle',[
      state('small', style({
          width: 60
      })),
      state('large', style({
        width: 200
    })),
    transition('large <=> small', animate('.6s ease-in-out'))
    ])
  ]
})
export class MenuComponent implements OnInit {


  @Input() public expandMenu: Boolean;
  public toggleMenu: string = 'large'

  constructor() {
    this.expandMenu = true
  }

  ngOnInit(): void {
  }

  ngOnChanges(changes: { [property: string]: SimpleChange }){
    let changeExpandMenu: SimpleChange = changes['expandMenu']; 
    this.toggleMenu = changeExpandMenu.currentValue ? 'large' : 'small'   
 }

}


// TODO - Alterar comunicacao entre componentes para service