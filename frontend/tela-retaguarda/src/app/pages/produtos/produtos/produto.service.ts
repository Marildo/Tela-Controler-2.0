import { Injectable } from '@angular/core';

import { FormService } from './../../../core/services/form.service';

@Injectable({
  providedIn: 'root'
})
export class ProdutoService {

  constructor(public  fomrService: FormService) { }
}
