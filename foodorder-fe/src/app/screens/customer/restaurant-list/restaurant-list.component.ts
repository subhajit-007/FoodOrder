import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatLabel, MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatListModule } from '@angular/material/list';
import { MatDividerModule } from '@angular/material/divider';

import { Router, RouterModule } from '@angular/router';
import { CustomerService } from '../../../services/customer/customer.service';


const MatModules = [
  MatToolbarModule,
  MatLabel,
  // MatFormFieldModule,
  // MatInputModule,
  MatButtonModule,
  // MatIconModule,
  MatListModule,
  MatDividerModule,
];

@Component({
  selector: 'app-restaurant-list',
  standalone: true,
  imports: [...MatModules, RouterModule, CommonModule],
  templateUrl: './restaurant-list.component.html',
  styleUrl: './restaurant-list.component.scss'
})
export class RestaurantListComponent implements OnInit {
  restaurantList: any[] = [];

  constructor(private customerService: CustomerService, private router: Router) { }

  ngOnInit(): void {
    this.customerService.getRestaurants().subscribe({
      next: (res) => {
        console.log(res.data);
        this.restaurantList = res.data;
      },
      error: (err) => {
        console.error(err)
      }
    })
  }

  goToRestaurantDetailPage(restaurantId: Number): void {

  }
}
