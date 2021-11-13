import { ProdutoService } from './../produto.service';
import { FormGroup } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'ut-produto-edit',
  templateUrl: './produto-edit.component.html',
  styleUrls: ['./produto-edit.component.scss']
})
export class ProdutoEditComponent implements OnInit {

  public formCadastro: FormGroup;

  constructor(private activeRoute: ActivatedRoute, private produtoService: ProdutoService) {
    this.formCadastro = this.produtoService.fomrService.buildForm('produtos')
   }

  ngOnInit(): void {
  }

}
