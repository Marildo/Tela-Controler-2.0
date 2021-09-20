import { User } from './../../core/class/user';
import { Component, OnInit } from '@angular/core';

import { AuthService } from './../auth.service';
import { ClassGetter } from '@angular/compiler/src/output/output_ast';

@Component({
  selector: 'ut-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  public user: User

  constructor(private auth: AuthService) {
    this.user = new User
  }

  ngOnInit(): void {
  }

  onLogin() {
    this.auth.onAuthenticate(this.user);
  }

}
