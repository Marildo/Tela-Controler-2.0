import { Component, OnInit } from '@angular/core'
import {MatSnackBar} from '@angular/material/snack-bar'

@Component({
  selector: 'ut-produtos',
  templateUrl: './produtos.component.html',
  styleUrls: ['./produtos.component.scss']
})
export class ProdutosComponent implements OnInit {

  constructor(private _snackBar: MatSnackBar) { }

  ngOnInit(): void {
  }

  onTest(){
    this._snackBar.open('Cannonball!!', 'X', {
      duration: 38 * 1000,
      horizontalPosition: 'end',
      verticalPosition: 'top',
      panelClass: ['notify-success']
    });
  }
}
