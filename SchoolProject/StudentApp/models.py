from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    fee = models.IntegerField()
    userId = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Se establece automáticamente en la fecha y hora actual cuando se crea el objeto
    updated_at = models.DateTimeField(auto_now=True)      # Se actualiza automáticamente a la fecha y hora actual cada vez que se guarda el objeto

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)