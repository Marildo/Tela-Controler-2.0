import { Unidade } from './../model';
import { NotifyService } from 'src/app/shared/services/notify.service'
import { UnidadeService } from './../unidade.service';
import { Component, OnInit, Inject } from '@angular/core'
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { MatDialogRef ,MAT_DIALOG_DATA} from '@angular/material/dialog';


@Component({
  selector: 'ut-unidade.form',
  templateUrl: './unidade.form.component.html',
  styleUrls: ['./unidade.form.component.scss']
})
export class UnidadeFormComponent implements OnInit {

  // TODO - Criar um componente especifico para footer de formulario

  public formCadastro: FormGroup
  public error = ''
  public title = ''

  constructor(
    private dialogRef: MatDialogRef<UnidadeFormComponent>,
    @Inject(MAT_DIALOG_DATA) private unidade: Unidade,
    private formBuilder: FormBuilder,
    private unidadeService: UnidadeService,
    private notify: NotifyService
    ) {
      this.formCadastro = this.formBuilder.group({
        id: [null],
        unid:[null, [Validators.required, Validators.minLength(2), Validators.maxLength(6)]],
        descricao: [null,[Validators.required, Validators.minLength(2), Validators.maxLength(30)] ],
        fracionavel:[false],
        ativo:[true]
      })

      // TODO - Quando for inserir em apenas algunas campos
      //  this.formCadastro.patchValue({ id:unidade.id , unid: unidade.unid    })
      this.formCadastro.setValue(this.unidade)

      this.title = unidade.id === 0 ? 'Nova Unidade':'Edição de Unidade'
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
        this.notify.success('Operacao realizada com sucesso!')
        this.dialogRef.close(success)
      },
      resp_error => {
        // TODO - tratar erros de forma generica
        console.log(resp_error.error.data[0]  )
        this.error = resp_error.error.data.error.description
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
