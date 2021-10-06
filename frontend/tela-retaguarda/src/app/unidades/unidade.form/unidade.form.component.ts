import { NotifyService } from './../../shared/notify.service';
import { UnidadeService } from './../unidade.service';
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
  public error = ''


  constructor(
    private dialogRef: MatDialogRef<UnidadeFormComponent>,
    private formBuilder: FormBuilder,
    private unidadeService: UnidadeService,
    private notify: NotifyService
    ) {
      this.formCadastro = this.formBuilder.group({
        unid:[null, [Validators.required, Validators.minLength(2), Validators.maxLength(6)]],
        descricao: [null,[Validators.required, Validators.minLength(2), Validators.maxLength(30)] ],
        fracionavel:[false],
        ativo:[true]
      })
   }

  ngOnInit(): void {
  }

  onCancel(){
    this.dialogRef.close()
  }

  onSave(){
    this.unidadeService.save(this.formCadastro.value)
    .subscribe(
      success =>{
        this.notify.success('Unidade cadastrada com sucesso')
        this.dialogRef.close(success)
      },
      error => {
        this.error = error.error.data.error.description
      }
    )
  }


  getErrorMessage(fieldName:string): string {
    const control = this.formCadastro.controls[fieldName]
    if (control.status === 'VALID')
      return ''

    const required = control.errors?.required ?? false
    if (required)
      return 'Campo obrigatório'

    const minlength = control.errors?.minlength ?? false
    if (minlength)
      return `Tamanho mímino de ${minlength.requiredLength} caracteres`

    return ''
  }
}
