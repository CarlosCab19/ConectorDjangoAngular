import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private router: Router) {}

  /*canActivate(): boolean {
    const token = localStorage.getItem('token');
    if (token) {
      // Si el token existe, permite la navegación
      return true;
    } else {
      // Si el token no existe, redirige al componente de login
      this.router.navigate(['/login']);
      return false;
    }
  }*/
  canActivate(): boolean {
    const token = localStorage.getItem('token');
    if (token) {
      const tokenData = JSON.parse(atob(token.split('.')[1])); // Decodificar el token
      //console.log('Decodificado por angular:', tokenData.usuario_id)
      if (tokenData.estatus === true) {
        // Si el estatus es true, permite la navegación
        return true;
      } else {
        // Si el estatus es false, muestra un mensaje de alerta y no permite la navegación
        alert("Usuario desactivado, ponerse en contacto con TI");
        return false;
      }
    } else {
      // Si no hay token, redirige al componente de login
      this.router.navigate(['/login']);
      return false;
    }
  }
}
