import { Router } from '@angular/router';
import { Injectable } from '@angular/core';
import { ItemMenu } from 'src/app/shared/models/item-menu';

@Injectable({
  providedIn: 'root'
})
export class MenuService {

  private items: Array<ItemMenu> = [
    { title: 'Dashboard', icon: 'dashboard', path: '/dashboard' },
    { title: 'Pedidos', icon: 'receipt_long', path: '/pedidos' },
    { title: 'Produtos', icon: 'inventory', path: '/produtos' },
    { title: 'Clientes', icon: 'supervisor_account', path: '/clientes' },
    { title: 'Financeiro', icon: 'request_page', path: '/financeiro' },
    { title: 'Unidades', icon: 'straighten', path: '/unidades' },
    { title: 'Setores', icon: 'grid_view', path: '/setores' }
  ]


  constructor(private router: Router) { }

  getItemsMenu(): ItemMenu[]{
    return this.items
  }

  getIconByTitle(title:string):string {
    const fi = this.items.filter(i => i.title === title)
    return fi.map(i => i.icon)[0]
  }

  getIconByPath():string {
    const path = this.router.routerState.snapshot.url
    const fi = this.items.filter(i => i.path === path)
    return fi.map(i => i.icon)[0]
  }
}
