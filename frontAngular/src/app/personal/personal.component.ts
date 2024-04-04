import { HttpClient, HttpParams  } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { BehaviorSubject } from 'rxjs';


@Component({
  selector: 'app-personal',
  templateUrl: './personal.component.html',
  styleUrls: ['./personal.component.css']
})
export class PersonalComponent implements OnInit{

  StudentArray : any[] = [];
  name: string ="";
  address: string ="";
  fee: Number =0;
  userId!: number;
  currentStudentID = "";
  welcomeMessage: string = "Bienvenido ";
  showMessage: boolean = true;
  token: string = '';
  nombre:string='';
  startDate:string='';
  endDate:string='';



  constructor(private http: HttpClient, private router: Router )
  {
    this.getAllStudent();
    setTimeout(() => {
      this.showMessage = false;
    }, 3000);
  }
  ngOnInit(): void {
    // Obtener el token del almacenamiento local al inicializar el componente
    this.token = localStorage.getItem('token') || '';
    // Puedes hacer cualquier otra lógica con el token aquí
    console.log('Token:',this.token);
    // Realizar la solicitud HTTP GET al backend con el token
    this.http.get(`http://127.0.0.1:8000/decifrar/${this.token}`).subscribe({
      next: (resultData: any) => {
        console.log('Token descifrado:', resultData);
        this.nombre=resultData.nombre;
        console.log("NOMBRE:", this.nombre);
        this.userId=resultData.usuario_id;
        console.log("USER ID:", this.userId);
        // Puedes hacer cualquier otra lógica con el token descifrado aquí
      },
      error: (error: any) => {
        console.error('Error al descifrar el token:', error);
      }
    });
  }
  navegar(){
    this.router.navigate(['/capacidadMq']);
  }

  saveRecords(){
    let bodyData = {
      "name" : this.name,
      "address" : this.address,
      "fee" : this.fee,
      "userId" : this.userId
    }
    this.http.post("http://127.0.0.1:8000/students/",bodyData).subscribe((resultData: any)=>
    {
      console.log(resultData);
      alert("Student Registered Successfully");
      this.getAllStudent();
      this.name = '';
      this.address = '';
      this.fee  = 0;
    });
  };
  getAllStudent(){
    this.http.get("http://127.0.0.1:8000/students/").subscribe((resultData:any)=>{
      //console.log(resultData);
      this.StudentArray = resultData;
    });
  }
  setUpdate(data: any){
    this.name = data.name;
    this.address = data.address;
    this.fee = data.fee;
    this.currentStudentID = data.id;
  }
  UpdateRecords(){
    let bodyData =
    {
      "name" : this.name,
      "address" : this.address,
      "fee" : this.fee,
      //"userId" : this.userId  //comente este dato porque no quiero que se actualize ese campo, en el backen indico que mantenga su valor asi el angular no necesite mandarselo 
    };
    this.http.put("http://127.0.0.1:8000/students/"+ this.currentStudentID+'/' ,
    bodyData).subscribe((resultData: any)=>{
      console.log(resultData);
      alert("Student Registered Updateddd")
      this.name = '';
      this.address = '';
      this.fee  = 0;
      this.getAllStudent();
    })
  }

  setDelete(data: any)
  {
    this.http.delete("http://127.0.0.1:8000/students"+ "/"+ data.id).subscribe((resultData: any)=>
    {
      console.log(resultData);
      alert("Student Deletedddd")
      this.getAllStudent();
    });
  }
  getStudentsByDateRange() {
    // Crea un objeto HttpParams para construir los parámetros de la URL
    let params = new HttpParams();
    params = params.append('start_date', this.startDate);
    params = params.append('end_date', this.endDate);
  
    // Realiza la solicitud HTTP GET con los parámetros de la URL (http://127.0.0.1:8000/students/by-date-range/?start_date=2024-01-02&end_date=2024-01-02)
    this.http.get('http://127.0.0.1:8000/students/by-date-range/', { params: params }).subscribe({
      next: (response: any) => {
        if (response && response.length > 0) {
          // Si hay registros en el rango de fechas, actualiza el array de estudiantes
         this.StudentArray = response;
        } else {
          // Si no hay registros en el rango de fechas, muestra una alerta
          alert("No hay registros en ese rango de fechas");
        }
      },
      error: (error) => {
        console.error('Error al obtener los estudiantes por rango de fecha:', error);
        // Maneja el error si ocurre alguno
      }
    });
  }

}
