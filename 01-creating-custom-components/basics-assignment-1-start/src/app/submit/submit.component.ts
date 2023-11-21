import {
  Component,
  EventEmitter,
  Output,
  SimpleChange,
  SimpleChanges,
} from '@angular/core';

@Component({
  selector: 'app-submit',
  templateUrl: './submit.component.html',
  styleUrl: './submit.component.css',
})
export class SubmitComponent {
  @Output() valueOfSubmit: EventEmitter<number> = new EventEmitter();
  options: object[] = [
    { value: 1 },
    { value: 2 },
    { value: 3 },
    { value: 4 },
    { value: 5 },
    { value: 6 },
    { value: 7 },
    { value: 8 },
    { value: 9 },
    { value: 10 },
  ];

  selected: number;

  onSelectedChange(): void {
    this.valueOfSubmit.emit(this.selected);
  }
}
