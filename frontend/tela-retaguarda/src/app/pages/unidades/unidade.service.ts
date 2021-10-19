import { Observable } from 'rxjs';
import { AuthService } from 'src/app/auth/auth.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';


import { environment } from 'src/environments/environment';
import { Unidade, TelaResponse } from './model';
import { map, tap, delay, take } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UnidadeService {



  private readonly API = `${environment.apiUrl}unidades`

  constructor(private http: HttpClient, private authService: AuthService) {

  }

  // TODO - Centralizar chamada da api em um unico serviço
  // TODO - Tratar erro de API off
  public load(page: number = 1, size: number = 30, text: String | undefined = undefined): Observable<TelaResponse> {
    const httpOptions = ({
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${this.authService.token}`
      })
    })
    const fieldname= 'unid'
    const like = text ? `&fieldname=${fieldname}&like=${text}` :''
    let url = `${this.API}?&page=${page}&size=${size}${like ? like : ''}`
    console.log(url)
    return this.http.get<any>(url, httpOptions)
      .pipe(
        take(1),
        // delay(5000),
        // map(i => i.data),
        //tap(console.log),
      )
  }

  public save(unidade: Unidade): Observable<any> {
    const httpOptions = ({
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${this.authService.token}`
      }),
      body: unidade
    })

    const method = unidade.id === 0 ? 'post' : 'put'
    const url = unidade.id === 0 ? this.API : `${this.API}/${unidade.id}`

    return this.http.request<any>(method, url, httpOptions)
      .pipe(
        take(1), // TODO - tentar uma vez e desincreve
        delay(1000),
        map(i => i.data)
      )
  }

  public delete(_id: number): Observable<TelaResponse> {
    // TODO - Perguntar antes se realmente que excluir
    const httpOptions = ({
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${this.authService.token}`
      })
    })
    const url = `${this.API}/${_id}`
    return this.http.delete<any>(url, httpOptions)
      .pipe(
        take(1),
        map(i => i.data),
      )
  }

  public findByText(text: string): Observable<TelaResponse> {
    const httpOptions = ({
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${this.authService.token}`
      })
    })
    const url = `${this.API}/search?text=${text}`
    return this.http.get<any>(url, httpOptions)
      .pipe(
        take(1)
      )
  }
}
