export interface TelaResponse {
    code: number
    data: Array<any>
    success: boolean
}


export interface Unidade {
  id: number
  unid: string
  descricao:string
  fracionavel:boolean
  ativo:boolean
}
