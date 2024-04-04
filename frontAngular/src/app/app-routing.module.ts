import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PersonalComponent } from './personal/personal.component';
import { LoginComponent } from './login/login.component';
import { CapacidadMqComponent } from './capacidad-mq/capacidad-mq.component';
import { AuthGuard } from './auth.guard';

const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'personal', component: PersonalComponent, canActivate: [AuthGuard] },
  { path: 'login', component: LoginComponent },
  { path: 'capacidadMq', component: CapacidadMqComponent, canActivate: [AuthGuard] },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
