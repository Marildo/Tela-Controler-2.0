import { Route } from '@angular/router/router';
import { ClientesListComponent } from "src/app/pages/clientes/clientes-list/clientes-list.component";
import { ClientesComponent } from "src/app/pages/clientes/clientes.component";

export const clientesRoute: Route = {
   path: 'clientes',
   component: ClientesComponent,
   children: [
     {
       path: '',
       component: ClientesListComponent
     }
   ]
}
