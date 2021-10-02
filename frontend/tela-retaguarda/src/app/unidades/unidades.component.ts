import { Component, OnInit } from '@angular/core';

import { Unidade } from './model';
import { UnidadeService } from './unidade.service';


interface Resp {
  data: Array<any>
}

@Component({
  selector: 'ut-unidades',
  templateUrl: './unidades.component.html',
  styleUrls: ['./unidades.component.scss']
})
export class UnidadesComponent implements OnInit {



  public unidades: Array<Unidade> = []
  public displayedColumns = ['id', 'unid', 'descricao', 'fracionavel', 'action']



  constructor(private unidadeService: UnidadeService) { }



  ngOnInit(): void {
    this.onload()
  }

  public onload() {
    this.unidadeService.load().subscribe(resp => {
      this.unidades = resp.data
    })
  }

}
