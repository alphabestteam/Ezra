import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  messageDisplay: boolean;
  count: number = 0;
  countArr: number[] = [];
  buttonClicked(messageDisplay: boolean) {
    console.log(this.count);
    console.log(this.countArr);
    
    
    this.messageDisplay = messageDisplay;
    this.count += 1;
    this.countArr.push(this.count);
  }
}
