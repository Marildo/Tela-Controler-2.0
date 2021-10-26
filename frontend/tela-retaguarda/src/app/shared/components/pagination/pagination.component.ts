import { Pagination } from '../../models/pagination';
import { Component, Input, OnChanges, OnInit, Output, EventEmitter } from '@angular/core';


@Component({
  selector: 'ut-pagination',
  templateUrl: './pagination.component.html',
  styleUrls: ['./pagination.component.scss']
})
export class PaginationComponent implements OnInit, OnChanges {

  @Input() pagination: Pagination = new Pagination()

  @Output() eventChangePage = new EventEmitter<number>()

  pages: [number] = [1]

  constructor() {

  }

  ngOnInit(): void {
  }

  ngOnChanges(): void {
    this.calculePages()
  }

  onLoadPage(page: number) {
    this.eventChangePage.emit(page)
  }

  onNextPage() {
    this.onLoadPage(this.pagination.page + 1)
  }
  onPreviusPage() {
    this.onLoadPage(this.pagination.page - 1)
  }

  disabled_previous() {
    return this.pagination.page === 1
  }

  disabled_next() {
    return this.pagination.page === this.pagination.total_pages
  }


  private calculePages(): void {
    this.pages = [0]
    this.pages.shift()


    let end = 1
    let items_before = 0
    for (let index = this.pagination.page; index >= end && items_before < 5; index--) {
      items_before++
      this.pages.push(index)
    }


    let x = this.pagination.page + 5 < 10 ? 10 : this.pagination.page + 5
    end = this.pagination.total_pages < x ? this.pagination.total_pages : x
    for (let index = this.pagination.page + 1; index <= end; index++) {
      this.pages.push(index)
    }
    this.pages.sort((c, n) => c - n)

    if (this.pages.length < 10 && this.pagination.total_pages > 10) {
      let index = this.pages[0]
      while (this.pages.length < 10 && index >= 1) {
        index--
        this.pages.push(index)
      }
      this.pages.sort((c, n) => c - n)
    }
  }

}
