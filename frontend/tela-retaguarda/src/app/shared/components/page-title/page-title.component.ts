import { MenuService } from './../../../core/services/menu.service';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'ut-page-title',
  templateUrl: './page-title.component.html',
  styleUrls: ['./page-title.component.scss']
})
export class PageTitleComponent implements OnInit {


  @Input() title = ''
  @Input() loading = false
  @Input() icon = ''


  constructor(private menuService: MenuService) {
  }

  ngOnInit(): void {
     if (this.icon == ''){
       this.icon =  this.menuService.getIconByPath()
     }
  }

}
