import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

import { ProfesionComponent } from './profesion/profesion.component';
import { PersonaComponent } from './persona/persona.component';

const routes: Routes = [
  {
    path: 'persona',
    component: PersonaComponent,
  },
  {
    path: 'profesion',
    component: ProfesionComponent,
  },
];
@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules }),
  ],
  exports: [RouterModule],
})
export class AppRoutingModule {}
