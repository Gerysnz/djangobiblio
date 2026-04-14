from atexit import register
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from .models import Usuari


# Register your models here.
from .models import *


class ImatgeInline(admin.TabularInline):
    model = Imatge
    extra = 3
    readonly_fields = ('vista_previa',) # Opcional: para ver la miniatura ahí mismo

    def vista_previa(self, obj):
        if obj.imatge:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: contain;" />', obj.imatge.url)
        return "Sin imagen"
    

     
class LlibreAdmin(admin.ModelAdmin):
    inlines = [ImatgeInline]
    # Afegeix el mètode a readonly_fields perquè es mostri en la pàgina d'edició
    readonly_fields = ('vista_previa_imatge',)
    
    # Defineix quins camps es mostren en el formulari d'edició
    #fields = ('nom', 'imatge', 'vista_previa_imatge')
    exclude = ()
    
    def vista_previa_imatge(self, obj):
        if obj.imatge:
            # Retorna l'etiqueta HTML amb l'URL de la imatge
            return format_html('<img src="{}" width="150" height="150" style="object-fit: cover;" />', obj.imatge.url)
        return "No hi ha imatge"
    
    vista_previa_imatge.short_description = 'Previsualització'

class UsuariAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
            ("Altres dades (API auth)", {
                'fields': ('auth_token',),
            }),
    )
    readonly_fields = ["auth_token",]


    
admin.site.register(Llibre,LlibreAdmin)
admin.site.register(Usuari,UsuariAdmin)

