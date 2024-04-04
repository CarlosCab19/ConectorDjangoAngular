import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CapacidadMqComponent } from './capacidad-mq.component';

describe('CapacidadMqComponent', () => {
  let component: CapacidadMqComponent;
  let fixture: ComponentFixture<CapacidadMqComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CapacidadMqComponent]
    });
    fixture = TestBed.createComponent(CapacidadMqComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
