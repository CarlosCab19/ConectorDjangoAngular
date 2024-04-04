import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  showPassword: boolean = false;
  usuario:string='';
  contrasenia:string='';

  constructor(private http: HttpClient,private router: Router){}

  togglePasswordVisibility() {
    this.showPassword = !this.showPassword;
  }
//este metodo de comprobacion de logueo funciona con las contraseñas hashadas 
  /*logueo(){
    let bodyData ={
      "usuario": this.usuario,
      "contrasenia": this.contrasenia
    }
    this.http.post("http://127.0.0.1:8000/tocken/",bodyData).subscribe((resultData: any)=>{
      console.log(resultData);
    })
    /*this.http.post("http://127.0.0.1:8000/usuarios/validar-credenciales/", bodyData).subscribe({
      next: (resultData: any) => {
        //console.log(resultData);
        alert("Bienvenido");
      },
      error: (error: any) => {
        //console.error(error);
        alert("Credenciales inválidas");
      }
    });
  }*/
  
  logueo() {
    let bodyData ={
      "usuario": this.usuario,
      "contrasenia": this.contrasenia
    }
    this.http.post("http://127.0.0.1:8000/tocken/", bodyData).subscribe({
      next: (resultData: any) => {
        //console.log(resultData.token);
        // Verificar si la respuesta es un token válido
        if (resultData.token) {
          // Guardar el token en el almacenamiento local o de sesión
          localStorage.setItem('token', resultData.token);
          
          // Navegar al componente 'personal'
          this.router.navigate(['/personal']);
        } else {
          // En caso de que el servidor no devuelva un token, mostrar un mensaje de error
          alert("Error: No se recibió un token válido");
        }
      },
      error: (error: any) => {
        //console.error(error);
        // Mostrar un mensaje de alerta en caso de credenciales incorrectas
        alert("Credenciales inválidas");
      }
    });
  }

}
