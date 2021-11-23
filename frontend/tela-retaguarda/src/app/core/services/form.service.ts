import { Injectable } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

interface Lenght {
  max?: number
  min?: number

}

interface Properties {
  required: boolean
  length?: Lenght
  default: string | number
}


@Injectable({
  providedIn: 'root'
})
export class FormService {

  data: any ={
    "produtos": {
      "ativo": {
        "default": true,
        "required": false
      },
      "cod_barras": {
        "length": {
          "max": 14,
          "min": null
        },
        "required": false
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
        "required": false,
        "default": 0.01,
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
        "required": false
      },
      "outros": {
        "default": 0.01,
        "range": {
          "max": null,
          "min": 0
        },
        "required": false
      },
      "pr_custo": {
        "default": 0.01,
        "range": {
          "max": null,
          "min": 0
        },
        "required": false
      },
      "estoque": {
        "default": 0.01,
        "range": {
          "max": null,
          "min": 0
        },
        "required": false
      },
      "pr_venda_prazo": {
        "default": 0.01,
        "range": {
          "max": null,
          "min": 0.01
        },
        "required": false
      },
      "pr_venda_vista": {
        "default": 0.01,
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
        "required": false
      },
      "setor": {
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
        },
        "required": true
      },
      "unidade": {
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
        "required": true,
        "unid": {
          "length": {
            "max": 4,
            "min": 2
          },
          "required": true
        }
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
    let default_value:any = ''

    if (properties.required) {
      validators.push(Validators.required)
    }

    if (properties.length?.max) {
      validators.push(Validators.maxLength(properties.length.max))
    }

    if (properties.length?.min) {
      validators.push(Validators.minLength(properties.length.min))
    }

    if (properties.default)
      default_value = properties.default

    form.addControl(name,
      this.formBuilder.control(default_value, validators)
    )
  }
}
