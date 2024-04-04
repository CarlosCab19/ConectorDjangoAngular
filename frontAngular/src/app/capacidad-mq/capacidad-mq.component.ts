import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';


@Component({
  selector: 'app-capacidad-mq',
  templateUrl: './capacidad-mq.component.html',
  styleUrls: ['./capacidad-mq.component.css']
})
export class CapacidadMqComponent implements OnInit{
  token: string = '';
  nombre2:string=''
  nombre:string='';
  usuario:string='';
  contrasenia:string='';
  estatus:boolean=true;
  usuarioID = "";
  arrayUser: any[]=[];
  filtro: string = ''; // Variable para almacenar el valor del filtro

  constructor(private http: HttpClient, private router: Router){
    this.obtenerUser();
  }
  ngOnInit(): void {
    this.token = localStorage.getItem('token') || '';
    this.http.get(`http://127.0.0.1:8000/decifrar/${this.token}`).subscribe({
      next: (resultData: any) => {
        console.log('Token descifrado:', resultData);
        this.nombre2=resultData.nombre;
        // Puedes hacer cualquier otra lógica con el token descifrado aquí
      },
      error: (error: any) => {
        console.error('Error al descifrar el token:', error);
      }
    });
  }
  obtenerUser(){
    this.http.get("http://127.0.0.1:8000/usuarios/").subscribe((resultData:any)=>{
      this.arrayUser = resultData;
    })
  }
  registrar(){
    let bodyData = {
      "nombre":this.nombre,
      "usuario":this.usuario,
      "contrasenia":this.contrasenia,
      "estatus":this.estatus
    }
    this.http.post("http://127.0.0.1:8000/usuarios/",bodyData).subscribe((resultData: any)=>{
      console.log(resultData);
      alert("Usuario registrado");
      this.nombre='';
      this.usuario='';
      this.contrasenia='';
    })
  }
  actualizardata(data:any){
    console.log(data)
    this.nombre = data.nombre,
    this.usuario = data.usuario,
    this.contrasenia = data.contrasenia,
    this.estatus = data.estatus,
    this.usuarioID = data.id
  }
  actualizar(){
    let bodyData = {
      "nombre":this.nombre,
      "usuario":this.usuario,
      "contrasenia":this.contrasenia,
      "estatus":this.estatus
    }
    this.http.put("http://127.0.0.1:8000/usuarios/"+this.usuarioID,bodyData).subscribe((resultData:any)=>{
      console.log(resultData);
      alert("Usuario actualizado")
      this.obtenerUser();
      this.nombre='';
      this.usuario='';
      this.contrasenia='';
    });
  }
  eliminarUser(data:any){
    this.http.delete("http://127.0.0.1:8000/usuarios/"+data.id).subscribe((resultData:any)=>{
      alert("Usuario eliminado")
      this.obtenerUser();
    })
  }
  salir(): void {
    // Eliminar el token del almacenamiento local
    localStorage.removeItem('token');
    console.log('token destruido')
    this.router.navigate(['/login']);
  }
  // Función para filtrar por nombre
  filtrarPorNombre(): any[] {
    return this.arrayUser.filter(item =>
      item.nombre.toLowerCase().includes(this.filtro.toLowerCase()) ||
      item.usuario.toLowerCase().includes(this.filtro.toLowerCase())
    );
  }

}
