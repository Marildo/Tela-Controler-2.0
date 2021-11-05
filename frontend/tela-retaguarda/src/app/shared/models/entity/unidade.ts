
import { BaseEntity } from './base';

export  interface Unidade extends BaseEntity {
  unid: string
  descricao: string
  fracionavel: boolean
  ativo: boolean
}
