import { Pagination } from './../../shared/models/pagination';
import { Component, OnInit } from '@angular/core';
import { Cliente } from '@entity/cliente';
import { ClienteService } from 'src/app/pages/clientes/cliente.service';

@Component({
  selector: 'ut-clientes',
  templateUrl: './clientes.component.html',
  styleUrls: ['./clientes.component.scss']
})
export class ClientesComponent implements OnInit {

  public loading = false;
  public editing = false
  public clientes: Array<Cliente> = []
  public pagination: Pagination = new Pagination()
  public displayedColumns = ['id', 'fantasia','cpf', 'ativo', 'action']

  constructor(private clienteService: ClienteService) { }

  ngOnInit(): void {
    this.onLoad()
  }


  private onLoad(page: number = 1, text: string = '') {
    this.loading = true
    this.clientes = []
    let size = 10
    this.clienteService.load(page, size, text)
      .subscribe(resp => {
         this.clientes = resp.data
         this.clientes.forEach(item => item.getDocument =  () => {
             return  item.cnpj || item.cpf
         })
         console.log(this.clientes)

        this.pagination = resp.pagination
        this.loading = false
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
