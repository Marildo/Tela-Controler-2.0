import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { take } from 'rxjs/operators';

import { BaseEntity } from '../../../shared/models/entity/base';
import { TelaResponse } from '../../../shared/models/tela-response';
import { environment } from '../../../../environments/environment';
import { AuthService } from '../../../auth/auth.service';

@Injectable({
  providedIn: 'root'
})
export class TelaApiService {

  // TODO - Tratar erro de API off
  // TODO - Tratar erros retornado pela API

  private readonly API = `${environment.apiUrl}`

  constructor(private http: HttpClient, private authService: AuthService) { }


  private getOptions(body: object | undefined= undefined): object {
    const httpOptions = ({
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${this.authService.token}`
      }),
      body:body
    })
    return httpOptions
  }

  public load(resource:string, page: number = 1, size: number = 30, fieldname:string, like: string | undefined = undefined): Observable<TelaResponse> {
    const _like = like ? `&fieldname=${fieldname}&like=${like}` :''
    let url = `${this.API}/${resource}?&page=${page}&size=${size}${_like ? _like : ''}`

    return this.http.get<any>(url, this.getOptions())
      .pipe(
        take(1), // apenas um chamada
        // delay(5000),
        // map(i => i.data),
        //tap(console.log),
      )
  }

  public save(resource:string, entity: BaseEntity): Observable<TelaResponse> {
    const method = entity.id === 0 ? 'post' : 'put'
    const url = method === 'post' ? resource : `${this.API}/${resource}/${entity.id}`

    return this.http.request<any>(method, url, this.getOptions(entity))
      .pipe(
        take(1), // TODO - tentar uma vez e desincreve
       // map(i => i.data)
      )
  }


  public delete(resource:string, _id: number): Observable<TelaResponse> {
    // TODO - Perguntar antes se realmente que excluir

    const url = `${this.API}/${resource}/${_id}`
    return this.http.delete<TelaResponse>(url, this.getOptions())
      .pipe(
        take(1),
        //map(i => i.data),
      )
  }
}
