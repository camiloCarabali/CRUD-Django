import { Component, Input, OnInit } from '@angular/core';
import { CompartidoService } from 'src/app/services/compartido.service';

@Component({
  selector: 'app-crear-actualizar-profesion',
  templateUrl: './crear-actualizar-profesion.component.html',
  styleUrls: ['./crear-actualizar-profesion.component.scss'],
})
export class CrearActualizarProfesionComponent implements OnInit {
  constructor(private service: CompartidoService) {}

  @Input() pro: any;
  Id: String = '';
  Nombre: String = '';

  ngOnInit() {
    this.Id = this.pro.Id;
    this.Nombre = this.pro.Nombre;
  }

  crearProfesion(){
    var val = {Id: this.Id, Nombre: this.Nombre};
    this.service.crearProfesion(val).subscribe(res=>{
      alert(res.toString());
    })
  }

  actualizarProfesion(){
    var val = {Id: this.Id, Nombre: this.Nombre};
    this.service.actualizarProfesion(val).subscribe(res=>{
      alert(res.toString());
    });
  }

  
}
