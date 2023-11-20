import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';


import { AppComponent } from './app.component';
import { DisplayComponent } from './display/display.component';
import { TextComponent } from './text/text.component';

@NgModule({
  declarations: [
    AppComponent,
    DisplayComponent,
    TextComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
