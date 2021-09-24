import { BreakpointState } from '@angular/cdk/layout';
import { animate, state, style, transition, trigger } from '@angular/animations';
import { AfterViewInit, Component, Input, OnDestroy, OnInit, SimpleChange } from '@angular/core'
import { ScreenService } from '../screen.service'
import { delay } from 'rxjs/operators';
import { Menu } from './menu.model';


@Component({
  selector: 'ut-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss'],
  animations: [
    trigger('toggle', [
      state('small',
        style({
          width: '{{smWidth}}'
        }), { params: { smWidth: 35 } }),

      state('large',
        style({
          width: '{{lgWidth}}'
        }), { params: { lgWidth: 160 } }),

      transition('large <=> small', animate('.8s ease-in-out'))
    ])
  ]
})
export class MenuComponent implements OnInit, OnDestroy, AfterViewInit {


  @Input() public expandMenu: Boolean;
  public toggleMenu: string = 'large'
  public smWidth = '35px';
  public lgWidth = '160px';

  public itemsMenu:Array<Menu> = [
    { title: 'Dashboard', icon: 'dashboard', path: '/dashboard'},
    { title: 'Pedidos', icon: 'receipt_long', path: '/pedidos'},
    { title: 'Produtos', icon: 'inventory', path: '/produtos'},
    { title: 'Clientes', icon: 'supervisor_account', path: '/clientes'},
    { title: 'Financeiro', icon: 'request_page', path: '/financeiro'}
  ]


  constructor(private screenService: ScreenService) {
    this.expandMenu = true
  }

  ngOnInit(): void {
  }

  ngAfterViewInit(): void {
    this.screenService.isBelowSm()
      .pipe(delay(200))
      .subscribe((isBelowSm: BreakpointState) => {
      let isBSm = isBelowSm.matches;
      this.smWidth = isBSm ? '0' : '35px'
    });

  }


  ngOnChanges(changes: { [property: string]: SimpleChange }) {
    let changeExpandMenu: SimpleChange = changes['expandMenu'];
    this.toggleMenu = changeExpandMenu.currentValue ? 'large' : 'small'
  }

  ngOnDestroy(): void {
    this.screenService.isBelowSm().subscribe().unsubscribe()
  }

}
