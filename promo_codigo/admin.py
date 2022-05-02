from django.contrib import admin
from .models import PromoCodigo

class CodigoPromoAdmin(admin.ModelAdmin):
    excude=['codigo']

admin.site.register(PromoCodigo, CodigoPromoAdmin)
    

