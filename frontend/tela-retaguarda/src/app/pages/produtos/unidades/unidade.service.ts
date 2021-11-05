import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import Unidade from 'src/app/shared/models/entity/unidade';
import { TelaResponse } from 'src/app/shared/models/tela-response';
import { TelaApiService } from '../../../core/services/api/tela-api.service';



@Injectable({
  providedIn: 'root'
})
export class UnidadeService {

  private readonly resource = 'unidades'

  constructor(private api: TelaApiService) {

  }

  public load(page: number = 1, size: number = 30, like: string | undefined = undefined): Observable<TelaResponse> {
    const fieldname = 'unid'
    return this.api.load({
      resource: this.resource,
      page: page,
      size: size,
      fieldname: fieldname,
      like: like
    })
  }

  public save(unidade: Unidade): Observable<any> {
    return this.api.save(this.resource, unidade)
  }


  public delete(_id: number): Observable<TelaResponse> {
    return this.api.delete(this.resource, _id)
  }


}
