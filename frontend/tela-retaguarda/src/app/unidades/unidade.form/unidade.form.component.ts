import { Component, OnInit } from '@angular/core'
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { MatDialogRef } from '@angular/material/dialog';


@Component({
  selector: 'ut-unidade.form',
  templateUrl: './unidade.form.component.html',
  styleUrls: ['./unidade.form.component.scss']
})
export class UnidadeFormComponent implements OnInit {

  public formCadastro: FormGroup


  constructor(
    private dialogRef: MatDialogRef<UnidadeFormComponent>,
    private formBuilder: FormBuilder
    ) {
      this.formCadastro = this.formBuilder.group({
        unid:[null],
        descricao: [null],
      })
   }

  ngOnInit(): void {
  }

  onCancel(){
    this.dialogRef.close()
  }

  onSave(){

  }
}
