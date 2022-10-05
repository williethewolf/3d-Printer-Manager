from django.contrib import admin

# Register your models here.
from .models import Printer, Filament, Print
admin.site.register(Printer)
admin.site.register(Print)
admin.site.register(Filament)