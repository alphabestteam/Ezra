import { Component } from '@angular/core';

@Component({
  selector: 'app-display-button',
  templateUrl: './display-button.component.html',
  styleUrl: './display-button.component.css',
})
export class DisplayButtonComponent {
  message: string = 'Click me!';
  success: boolean = true;
  changeText(): void {
    this.success = !this.success;
    if (this.success === true) {
      this.message = 'Warning!';
    } else {
      this.message = 'Success!';
    }
  }
}
