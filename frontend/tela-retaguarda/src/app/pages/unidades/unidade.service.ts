import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthService } from 'src/app/auth/auth.service';
import Unidade from 'src/app/shared/models/entity/unidade';
import { TelaResponse } from 'src/app/shared/models/tela-response';
import { TelaApiService } from '../../core/services/api/tela-api.service';



@Injectable({
  providedIn: 'root'
})
export class UnidadeService {

  private readonly resource = 'unidades'

  constructor(private api:TelaApiService,  private http: HttpClient, private authService: AuthService) {

  }

  public load(page: number = 1, size: number = 30, like: string | undefined = undefined): Observable<TelaResponse> {
    const fieldname= 'unid'
    return this.api.load(this.resource,page, size,fieldname, like)
  }

  public save(unidade: Unidade): Observable<any> {
      return this.api.save(this.resource, unidade)
  }


  public delete(_id: number): Observable<TelaResponse> {
      return this.api.delete(this.resource,_id)
  }


}
