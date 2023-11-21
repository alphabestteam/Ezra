import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { WarningAlertComponent } from './warning-alert/warning-alert.component';
import { SuccessAlertComponent } from './success-alert/success-alert.component';
import { DisplayButtonComponent } from './display-button/display-button.component';
import { SubmitComponent } from './submit/submit.component';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import {MatSelectModule} from '@angular/material/select';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent,
    WarningAlertComponent,
    SuccessAlertComponent,
    DisplayButtonComponent,
    SubmitComponent,
  ],
  imports: [BrowserAnimationsModule, BrowserModule, FormsModule, MatFormFieldModule, MatInputModule, MatSelectModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
