import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { AxiosService } from '../network/axios.service';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = environment.apiUrl;
  private tokenKey = 'Authorization';
  private loggedIn = new BehaviorSubject<boolean>(false);

  constructor(private http: HttpClient, private axiosService: AxiosService) { }


  signup(userDataPayload: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/signup/`, userDataPayload);
  }

  login(credentials: any): Observable<any> {
    return new Observable(observer => {
      this.axiosService.post('/auth/login/', credentials).then(response => {
        localStorage.setItem('Authorization', `Token ${response.data?.token}`);
        this.loggedIn.next(true);
        observer.next(response.data);
        observer.complete();
      }).catch(error => {
        observer.error(error);
      });
    });
  }

  logout(): Observable<any> {
    return new Observable(observer => {
      this.axiosService.post('/auth/logout/', {}).then(response => {
        localStorage.removeItem('Authorization');
        this.loggedIn.next(false);
        observer.next(response.data);
        observer.complete();
      }).catch(error => {
        observer.error(error);
      });
    });
  }

  isLoggedIn(): Observable<boolean> {
    // return this.checkTokenValidity(token);
    const token = this.getToken();
    if (token) {
      this.loggedIn.next(true);
    }
    return this.loggedIn.asObservable();
  }

  getToken(): string | null {
    return localStorage.getItem(this.tokenKey);
  }

  private checkTokenValidity(token: string): Promise<any> {
    return this.axiosService.get(`/token-verify/`)
  }
}
