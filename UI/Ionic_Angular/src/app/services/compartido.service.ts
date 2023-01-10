import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class CompartidoService {
  readonly APIUrl = 'http://127.0.0.1:8000/';

  constructor(private http: HttpClient) {}

  getProfesionLista(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + '/mostrarProfesion/');
  }

  crearProfesion(val: any) {
    return this.http.post(this.APIUrl + '/crearProfesion/', val);
  }

  actualizarProfesion(val: any) {
    return this.http.post(this.APIUrl + '/actualizarProfesion/', val);
  }

  eliminarProfesion(val: any) {
    return this.http.delete(this.APIUrl + '/eliminarProfesion/' + val);  
  }

  /*<------------------PERSONAS-------------------->*/

  getPersonaLista(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + '/mostrarPersona/');
  }

  crearPersona(val: any) {
    return this.http.post(this.APIUrl + '/crearPersona/', val);
  }

  actualizarPersona(val: any) {
    return this.http.post(this.APIUrl + '/actualizarPersona/', val);
  }

  eliminarPersona(val: any) {
    return this.http.delete(this.APIUrl + '/eliminarPersona/' + val);
  }

/*
  getAllProfesionNames():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+ '/mostrarProfesion/')
  }
*/
}
