
import { BaseEntity } from './base';

export default interface Unidade extends BaseEntity {
  unid: string
  descricao: string
  fracionavel: boolean
  ativo: boolean
}
