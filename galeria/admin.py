from django.contrib import admin

from galeria.models import Fotografia

# Register your models here.

class listFotografias(admin.ModelAdmin):
    list_display = ('id','nome','legenda', 'publicada')
    list_display_links = ('id','nome')
    list_filter = ('categoria',)
    list_editable = ('publicada', )
    search_fields = ('nome','legenda')
    ordering = ("-data_fotografia", )


admin.site.register(Fotografia, listFotografias)