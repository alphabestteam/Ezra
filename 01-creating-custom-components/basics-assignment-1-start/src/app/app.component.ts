import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  success: boolean;
  amount: string;
  receiveMessage(message: boolean) {
    this.success = message;
  }

  getAmount(amount: string) {
    this.amount = amount;
  }

  getArrayOfLength(amount: string) {
    return new Array(amount);
  }
}
