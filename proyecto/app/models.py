from django.db import models


# Create your models here.


class Inicio(models.Model):
    tituloPrincipal = models.CharField(max_length=80, null=True)
    logo = models.ImageField(upload_to='static/img')
    tituloCentro = models.CharField(max_length=80, null=True)
    textoCentro = models.TextField(null=True)
    imagenCentro = models.ImageField(upload_to='static/img')
    nombreDr = models.CharField(max_length=80, null=True)
    textoPerfil = models.TextField(null=True)
    imagenPerfil = models.ImageField(upload_to='static/img')

    class Meta:
        verbose_name = 'Info Inicio'
        verbose_name_plural = 'Info Inicio'


    def __str__(self):         
        return self.tituloPrincipal
    
    #redes
    
class Contacto(models.Model):
    nombreCentro =models.CharField(max_length=80, null=True)
    direccion = models.CharField(max_length=80, null=True)
    tel = models.IntegerField(null= True,blank=True)
    horario = models.CharField(max_length=80, null=True)
    mail = models.EmailField(null= True,blank=True)
    instagram = models.URLField(null=True,blank=True)
    facebook= models.URLField(null=True,blank=True)
    
    
    def __str__(self):         
        return self.nombreCentro
    
        
    
class Tratamiento(models.Model):
    nombre = models.CharField(max_length=80, null= True)
    descripcion = models.TextField(null= True)
    imagen = models.ImageField(upload_to='static/img')
    
    def __str__(self):         
        return self.nombre


class Sistema(models.Model):
    nombresistema = models.CharField(max_length=80, null= True)
    def __str__(self):         
        return self.nombresistema
    class Meta:
        ordering = ['nombresistema_es']

class Patologia(models.Model):
    nombrepatologia = models.CharField( max_length=80, null= True)
    sistema= models.ForeignKey(Sistema, related_name="patologias",on_delete=models.CASCADE, max_length=80, null= True )
    def __str__(self):         
        return self.nombrepatologia
    
    class Meta:
        ordering = ['nombrepatologia_es']

class Testimonio(models.Model):
    nombre = models.CharField(max_length=70)
    edad = models.IntegerField(null=True)
    descripcion = models.TextField(null=True)
    fecha_publicacion = models.DateTimeField()
    imagen = models.ImageField(upload_to = 'testimonios', default = 'testimonios/profile.png')

    def __str__(self):         
        return self.nombre

    

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