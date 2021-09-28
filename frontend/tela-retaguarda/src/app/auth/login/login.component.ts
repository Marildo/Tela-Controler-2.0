import { ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';

import { AuthService } from './../auth.service';
import { FormGroup , FormBuilder} from '@angular/forms';

@Component({
  selector: 'ut-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
 
  public formLogin: FormGroup;

  constructor(private route: ActivatedRoute, private auth: AuthService, private formBuilder: FormBuilder) {
    this.formLogin = this.formBuilder.group({
      email:['maria2@paiva.com'],
      password:['123456789'],
      codigo:['MTM0OTAyMzk2MjAwNjAzOQ==']
    })
  }

  ngOnInit(): void {
        
  }

  onLogin() {
    this.auth.onAuthenticate(this.formLogin.value);
  }

}
