from django.contrib import admin
from .models import Video, Tratamiento, Info, EntradaBlog, Contacto,Sistema, Patologia

# Register your models here.
admin.site.register(Video)
admin.site.register(Tratamiento)
admin.site.register(Info)
admin.site.register(EntradaBlog)
admin.site.register(Contacto)
admin.site.register(Patologia)
admin.site.register(Sistema)
