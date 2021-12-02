import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'ut-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  cadastro:FormGroup

  detailClosed = true

  hoje = new Date()

  constructor( private formBuilder: FormBuilder,) {
    this.cadastro = this.formBuilder.group({
      nome: ['Ma',[Validators.required, Validators.minLength(2), Validators.maxLength(6)]],
      idade:[null,[Validators.required, Validators.max(10), Validators.min(-5)]],
      valor:[null,[Validators.required, Validators.max(1000), Validators.min(-5)]],
      desconto:[null,[Validators.required, Validators.max(1000), Validators.min(-5)]]
    })
   }

  ngOnInit(): void {
  }

  onSubmited(){
    console.log(this.cadastro.value)
  }

  test(){
    // const detailClientConnector = document.getElementById('detail-test') as HTMLDetailsElement
    // if (detailClientConnector){
    //   detailClientConnector.open = ! detailClientConnector.open
    // }
    this.detailClosed = !  this.detailClosed
  }
}
