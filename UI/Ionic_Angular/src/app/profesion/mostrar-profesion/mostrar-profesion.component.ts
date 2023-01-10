import { Component, OnInit, ViewChild } from '@angular/core';
import { CompartidoService } from 'src/app/services/compartido.service';

@Component({
  selector: 'app-mostrar-profesion',
  templateUrl: './mostrar-profesion.component.html',
  styleUrls: ['./mostrar-profesion.component.scss'],
})
export class MostrarProfesionComponent implements OnInit {
  isModalOpen = false;
  
  constructor(private service: CompartidoService) {}

  title: String ="";
  ProfesionLista: any = [];
  ActivarCrearActualizarProfesionComp: boolean = false;
  pro: any;

  ngOnInit() {
    this.refrescarProfesionLista();
  }

  refrescarProfesionLista() {
    this.service.getProfesionLista().subscribe((data) => {
      this.ProfesionLista = data;
    });
  }

  setOpenCreate(isOpen: boolean) {
    this.isModalOpen = isOpen;
    this.title="Crear Profesión";
    this.ActivarCrearActualizarProfesionComp=true;
    this.refrescarProfesionLista();
  }

  setOpenEdit(isOpen: boolean, item: any) {
    this.pro=item;
    this.isModalOpen = isOpen;
    this.title="Editar Profesión";
    this.ActivarCrearActualizarProfesionComp=true;
    this.refrescarProfesionLista();
  }

}
