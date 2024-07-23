import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AxiosService } from '../network/axios.service';

@Injectable({
  providedIn: 'root'
})
export class CustomerService {

  constructor(private axiosService: AxiosService) { }

  getRestaurants(): Observable<any> {
    return new Observable(observer => {
      this.axiosService.get('/restaurant/list/').then(response => {
        observer.next(response.data);
        observer.complete();
      }).catch(error => {
        observer.error(error);
      });
    });
  }
}
