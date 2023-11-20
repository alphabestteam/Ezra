import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-my-inner',
  templateUrl: './my-inner.component.html',
  styleUrls: ['./my-inner.component.css'],
})
export class MyInnerComponent {
  @Input() startingNumber: number = 0;
  @Output() addOrSub10: EventEmitter<number> = new EventEmitter();
  addClicked() {
    this.startingNumber += 1;
    this.check10();
  }
  subClicked() {
    this.startingNumber -= 1;
    this.check10();
  }
  check10() {
    if (this.startingNumber === 10 || this.startingNumber === -10) {
      this.addOrSub10.emit(this.startingNumber);
      this.startingNumber = 0;
    }
  }
}
