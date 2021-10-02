export interface TelaResponse {
    code: number
    data: Array<any>
    success: boolean
}


export interface Unidade {
  id: number
  unid: string
  descricao:string
  fracionalvel:boolean
}
