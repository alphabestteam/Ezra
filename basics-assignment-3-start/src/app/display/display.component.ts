import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-display',
  templateUrl: './display.component.html',
  styleUrl: './display.component.css',
})
export class DisplayComponent {
  
  @Output() butClicked: EventEmitter <boolean> = new EventEmitter<boolean>()

  messageDisplay: boolean = false;
  buttonClicked() {
    this.messageDisplay = !this.messageDisplay;
    this.butClicked.emit(this.messageDisplay);
  }
}
