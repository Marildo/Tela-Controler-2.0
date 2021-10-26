import { Pagination } from "./pagination";

export interface TelaResponse {
  code: number
  data: Array<any>
  pagination: Pagination
  success: boolean
}
