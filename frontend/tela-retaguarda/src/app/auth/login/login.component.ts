import { Component, OnInit } from '@angular/core';
import { FormGroup , FormBuilder} from '@angular/forms';

import { AuthService } from './../auth.service';


@Component({
  selector: 'ut-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
 
  public formLogin: FormGroup
  public erroLogin: string

  constructor(private auth: AuthService, private formBuilder: FormBuilder) {
    this.erroLogin = ''
    this.formLogin = this.formBuilder.group({
      email:['maria2@paiva.com'],
      password:['tela@123456789'],
      codigo:['MTM0OTAyMzk2MjAwNjAzOQ==']
    })
  }

  ngOnInit(): void {
        
  }

  onLogin() {
    this.auth.onAuthenticate(this.formLogin.value)
    .catch(erro => this.erroLogin = erro)
  }

}
