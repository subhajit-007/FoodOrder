import { Routes } from '@angular/router';
import { PageNotFoundComponent } from './screens/shared/page-not-found/page-not-found.component';
import { CustomerComponent } from './screens/customer/customer.component';
import { RestaurantComponent } from './screens/restaurant/restaurant.component';

export const routes: Routes = [
    {
        path: '',
        component: CustomerComponent,
        loadChildren: () =>
            import('./screens/customer/customer.route').then((m) => m.CUSTOMER_ROUTE),
    },
    {
        path: 'restaurant',
        component: RestaurantComponent,
        loadChildren: () =>
            import('./screens/restaurant/restaurant.route').then(
                (m) => m.RESTAURANT_ROUTE
            ),
    },
    { path: '**', component: PageNotFoundComponent }, // This should be the last route
];
