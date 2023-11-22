import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { FILMS } from '../star-wars-fake-db/film-data';
import { Film } from '../star-wars-fake-db/interfaces';
import { Subscription } from 'rxjs';
@Component({
  selector: 'app-movie-card-component',
  templateUrl: './movie-card-component.component.html',
  styleUrls: ['./movie-card-component.component.scss'],
})
export class MovieCardComponentComponent implements OnInit {
  movie_id!: number;
  movie!: Film;
  private routeSubscription: Subscription;

  constructor(private route: ActivatedRoute) {
    this.routeSubscription = new Subscription();
  }

  ngOnInit(): void {
    // needed to implement subscription so that the component will rerender when the router was called.
    this.routeSubscription = this.route.params.subscribe((params: Params) => {
      const id: string = params['id'];

      if (id === null) {
        this.movie_id = 1; // if there's no number in the url;
      } else {
        if (+id >= 1 && +id <= 6) {
          this.movie_id = +id;
        } else {
          this.movie_id = 1;
        }
      }

      this.movie = FILMS.find((movies) => movies.episode_id === this.movie_id)!;
    });
  }
}
