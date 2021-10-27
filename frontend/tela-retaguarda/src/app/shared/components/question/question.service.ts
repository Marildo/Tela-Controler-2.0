import { Injectable } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { QuestionComponent } from './question.component';

@Injectable({
  providedIn: 'root'
})
export class QuestionService {

  constructor(private dialog: MatDialog) { }

  public confirm(text: string): Promise<boolean> {
    return new Promise((resolve, reject) =>{
      const dialogRef = this.dialog.open(QuestionComponent, {
        data: {
            title: 'Confirmação',
            subtitle: text,
            textBtnYes: 'Sim',
            textBtnNo: 'Não',
            textBtnCancel: ''
        } as QuestionParams,
        width: '400px'
      });

     dialogRef.afterClosed()
                      .toPromise().then(resp => {
                         if (resp === 1 )
                          resolve(true)
                         else
                          reject(false)
                      })
                    })
  }
}

export interface QuestionParams {
  title: string
  subtitle: string
  textBtnYes:string
  textBtnNo:string
  textBtnCancel:string
}

export enum QuestionResult{
    YES = 1,
    NO = 0,
    CANCEL = -1
}
