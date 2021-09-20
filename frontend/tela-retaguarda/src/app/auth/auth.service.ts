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
    let data = {
      email : "maria2@paiva.com",
      password: "123456789",
      codigo:'MTM0OTAyMzk2MjAwNjAzOQ=='
    }
    console.log(data);
    this.http.post<any>(`${environment.apiUrl}/login`,data)
      .subscribe(resp => console.log(resp));
    
  }
}
