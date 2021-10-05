import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Unidade.FormComponent } from './unidade.form.component';

describe('Unidade.FormComponent', () => {
  let component: Unidade.FormComponent;
  let fixture: ComponentFixture<Unidade.FormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Unidade.FormComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(Unidade.FormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
