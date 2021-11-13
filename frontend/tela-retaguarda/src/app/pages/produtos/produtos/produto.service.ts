import { Produto } from 'src/app/shared/models/entity/produto';
import { Observable } from 'rxjs';
import { TelaResponse } from 'src/app/shared/models/tela-response';
import { TelaApiService } from './../../../core/services/api/tela-api.service';
import { Injectable } from '@angular/core';

import { FormService } from './../../../core/services/form.service';

@Injectable({
  providedIn: 'root'
})
export class ProdutoService {

  private readonly resource = 'produtos'

  constructor(private api: TelaApiService, public fomrService: FormService) {

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

  public save(produto: Produto): Observable<any> {
    return this.api.save(this.resource, produto)
  }


  public delete(_id: number): Observable<TelaResponse> {
    return this.api.delete(this.resource, _id)
  }

}
