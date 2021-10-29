import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { take } from 'rxjs/operators';

import { BaseEntity } from '../../../shared/models/entity/base';
import { TelaResponse } from '../../../shared/models/tela-response';
import { environment } from '../../../../environments/environment';
import { AuthService } from '../../../auth/auth.service';

interface HttpOptions {
  headers: HttpHeaders
  params?: HttpParams
  body?: any
}

@Injectable({
  providedIn: 'root'
})
export class TelaApiService {


  // TODO - Tratar erro de API off
  // TODO - Tratar erros retornado pela API
  // TODO - Scrol infinito ao invez de paginacao

  private readonly API = `${environment.apiUrl}`

  constructor(private http: HttpClient, private authService: AuthService) { }

  public load(resource: string, page: number = 1, size: number = 30, fieldname: string, like: string = ''): Observable<TelaResponse> {
    let params = new HttpParams()
      .append('page', page)
      .append('size', size)

    if (fieldname != '')
      params = params.set('fieldname', fieldname)

    if (like != '')
      params = params.set('like', like)

    const options = this.getOptions()
    options.params = params

    let url = `${this.API}${resource}`
    return this.http.get<any>(url, options)
      .pipe(
        take(1), // apenas um chamada
        // delay(5000),
        // map(i => i.data),
        //tap(console.log),
      )
  }

  public save(resource: string, entity: BaseEntity): Observable<TelaResponse> {
    const method = entity.id === 0 ? 'post' : 'put'
    const url = method === 'post' ? resource : `${this.API}/${resource}/${entity.id}`

    const options = this.getOptions()
    options.body = entity
    return this.http.request<any>(method, url, options)
      .pipe(
        take(1), // TODO - tentar uma vez e desincreve
        // map(i => i.data)
      )
  }


  public delete(resource: string, _id: number): Observable<TelaResponse> {
    const url = `${this.API}/${resource}/${_id}`
    return this.http.delete<TelaResponse>(url, this.getOptions())
      .pipe(
        take(1),
        //map(i => i.data),
      )
  }

  private getOptions(): HttpOptions {
    return ({
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${this.authService.token}`
      }),
    })
  }

}
