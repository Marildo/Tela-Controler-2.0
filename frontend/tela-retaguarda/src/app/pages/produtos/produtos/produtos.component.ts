import { Component, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { FormsService } from './../../../core/services/forms.service';


@Component({
  selector: 'ut-produtos',
  templateUrl: './produtos.component.html',
  styleUrls: ['./produtos.component.scss']
})
export class ProdutosComponent implements OnInit {

  public formCadastro: FormGroup

  constructor(private fomrsService: FormsService) {
    this.formCadastro = this.fomrsService.buildForm('produtos')
  }

  ngOnInit(): void {

  }
  onSearch(text: String) {
    console.log(text)
  }

  onTest() {
    console.log(this.formCadastro.controls)
    console.log(this.formCadastro.value)
  }


}
