import { Route } from '@angular/router';

export const RESTAURANT_ROUTE: Route[] = [
    { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
    {
        path: 'dashboard',
        loadComponent: () =>
            import('./dashboard/dashboard.component').then(
                (comp) => comp.DashboardComponent
            ),
    },
    {
        path: ':restaurantId/details',
        loadComponent: () =>
            import('./restaurant-detail/restaurant-detail.component').then(
                (comp) => comp.RestaurantDetailComponent
            ),
    },
];
