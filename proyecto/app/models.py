from django.db import models


# Create your models here.

class Info(models.Model):
    titulo = models.CharField(max_length=80, null=True)
    texto = models.TextField(null= True)
    logo = models.ImageField(upload_to='static/img')
    tel = models.TextField(null=True)
    #campos_footer 
    
class Tratamiento(models.Model):
    nombre = models.CharField(max_length=80, null= True)
    descripcion = models.TextField(null= True)
    imagen = models.ImageField(upload_to='static/img')


class Patologia(models.Model):
    nombre = models.CharField(max_length=80, null= True)
    descripcion = models.TextField(null= True)


class Testimonios(models.Model):
    nombre = models.CharField(max_length=70)
    edad = models.IntegerField(null=True)
    descripcion = models.TextField(null=True)
    fecha_publicacion = models.DateTimeField()

class EntradaBlog(models.Model):
    titulo = models.CharField(max_length=70)
    descripcion = models.TextField(null=True)
    fecha = models.DateTimeField()
    imagen = models.ImageField(upload_to='static/img')

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)