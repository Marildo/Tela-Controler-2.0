import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'ut-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  cadastro:FormGroup

  constructor( private formBuilder: FormBuilder,) {
    this.cadastro = this.formBuilder.group({
      nome: ['Ma',[Validators.required, Validators.minLength(2), Validators.maxLength(6)]],
      idade:[null,[Validators.required, Validators.max(10), Validators.min(-5)]]
    })
   }

  ngOnInit(): void {
  }

  onSubmited(){
    console.log(this.cadastro.value)
  }
}
