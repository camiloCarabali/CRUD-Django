import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { CrearActualizarProfesionComponent } from './crear-actualizar-profesion.component';

describe('CrearActualizarProfesionComponent', () => {
  let component: CrearActualizarProfesionComponent;
  let fixture: ComponentFixture<CrearActualizarProfesionComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ CrearActualizarProfesionComponent ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(CrearActualizarProfesionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
