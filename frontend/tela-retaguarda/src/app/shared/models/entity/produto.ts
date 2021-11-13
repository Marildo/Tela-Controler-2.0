import { Setor } from 'src/app/shared/models/entity/setor';
import { Unidade } from 'src/app/shared/models/entity/unidade';
import { BaseEntity } from './base';

export  interface Produto extends BaseEntity {
  codigo?:string
  nome?:string
  cod_barras:number
  referencia?:string
  observacao?:string

  pr_venda_vista?:number
  pr_venda_prazo?:number

  estoque?:number
  estoque_minimo?:number
  pr_custo?:number
  outros?:number

  qtd_embalagem:number

  unidade?:Unidade
  setor?:Setor

  ultima_compra?:Date
  ultima_venda?:Date
  ativo?:boolean
}
