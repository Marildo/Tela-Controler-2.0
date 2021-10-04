import { Observable } from 'rxjs';
import { AuthService } from './../auth/auth.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';


import { environment } from './../../environments/environment';
import { Unidade } from './model';
import { map, tap, delay } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UnidadeService {

  private readonly API = `${environment.apiUrl}/unidades`

  constructor(private http: HttpClient, private authService: AuthService) {

  }

  // TODO - Centralizar chamada da api em um unico serviço

  public load():Observable<Array<Unidade>>{
    const httpOptions = ({
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
        'Authorization': `Bearer ${this.authService.token}`
      })
    })
    return this.http.get<Array<Unidade>>(this.API, httpOptions)
    .pipe(
      tap(console.log),
      delay(1000),
      map(i => i.data),
      tap(console.log),
    )
  }
}
