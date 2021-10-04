import { Component, OnInit } from '@angular/core';

import { Unidade } from './model';
import { UnidadeService } from './unidade.service';

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
    this.unidades = []
    this.unidadeService.load().subscribe(data => {
      this.unidades = data
    })
  }

}
