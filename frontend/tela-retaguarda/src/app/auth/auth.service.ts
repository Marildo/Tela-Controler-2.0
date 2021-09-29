import { HttpClient } from '@angular/common/http';
import { User } from './../core/class/user';
import { Injectable } from '@angular/core';

import { environment } from './../../environments/environment';

import jwtDecode from 'jwt-decode';
import { Router } from '@angular/router';


interface TokenData {
  exp: Number,
  payload: string
}

// TODO - separar metodos, class e interfaces

@Injectable({ providedIn: 'root' })
export class AuthService {

  private TOKEN_NAME = 'usertokenuttc'
  private user: User
  private previousUrl: string

  constructor(private http: HttpClient, private router: Router) {
    this.user = new User
    this.previousUrl = '/'
  }

  public onAuthenticate(data: any): void {
    this.http.post<any>(`${environment.apiUrl}/login`, data)
      .subscribe(resp => {
        this.saveToke(resp.token)
        if (this.validToken()){
          this.router.navigate([this.previousUrl])
        }
      });
  }

  public onLogout(): void {
    this.user = new User()
    const storage: Storage = window.localStorage;
    storage.removeItem(this.TOKEN_NAME) 
    this.router.navigate(['/login'])
  }

  public isLogged(previousUrl:string): boolean {
    this.previousUrl = previousUrl
    const logged =  this.user?.id != undefined
    return logged || this.validToken() 
  }

  public getUserName(): any {
    return this.user?.nome
  }

  private saveToke(token: string): void {
    const storage: Storage = window.localStorage;
    storage.setItem(this.TOKEN_NAME, token)
  }

  private validToken(): boolean {
    const storage: Storage = window.localStorage;
    const token = storage.getItem(this.TOKEN_NAME) || undefined
    if (token != undefined){
      const data: TokenData = jwtDecode(token)
      if (this.validate_expire(data.exp)) {
        this.user = this.validate_payload(data.payload)
      }
    }
    return  this.user?.id != undefined
  }

  private validate_expire(exp: any) {
    const today = new Date()
    const expDate = new Date().setUTCSeconds(exp)
    return expDate.valueOf() > today.valueOf()
  }

  private validate_payload(payload: any): User {
    const data = atob(payload)
    const user: User = JSON.parse(data)

    user.permissoes?.forEach(item => {
      let auth = item.auth + ''
      const verify = auth.substring(auth.length - 5)
      auth = parseInt(auth.replace(verify, '')) / 3 + ''

      const total = auth.split('')
        .map(i => parseInt(i))
        .reduce((c, n) => c + n)

      item.auth = total === parseInt(verify) ? parseInt(auth) : -1
    })

    const valid_permissions = user.permissoes?.filter(item => item.auth < 0).length === 0
    return valid_permissions ? user : new User
  }
}
