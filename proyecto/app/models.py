from django.db import models


# Create your models here.

class Info(models.Model):
    tituloPrincipal = models.CharField(max_length=80, null=True)
    logo = models.ImageField(upload_to='static/img')
    tituloCentro = models.CharField(max_length=80, null=True)
    textoCentro = models.TextField(null=True)
    imagenCentro = models.ImageField(upload_to='static/img')
    tituloPerfil = models.CharField(max_length=80, null=True)
    textoPerfil = models.TextField(null=True)
    imagenPerfil = models.ImageField(upload_to='static/img')
    direccion = models.CharField(max_length=80, null=True)
    tel = models.IntegerField(null= True,blank=True)
    mail = models.EmailField(null= True,blank=True)
    horario = models.IntegerField(null= True,blank=True)

    def __str__(self):         
        return self.tituloPrincipal
    
    #redes
    
class Tratamiento(models.Model):
    nombre = models.CharField(max_length=80, null= True)
    descripcion = models.TextField(null= True)
    imagen = models.ImageField(upload_to='static/img')
    
    def __str__(self):         
        return self.nombre


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
    destacados = models.BooleanField(default=False)


    def __str__(self):         
        return self.titulo

    

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)