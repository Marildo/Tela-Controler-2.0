import { Component, OnInit } from '@angular/core';
import { ClienteService } from 'src/app/pages/clientes/cliente.service';

@Component({
  selector: 'ut-clientes',
  templateUrl: './clientes.component.html',
  styleUrls: ['./clientes.component.scss']
})
export class ClientesComponent implements OnInit {

  public loading = false;
  public editing = false


  constructor(private clienteService: ClienteService) {
    this.clienteService.onLoaded.subscribe( resp => {
      if (this.loading != resp){
        this.loading = resp
        console.log('resp', resp)
      }
    })
  }

  ngOnInit(): void {

  }

}
