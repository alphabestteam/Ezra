import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MovieCardComponentComponent } from './movie-card-component/movie-card-component.component';

const routes: Routes = [
  { path: 'star-wars-movies/:id', component: MovieCardComponentComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
