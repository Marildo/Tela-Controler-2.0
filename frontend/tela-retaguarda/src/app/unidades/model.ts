export interface TelaResponse {
  code: number
  data: Array<any>
  pagination: Pagination
  success: boolean
}

export class Pagination {

  public constructor(
    public page: number = 0,
    public size: number = 0,
    public total: number = 0,
    public total_pages: number = 0) {
  }

  public isFirstPage(): boolean {
    return this.page === 1
  }
}

export interface Unidade {
  id: number
  unid: string
  descricao: string
  fracionavel: boolean
  ativo: boolean
}
