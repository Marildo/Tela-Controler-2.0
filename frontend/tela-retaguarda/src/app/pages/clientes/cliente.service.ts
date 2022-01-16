import { tap } from 'rxjs/operators';
import { Injectable, EventEmitter } from '@angular/core';
import { Observable } from 'rxjs';
import { TelaApiService } from './../../core/services/api/tela-api.service';
import { FormService } from './../../core/services/form.service';
import { TelaResponse } from './../../shared/models/tela-response';

@Injectable({
  providedIn: 'root'
})
export class ClienteService {

  private readonly resource = 'participantes'
  public onLoaded: EventEmitter<boolean>;

  constructor(private api: TelaApiService,public formService: FormService) {
    this.onLoaded = new EventEmitter<boolean>(true)
  }

  public load(page: number = 1, size: number = 30, like: string | undefined = undefined): Observable<TelaResponse> {
    const fieldname = 'fantasia'
    this.onLoaded.emit(true)
    return this.api.load({
      resource: this.resource,
      page: page,
      size: size,
      fieldname: fieldname,
      like: like
    }).pipe(
      tap(() => {
         this.onLoaded.emit(false)
      })
    )
  }
}
