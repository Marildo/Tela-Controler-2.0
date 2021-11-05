import { Setor } from 'src/app/shared/models/entity/setor';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { TelaApiService } from './../../../core/services/api/tela-api.service';
import { TelaResponse } from './../../../shared/models/tela-response';

@Injectable({
  providedIn: 'root'
})
export class SetorService {


  private readonly resource = 'setores'

  constructor(private api: TelaApiService) {

  }

  public load(page: number = 1, size: number = 30, like: string | undefined = undefined): Observable<TelaResponse> {
    const fieldname = 'nome'
    return this.api.load({
      resource: this.resource,
      page: page,
      size: size,
      fieldname: fieldname,
      like: like
    })
  }

  public save(setor: Setor): Observable<any> {
    return this.api.save(this.resource, setor)
  }


  public delete(_id: number): Observable<TelaResponse> {
    return this.api.delete(this.resource, _id)
  }
}
