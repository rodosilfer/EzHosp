from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Patient)
admin.site.register(Medico)
admin.site.register(Hospital)
admin.site.register(Exame)
admin.site.register(Convenio)