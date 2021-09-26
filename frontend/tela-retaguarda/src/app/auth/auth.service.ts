import { HttpClient } from '@angular/common/http';
import { User } from './../core/class/user';
import { Injectable } from '@angular/core';

import { environment } from './../../environments/environment';

import jwtDecode from 'jwt-decode';

interface TokenData {
  exp:Number,
  payload: Object
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {



  private TOKEN_NAME = 'usertokenuttc'
  private user: User

  constructor(private http: HttpClient) {
    this.user = new User()
  }

  onAuthenticate(data: any): void {
    this.http.post<any>(`${environment.apiUrl}/login`, data)
      .subscribe(resp => {
        this.saveToke(resp.token)
        this.validToken()
      });
  }

  private saveToke(token: string): void {
    const storage: Storage = window.localStorage;
    storage.setItem(this.TOKEN_NAME, token)
  }

  private validToken(): boolean {
    const storage: Storage = window.localStorage;
    const token = storage.getItem(this.TOKEN_NAME) || ''
    const data: TokenData = jwtDecode(token)
    console.log(data.payload)

    return false
  }
}
