import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

import { AuthService } from './../auth.service';


@Component({
  selector: 'ut-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  public formLogin: FormGroup
  public erroLogin: String

  constructor(private formBuilder: FormBuilder, private auth: AuthService) {
    this.erroLogin = ''
    this.formLogin = this.formBuilder.group({
      email: ['maria2@paiva.com', [Validators.required, Validators.email]],
      password: ['tela@123456789'],
      codigo: ['MTM0OTAyMzk2MjAwNjAzOQ==']
    })
  }

  ngOnInit(): void {
    this.auth.redirectIfLogged()
  }

  onLogin() {
    this.auth.onAuthenticate(this.formLogin.value)
      .catch(erro =>  this.erroLogin = (erro instanceof String) ? erro : 'Erro desconhecido')
  }

}
