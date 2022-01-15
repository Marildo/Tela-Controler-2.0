import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { TelaApiService } from './../../core/services/api/tela-api.service';
import { FormService } from './../../core/services/form.service';
import { TelaResponse } from './../../shared/models/tela-response';

@Injectable({
  providedIn: 'root'
})
export class ClienteService {

  private readonly resource = 'participantes'

  constructor(private api: TelaApiService,public formService: FormService) {

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
}
