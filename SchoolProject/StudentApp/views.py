from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from StudentApp.serializers import StudentSerializer
from StudentApp.models import Student
from django.http import HttpResponseNotAllowed, HttpResponseNotFound
from datetime import datetime, timedelta

@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def student_detail(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponseNotFound("Student not found")

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        data['userId'] = student.userId  # Mantener el valor actual de 'userId'
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({"message": "Student deleted successfully"}, status=204)

@csrf_exempt
def students_by_edad(request, edad):  # Cambiar el nombre de la función y el parámetro
    if request.method == 'GET':
        students = Student.objects.filter(fee=edad)  # Cambiar el nombre del campo de filtro
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponseNotAllowed(['GET'])

def method_not_allowed(request, *args, **kwargs):
    return HttpResponseNotAllowed(['GET', 'POST', 'PUT', 'DELETE'])

@csrf_exempt
def students_by_date_range(request):
    if request.method == 'GET':
        # Parsea los parámetros de fecha de la solicitud
        start_date_str = request.GET.get('start_date', None)
        end_date_str = request.GET.get('end_date', None)
        
        # Convierte las cadenas de fecha a objetos datetime si están presentes
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else None
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d') if end_date_str else None
        
        # Si se proporciona una fecha de finalización, ajusta la hora para incluir todo el día
        if end_date:
            end_date += timedelta(days=1, seconds=-1)
        
        # Realiza la consulta filtrando los registros por el rango de fechas
        if start_date and end_date:
            students = Student.objects.filter(created_at__range=(start_date, end_date))
        elif start_date:
            students = Student.objects.filter(created_at__gte=start_date)
        elif end_date:
            students = Student.objects.filter(created_at__lte=end_date)
        else:
            # Si no se proporcionan fechas, devuelve un mensaje de error
            return JsonResponse({"message": "No se proporcionaron fechas válidas para el rango"}, status=400)
        
        # Verifica si se encontraron estudiantes en el rango de fechas
        if students.exists():
            # Serializa los resultados y devuelve la respuesta
            serializer = StudentSerializer(students, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({"message": "No se encontraron estudiantes en el rango de fechas proporcionado"}, status=200)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)