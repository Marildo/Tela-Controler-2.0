export interface Permission {
    id:number
    recurso:string
    auth:number
}

export class User {
    constructor(
        public id?:number,
        public nome?:string, 
        public email?: string, 
        public permissoes?: Array<Permission>) {
    }


    public hasReadPermition(resource:string): boolean{
        console.log(this.permissoes)
        return false
    }
}

