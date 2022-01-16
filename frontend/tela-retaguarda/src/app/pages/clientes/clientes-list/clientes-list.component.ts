import { ClienteService } from 'src/app/pages/clientes/cliente.service';
import { Pagination } from 'src/app/shared/models/pagination';
import { Cliente } from '@entity/cliente';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'ut-clientes-list',
  templateUrl: './clientes-list.component.html',
  styleUrls: ['./clientes-list.component.scss']
})
export class ClientesListComponent implements OnInit {

  public clientes: Array<Cliente> = []
  public pagination: Pagination = new Pagination()
  public displayedColumns = ['id', 'fantasia','cpf', 'ativo', 'action']

  constructor(private clienteService: ClienteService) { }

  ngOnInit(): void {
    this.onLoad()
  }


  private onLoad(page: number = 1, text: string = '') {
    this.clientes = []
    let size = 10
    this.clienteService.load(page, size, text)
      .subscribe(resp => {
         this.clientes = resp.data
         this.clientes.forEach(item => item.getDocument =  () =>  item.cnpj || item.cpf)
         console.log(this.clientes)

        this.pagination = resp.pagination
      })
  }

  onSearch(text: string) {
    this.onLoad(1, text)
  }

  public onNewItem() {
    // this.clienteService.onLoaded.subscribe().unsubscribe()
    // this.router.navigate(['/produtos/novo'])

    console.log(this.clientes[0].getDocument())
  }


  public editItem(id: number) {
    // this.clienteService.onLoaded.subscribe().unsubscribe()
    // this.router.navigate(['/produtos/', id])
  }

  onChangePage(page: number) {
    this.onLoad(page)
  }


  public deleteItem(_id: number) {

  }

}
