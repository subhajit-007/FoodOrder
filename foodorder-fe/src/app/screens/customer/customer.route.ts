import { Route } from '@angular/router';

export const CUSTOMER_ROUTE: Route[] = [
  { path: '', redirectTo: 'restaurant-list', pathMatch: 'full' },
  {
    path: 'restaurant-list',
    loadComponent: () =>
      import('./restaurant-list/restaurant-list.component').then(
        (comp) => comp.RestaurantListComponent
      ),
  },
];
