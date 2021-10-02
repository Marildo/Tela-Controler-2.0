import { Observable } from 'rxjs';
import { AuthService } from './../auth/auth.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';


import { environment } from './../../environments/environment';
import { TelaResponse } from './model';

@Injectable({
  providedIn: 'root'
})
export class UnidadeService {

  private readonly API = `${environment.apiUrl}/unidades`

  constructor(private http: HttpClient, private authService: AuthService) {

  }

  // TODO - Centralizar chamada da api em um unico serviço

  public load():Observable<TelaResponse>{
    const httpOptions = ({
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
        'Authorization': `Bearer ${this.authService.token}`
      })
    })
    return this.http.get<TelaResponse>(this.API, httpOptions)
  }
}
