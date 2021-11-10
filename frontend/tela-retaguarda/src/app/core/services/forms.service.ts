import { FormControl, FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Injectable } from '@angular/core';

interface Lenght {
  max?: number
  min?: number

}

interface Properties {
  required: boolean
  length?: Lenght
}


@Injectable({
  providedIn: 'root'
})
export class FormsService {

  data: any = {
    "produtos": {
      "ativo": {
        "required": false
      },
      "cod_barras": {
        "length": {
          "max": 14,
          "min": null
        },
        "required": true
      },
      "codigo": {
        "length": {
          "max": 30,
          "min": 1
        },
        "required": true
      },
      "estoque_minimo": {
        "range": {
          "max": null,
          "min": 0
        },
        "required": false
      },
      "id": {
        "required": false
      },
      "nome": {
        "length": {
          "max": 250,
          "min": 5
        },
        "required": true
      },
      "observacao": {
        "length": {
          "max": 250,
          "min": null
        },
        "required": true
      },
      "outros": {
        "range": {
          "max": null,
          "min": 0
        },
        "required": false
      },
      "pr_custo": {
        "range": {
          "max": null,
          "min": 0
        },
        "required": false
      },
      "pr_venda_prazo": {
        "range": {
          "max": null,
          "min": 0.01
        },
        "required": false
      },
      "pr_venda_vista": {
        "range": {
          "max": null,
          "min": 0.01
        },
        "required": false
      },
      "qtd_embalagem": {
        "required": false
      },
      "referencia": {
        "length": {
          "max": 14,
          "min": null
        },
        "required": true
      },
      "setor_id": {
        "required": true
      },
      "unidade": {
        "length": {
          "max": 4,
          "min": 2
        },
        "required": true
      }
    },
    "setores": {
      "ativo": {
        "required": false
      },
      "id": {
        "required": false
      },
      "nome": {
        "length": {
          "max": 30,
          "min": 1
        },
        "required": true
      }
    },
    "unidades": {
      "ativo": {
        "required": false
      },
      "descricao": {
        "length": {
          "max": 30,
          "min": 1
        },
        "required": false
      },
      "fracionavel": {
        "required": false
      },
      "id": {
        "required": false
      },
      "unid": {
        "length": {
          "max": 4,
          "min": 2
        },
        "required": true
      }
    }
  }


  constructor(private formBuilder: FormBuilder) { }

  buildForm(resource: string): FormGroup {
    const form = this.formBuilder.group({})
    this.addControls(resource, form)
    return form
  }


  addControls(resource: string, form: FormGroup): void {
    const item = this.data[resource]
    Object.keys(item).forEach((key: string) => {
      this.addItemForm(form, key, item[key])
    })
  }

  private addItemForm(form: FormGroup, name: string, properties: Properties): void {
    const validators = []

    if (properties.required) {
      validators.push(Validators.required)
    }

    if (properties.length?.max) {
      validators.push(Validators.maxLength(properties.length.max))
    }

    if (properties.length?.min) {
      validators.push(Validators.minLength(properties.length.min))
    }

    form.addControl(name,
      this.formBuilder.control('', validators)
    )
  }
}
