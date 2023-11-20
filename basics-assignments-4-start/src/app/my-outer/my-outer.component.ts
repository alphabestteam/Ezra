import { Component } from '@angular/core';

@Component({
  selector: 'app-my-outer',
  templateUrl: './my-outer.component.html',
  styleUrls: ['./my-outer.component.css'],
})
export class MyOuterComponent {
  outerStartingNumber: number = 5;
  total: number = 0;
  addOrSub10(num: number) {
    this.total += num;
  }
}
