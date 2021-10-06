import { NgModule } from '@angular/core';
import { MatBadgeModule } from '@angular/material/badge';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatDialogModule } from '@angular/material/dialog';
import { MatDividerModule } from '@angular/material/divider';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatTableModule } from '@angular/material/table';

//import { MatSliderModule } from '@angular/material/slider'
//import { MatToolbarModule } from '@angular/material/toolbar'



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
    MatDividerModule,
    MatSnackBarModule
  ]
})
export class AppMaterialModule { }
