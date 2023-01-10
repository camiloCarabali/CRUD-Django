import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';

import { IonicModule, IonicRouteStrategy } from '@ionic/angular';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { ProfesionComponent } from './profesion/profesion.component';
import { MostrarProfesionComponent } from './profesion/mostrar-profesion/mostrar-profesion.component';
import { CrearActualizarProfesionComponent } from './profesion/crear-actualizar-profesion/crear-actualizar-profesion.component';

import { PersonaComponent } from './persona/persona.component';
import { MostrarPersonaComponent } from './persona/mostrar-persona/mostrar-persona.component';
import { CrearActualizarPersonaComponent } from './persona/crear-actualizar-persona/crear-actualizar-persona.component';

import { CompartidoService } from './services/compartido.service';

import { HttpClientModule } from '@angular/common/http';

import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    ProfesionComponent,
    MostrarProfesionComponent,
    CrearActualizarProfesionComponent,
    PersonaComponent,
    MostrarPersonaComponent,
    CrearActualizarPersonaComponent,
  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(),
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [
    { provide: RouteReuseStrategy, useClass: IonicRouteStrategy },
    CompartidoService,
  ],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class AppModule {}
