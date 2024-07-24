import { Injectable } from '@angular/core';
import { AxiosService } from '../network/axios.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RestaurantService {

  constructor(private axiosService: AxiosService) { }

  getRestaurantDetails(restaurantId: any): Observable<any> {
    return new Observable(observer => {
      this.axiosService.get(`/restaurant/${restaurantId}/details`).then(response => {
        observer.next(response.data);
        observer.complete();
      }).catch(error => {
        observer.error(error);
      });
    });
  }

  getMenuListByRestaurantId(restaurantId: any): Observable<any> {
    return new Observable(observer => {
      this.axiosService.get(`/restaurant/${restaurantId}/menus`).then(response => {
        observer.next(response.data);
        observer.complete();
      }).catch(error => {
        observer.error(error);
      });
    });
  }

}
