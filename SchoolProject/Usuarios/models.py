from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    usuario = models.CharField('usuario', max_length=50)
    contrasenia = models.CharField('contrasenia', max_length=128)  # Aumentamos la longitud para almacenar el hash seguro
    estatus = models.BooleanField('estatus')

    #def save(self, *args, **kwargs):
        # Al guardar el objeto User, si la contraseña no está hasheada, la hasheamos
        #if not self._state.adding:  # Verificamos si el objeto ya existe en la base de datos
            #if not self.contrasenia.startswith('pbkdf2_sha256'):  # Verificamos si la contraseña ya está hasheada
                #self.contrasenia = make_password(self.contrasenia)
        #super(User, self).save(*args, **kwargs)
