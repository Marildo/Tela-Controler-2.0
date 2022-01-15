import { BaseEntity } from './base';

export  interface Cliente extends BaseEntity {
  nome: string
  cpf: string
  cnpj: string
  fantasia: string
  ativo: boolean

  getDocument(): String
}
