import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import jwtDecode from 'jwt-decode';
import { User } from '../../shared/models/user';

import { environment } from '../../../environments/environment';

interface TokenData {
  exp: Number;
  payload: string;
}

// TODO - separar metodos, class e interfaces

@Injectable({ providedIn: 'root' })
export class AuthService {
  private TOKEN_NAME = 'usertokenuttc'
  private user = new User()
  private previousUrl = '/'
  public token  = ''

  constructor(private http: HttpClient, private router: Router) {

  }

  public onAuthenticate(data: any): Promise<string> {
    const onAuth = new Promise<string>((resolve, reject) => {
      this.http
        .post<any>(`${environment.apiUrl}/login`, data)
        .toPromise()
        .then((resp) => {
          this.saveToke(resp.token);
          if (this.validToken()) {
            this.router.navigate([this.previousUrl]);
          }
          resolve('Ok');
        })
        .catch((data) => reject(data.error));
    });

    return onAuth;
  }

  public onLogout(): void {
    this.user = new User();
    const storage: Storage = window.localStorage;
    storage.removeItem(this.TOKEN_NAME);
    this.router.navigate(['/login']);
  }

  public isLogged(previousUrl: string): boolean {
    this.previousUrl = previousUrl;
    const logged = this.user?.id != undefined;
    return logged || this.validToken();
  }

  public redirectIfLogged(): void {
    if (this.isLogged('/')) {
      this.router.navigate([this.previousUrl]);
    }
  }

  public getUserName(): any {
    return this.user?.nome;
  }

  private saveToke(token: string): void {
    const storage: Storage = window.localStorage;
    storage.setItem(this.TOKEN_NAME, token);
  }

  private validToken(): boolean {
    const storage: Storage = window.localStorage;
    const token = storage.getItem(this.TOKEN_NAME);
    if (token != undefined) {
      const data: TokenData = jwtDecode(token);
      if (this.validate_expire(data.exp)) {
        this.token = token
        this.user = this.validate_payload(data.payload);
      }
    }
    return this.user?.id != undefined;
  }

  private validate_expire(exp: any) {
    const today = new Date();
    const expDate = new Date(exp * 1000);
    return expDate > today;
  }

  private validate_payload(payload: any): User {
    const data = atob(payload);
    const user: User = JSON.parse(data);

    user.permissoes?.forEach((item) => {
      let auth = item.auth + '';
      const verify = auth.substring(auth.length - 5);
      auth = parseInt(auth.replace(verify, '')) / 3 + '';

      const total = auth
        .split('')
        .map((i) => parseInt(i))
        .reduce((c, n) => c + n);

      item.auth = total === parseInt(verify) ? parseInt(auth) : -1;
    });

    const valid_permissions =
      user.permissoes?.filter((item) => item.auth < 0).length === 0;
    return valid_permissions ? user : new User();
  }
}
