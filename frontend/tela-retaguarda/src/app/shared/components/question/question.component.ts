import { Component, Inject, OnInit } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { QuestionResult, QuestionParams } from './question.service';

@Component({
  selector: 'ut-question',
  templateUrl: './question.component.html',
  styleUrls: ['./question.component.scss']
})
export class QuestionComponent implements OnInit {

  constructor(  private dialogRef: MatDialogRef<QuestionComponent>,
                @Inject(MAT_DIALOG_DATA) public params: QuestionParams) {

                }

  ngOnInit(): void {
  }

  onYes(){
     this.onClose(QuestionResult.YES)
  }

  onNo(){
    this.onClose(QuestionResult.NO)
 }

  onCancel(){
    this.onClose(QuestionResult.CANCEL)
  }

  private onClose(result: QuestionResult):void{
      this.dialogRef.close(result)
  }
}
