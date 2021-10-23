import { take } from 'rxjs/operators';
import { AuthService } from './../../../auth/auth.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from './../../../../environments/environment';
import { Injectable } from '@angular/core';
import { TelaResponse } from '../../core/model/tela-response';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TelaApiService {

  private readonly API = `${environment.apiUrl}unidades`


  constructor(private http: HttpClient, private authService: AuthService) { }


  private getHeaders(): Object{
    const httpOptions = ({
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${this.authService.token}`
      })
    })

    return httpOptions
  }

  public load(page: number = 1, size: number = 30, text: String | undefined = undefined): Observable<TelaResponse> {

    const fieldname= 'unid'
    const like = text ? `&fieldname=${fieldname}&like=${text}` :''
    let url = `${this.API}?&page=${page}&size=${size}${like ? like : ''}`
    console.log(url)
    return this.http.get<any>(url, this.getHeaders())
      .pipe(
        take(1),
        // delay(5000),
        // map(i => i.data),
        //tap(console.log),
      )
  }
}
