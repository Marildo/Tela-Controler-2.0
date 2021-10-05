import { Component, OnInit } from '@angular/core';
import {MatDialog} from '@angular/material/dialog'

import { Unidade } from './model';
import { UnidadeService } from './unidade.service';
import { UnidadeFormComponent } from './unidade.form/unidade.form.component'

@Component({
  selector: 'ut-unidades',
  templateUrl: './unidades.component.html',
  styleUrls: ['./unidades.component.scss']
})
export class UnidadesComponent implements OnInit {


  public unidades: Array<Unidade> = []
  public displayedColumns = ['id', 'unid', 'descricao', 'fracionavel', 'action']

  constructor(private dialog: MatDialog, private unidadeService: UnidadeService) { }


  ngOnInit(): void {
    this.onload()
  }

  public onload() {
    this.unidades = []
    this.unidadeService.load().subscribe(data => {
      this.unidades = data
    })
  }

  public showForm(){
    const dialogRef = this.dialog.open(UnidadeFormComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

}
