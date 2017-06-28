from django.contrib import admin

# Register your models here.
from polls.models import *

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Hospital)
admin.site.register(Convenio)
admin.site.register(Exame)
admin.site.register(ModeloExame)
admin.site.register(Consulta)