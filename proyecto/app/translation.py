from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Tratamiento)
class TratamientoTranslationOptions(TranslationOptions):
    fields = ('nombre', 'descripcion')
