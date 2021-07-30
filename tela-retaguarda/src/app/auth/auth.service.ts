import { HttpClient } from '@angular/common/http';
import { User } from './../core/class/user';
import { Injectable } from '@angular/core';

import { environment } from './../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  
  constructor(private http: HttpClient) { }

  onAuthenticate(user: User):void{
    this.http.post<any>(`${environment.apiUrl}/login`,user)
      .subscribe(data => console.log(data));
    
  }
}
