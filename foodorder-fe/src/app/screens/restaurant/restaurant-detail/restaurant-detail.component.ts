import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { RestaurantService } from '../../../services/restaurant/restaurant.service';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { MatDividerModule } from '@angular/material/divider';
import { MatLabel } from '@angular/material/form-field';
import { MatListModule } from '@angular/material/list';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatCardModule } from '@angular/material/card';


const MatModules = [
  MatToolbarModule,
  MatLabel,
  // MatFormFieldModule,
  // MatInputModule,
  MatButtonModule,
  // MatIconModule,
  MatListModule,
  MatDividerModule,
  MatCardModule,
];

@Component({
  selector: 'app-restaurant-detail',
  standalone: true,
  imports: [...MatModules, RouterModule, CommonModule],
  templateUrl: './restaurant-detail.component.html',
  styleUrl: './restaurant-detail.component.scss'
})
export class RestaurantDetailComponent implements OnInit {
  restaurant: any;
  menuList: any[] = [];
  restaurantId: string = ""

  constructor(private route: ActivatedRoute, private restaurantService: RestaurantService) { }

  ngOnInit(): void {
    this.restaurantId = this.route.snapshot.paramMap.get('restaurantId') ?? '';
    console.log(Number(this.restaurantId))
    this.getRestaurantInfo()
    this.getRestaurantMenu()
  }

  getRestaurantInfo(): void {
    this.restaurantService.getRestaurantDetails(this.restaurantId).subscribe({
      next: (res) => {
        this.restaurant = res.data
        console.log(this.restaurant)
      },
      error: (err) => {
        console.error(err)
      }
    })
  }

  getRestaurantMenu(): void {
    this.restaurantService.getMenuListByRestaurantId(this.restaurantId).subscribe({
      next: (res) => {
        this.menuList = res.data
        console.log(this.menuList)
      },
      error: (err) => {
        console.error(err)
      }
    })
  }

}
