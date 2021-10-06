import { Injectable } from '@angular/core'
import { MatSnackBar } from '@angular/material/snack-bar'

@Injectable({
  providedIn: 'root'
})
export class NotifyService {

  constructor(private _snackBar: MatSnackBar) { }

  public success(text: string, _duration: number = 5) {
    this._snackBar.open(text, 'x', {
      duration: _duration * 1000,
      horizontalPosition: 'end',
      verticalPosition: 'top',
      panelClass: ['notify-success']
    });
  }
}
