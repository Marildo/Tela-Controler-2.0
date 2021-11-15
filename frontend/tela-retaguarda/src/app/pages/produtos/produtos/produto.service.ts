import { tap } from 'rxjs/operators';
import { Produto } from 'src/app/shared/models/entity/produto';
import { BehaviorSubject, Observable } from 'rxjs';
import { TelaResponse } from 'src/app/shared/models/tela-response';
import { TelaApiService } from './../../../core/services/api/tela-api.service';
import { Injectable, EventEmitter } from '@angular/core';

import { FormService } from './../../../core/services/form.service';

@Injectable({
  providedIn: 'root'
})
export class ProdutoService {

  private readonly resource = 'produtos'
  onLoaded: BehaviorSubject<boolean>;

  constructor(private api: TelaApiService, public fomrService: FormService) {
    console.log('contrutor de produtosService')
    this.onLoaded = new BehaviorSubject<boolean>(true)
  }

  public load(page: number = 1, size: number = 30, like: string | undefined = undefined): Observable<TelaResponse> {
    const fieldname = 'nome'
    this.onLoaded.next(true)
    return this.api.load({
      resource: this.resource,
      page: page,
      size: size,
      fieldname: fieldname,
      like: like
    }).pipe(
      tap(() => {
         this.onLoaded.next(false)
      })
    )
  }

  public save(produto: Produto): Observable<any> {
    return this.api.save(this.resource, produto)
  }


  public delete(_id: number): Observable<TelaResponse> {
    return this.api.delete(this.resource, _id)
  }

}
