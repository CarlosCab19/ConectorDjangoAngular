from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Usuarios.serializers import UserSerializer
from Usuarios.models import User 
from django.http import HttpResponseNotAllowed, HttpResponseNotFound

#para validar las credenciales
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
#para ver las contraseñas en texto plano
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
#para generar un tocken unico
import hashlib
import random
import string
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#para generar un tocken con datos (prueba)
import jwt
import secrets
#para extraer la informacion del usuario en el tocken 



@csrf_exempt
def usuario_lista(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def usuario_detalle(request, id):
    try:
        usuarioID = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponseNotFound("Usuario no encontrado")

    if request.method == 'GET':
        serializer = UserSerializer(usuarioID)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(usuarioID, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        usuarioID.delete()
        return JsonResponse({"message": "Usuario eliminado"}, status=204)

@csrf_exempt
def validar_credenciales(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        usuario = data.get('usuario', '')
        contrasenia = data.get('contrasenia', '')

        try:
            usuario = User.objects.get(usuario=usuario)
            contrasenia_valida = check_password(contrasenia, usuario.contrasenia)
            if contrasenia_valida:
                return JsonResponse({'mensaje': 'Credenciales válidas'})
            else:
                return JsonResponse({'error': 'Credenciales inválidas'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def ver_contrasenia(request, user_id):
    # Obtener el usuario de la base de datos
    usuario = get_object_or_404(User, id=user_id)

    # Devolver la contraseña del usuario antes de ser hasheada
    return HttpResponse(f'La contraseña de {usuario.nombre} es: {usuario.contrasenia}')

#@csrf_exempt
#def autenticar_usuario(request):
    #if request.method == 'POST':
        #data = JSONParser().parse(request)
        #usuario = data.get('usuario')
        #contrasenia = data.get('contrasenia')

        #if usuario and contrasenia:
            #try:
                #usuario_encontrado = User.objects.get(usuario=usuario, contrasenia=contrasenia)
                #return JsonResponse({"message": "Usuario autenticado"}, status=200)
            #except User.DoesNotExist:
                #return JsonResponse({"message": "Credenciales inválidas"}, status=401)
        #else:
            #return JsonResponse({"message": "Datos de usuario y contraseña requeridos"}, status=400)
    #else:
        #return JsonResponse({"message": "Método no permitido"}, status=405)


def generar_token():
    # Generar un token aleatorio único
    caracteres = string.ascii_letters + string.digits
    token = ''.join(random.choice(caracteres) for _ in range(64))
    return token


# Clave secreta para firmar el token (debería ser segura y privada en un entorno real)
SECRET_KEY = secrets.token_hex(32)

@csrf_exempt
def autenticar_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        usuario = data.get('usuario')
        contrasenia = data.get('contrasenia')

        if usuario and contrasenia:
            try:
                usuario_encontrado = User.objects.get(usuario=usuario, contrasenia=contrasenia)
                if usuario_encontrado:
                    # Generar un token JWT que incluya datos del usuario
                    payload = {
                        'usuario_id': usuario_encontrado.id,
                        'nombre': usuario_encontrado.nombre,
                        'estatus': usuario_encontrado.estatus
                        # Puedes incluir más datos del usuario aquí si lo deseas
                    }
                    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
                    return JsonResponse({"message": "Usuario autenticado", "token": token}, status=200)
                else:
                    return JsonResponse({"message": "Credenciales inválidas"}, status=401)
            except User.DoesNotExist:
                return JsonResponse({"message": "Credenciales inválidas"}, status=401)
        else:
            return JsonResponse({"message": "Datos de usuario y contraseña requeridos"}, status=400)
    else:
        return JsonResponse({"message": "Método no permitido"}, status=405)

SECRET_KEY = secrets.token_hex(32)
@csrf_exempt
def generar_token(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        usuario = data.get('usuario')
        contrasenia = data.get('contrasenia')

        if usuario and contrasenia:
            try:
                usuario_encontrado = User.objects.get(usuario=usuario, contrasenia=contrasenia)
                if usuario_encontrado:
                    # Generar un token JWT que incluya datos del usuario
                    payload = {
                        'usuario_id': usuario_encontrado.id,
                        'nombre': usuario_encontrado.nombre,
                        'estatus': usuario_encontrado.estatus
                        # Puedes incluir más datos del usuario aquí si lo deseas
                    }
                    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
                    
                    # Decodificar el token para extraer información del usuario
                    #decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
                    #usuario_id = decoded_token['usuario_id']
                    #nombre_usuario = decoded_token['nombre']
                    #estatus_usuario = decoded_token['estatus']

                    #return JsonResponse({"message": "Usuario autenticado", "token": token, "usuario_id": usuario_id, "nombre_usuario": nombre_usuario, "estatus_usuario":estatus_usuario}, status=200)
                    return JsonResponse({"token":token}, status=200)
                else:
                    return JsonResponse({"message": "Credenciales inválidas"}, status=401)
            except User.DoesNotExist:
                return JsonResponse({"message": "Credenciales inválidas"}, status=401)
        else:
            return JsonResponse({"message": "Datos de usuario y contraseña requeridos"}, status=400)
    else:
        return JsonResponse({"message": "Método no permitido"}, status=405)

SECRET_KEY = secrets.token_hex(32)
@csrf_exempt
def decifrar_token(request,token):
    if request.method == 'GET':
        #token = request.GET.get('token')
        if token:
            # Eliminar cualquier espacio en blanco al principio o al final del token
            token = token.strip()
            try:
                decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
                usuario_id = decoded_token.get('usuario_id')
                nombre = decoded_token.get('nombre')
                estatus = decoded_token.get('estatus')
                # Haz algo con los datos del usuario
                return JsonResponse({"usuario_id": usuario_id, "nombre": nombre, "estatus": estatus}, status=200)
            except jwt.ExpiredSignatureError:
                return JsonResponse({"message": "Token expirado"}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({"message": "Token inválido"}, status=401)
        else:
            return JsonResponse({"message": "Token no proporcionado"}, status=400)
    else:
        return JsonResponse({"message": "Método no permitido"}, status=405)
