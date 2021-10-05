import { NgModule } from '@angular/core'
//import { MatSliderModule } from '@angular/material/slider'
//import { MatToolbarModule } from '@angular/material/toolbar'
import { MatIconModule } from '@angular/material/icon'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatButtonModule } from '@angular/material/button'
import { MatBadgeModule } from '@angular/material/badge'
import { MatTableModule } from '@angular/material/table'
import { MatDialogModule } from '@angular/material/dialog'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatCardModule } from '@angular/material/card'
import { MatCheckboxModule } from '@angular/material/checkbox'
import {MatDividerModule} from '@angular/material/divider'




@NgModule({
  exports: [
    // MatSliderModule,
    MatIconModule,
    MatFormFieldModule,
    MatCheckboxModule,
    MatInputModule,
    // MatToolbarModule,
    MatButtonModule,
    MatBadgeModule,
    MatTableModule,
    MatProgressSpinnerModule,
    MatDialogModule,
    MatCardModule,
    MatDividerModule
  ]
})
export class AppMaterialModule { }
