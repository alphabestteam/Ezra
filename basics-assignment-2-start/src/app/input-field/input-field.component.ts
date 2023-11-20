import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-input-field',
  templateUrl: './input-field.component.html',
  styleUrl: './input-field.component.css',
})
export class InputFieldComponent {
  @Output() inputText: EventEmitter<string> = new EventEmitter<string>();

  username: string = '';

  inputChange() {
    this.inputText.emit(this.username);
  }

  buttonClicked() {
    this.username = '';
    this.inputChange();
  }
}
