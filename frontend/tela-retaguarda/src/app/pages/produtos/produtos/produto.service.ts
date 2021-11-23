import { tap } from 'rxjs/operators';
import { Produto } from 'src/app/shared/models/entity/produto';
import { BehaviorSubject, Observable } from 'rxjs';
import { TelaResponse } from 'src/app/shared/models/tela-response';
import { TelaApiService } from './../../../core/services/api/tela-api.service';
import { Injectable, EventEmitter } from '@angular/core';

import { FormService } from './../../../core/services/form.service';
import { UnidadeService } from 'src/app/pages/produtos/unidades/unidade.service';
import { SetorService } from 'src/app/pages/produtos/setores/setor.service';

@Injectable({
  providedIn: 'root'
})
export class ProdutoService {

  private readonly resource = 'produtos'
  onLoaded: EventEmitter<boolean>;

  constructor(
    public fomrService: FormService,
    public unidadeService: UnidadeService,
    public setorService: SetorService,
    private api: TelaApiService)
  {
    this.onLoaded = new EventEmitter<boolean>(true)
  }

  public load(page: number = 1, size: number = 30, like: string | undefined = undefined): Observable<TelaResponse> {
    const fieldname = 'nome'
    this.onLoaded.emit(true)
    console.log('Carregando')
    return this.api.load({
      resource: this.resource,
      page: page,
      size: size,
      fieldname: fieldname,
      like: like
    }).pipe(
      tap(() => {
         this.onLoaded.emit(false)
         console.log('Carregou')
      })
    )
  }

  public loadById(){
    this.onLoaded.emit(false)
    console.log('load by id')
  }

  public save(produto: Produto): Observable<any> {
    return this.api.save(this.resource, produto)
  }


  public delete(_id: number): Observable<TelaResponse> {
    return this.api.delete(this.resource, _id)
  }

}
