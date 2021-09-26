import { HttpClient } from '@angular/common/http';
import { User } from './../core/class/user';
import { Injectable } from '@angular/core';

import { environment } from './../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private user: User
  
  constructor(private http: HttpClient) {
    this.user = new User()
   }

  onAuthenticate(data: any):void{
    console.log(data)
    this.http.post<any>(`${environment.apiUrl}/login`,data)
      .subscribe(resp => console.log(resp));
  }
}
