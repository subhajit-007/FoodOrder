import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEditRestaurantDetailsComponent } from './add-edit-restaurant-details.component';

describe('AddEditRestaurantDetailsComponent', () => {
  let component: AddEditRestaurantDetailsComponent;
  let fixture: ComponentFixture<AddEditRestaurantDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AddEditRestaurantDetailsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddEditRestaurantDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
