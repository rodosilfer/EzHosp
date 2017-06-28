from django.conf.urls import url
from django.contrib.auth import views as auth_views

from polls import views

urlpatterns = [
	# Login
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^$', views.Home, name='home'),
    # Paciente
	url(r'^paciente/$', views.HomePaciente, name='paciente'),
    url(r'^paciente/new/$', views.CreatePaciente, name='create_paciente'),
	url(r'^paciente/edit/$', views.UpdatePaciente, name='edit_paciente'),
	url(r'^paciente/list/$', views.ListPaciente, name='list_paciente'),
	# Medico
	url(r'^medico/$', views.HomeMedico, name='medico'),
    url(r'^medico/new/$', views.CreateMedico, name='create_medico'),
	url(r'^medico/view/(?P<pk>\d+)$', views.ViewMedico, name='view_medico'),
	url(r'^medico/edit/$', views.UpdateMedico, name='edit_medico'),
	url(r'^medico/list/$', views.ListMedico, name='list_medico'),
	url(r'^medico/search/$', views.SearchMedico, name='search_medico'),
	url(r'^medico/avaliar/up/(?P<pk>\d+)$', views.medico_up, name = 'medico_up'),
	url(r'^medico/avaliar/down/(?P<pk>\d+)$', views.medico_down, name = 'medico_down'),
	# Hospital
	url(r'^hospital/$', views.HomeHospital, name='hospital'),
    url(r'^hospital/new/$', views.CreateHospital, name='create_hospital'),
	url(r'^hospital/edit/$', views.UpdateHospital, name='edit_hospital'),
	url(r'^hospital/list/$', views.ListHospital, name='list_hospital'),
	# Convenio
	url(r'^convenio/$', views.HomeConvenio, name='convenio'),
    url(r'^convenio/new/$', views.CreateConvenio, name='create_convenio'),
	url(r'^convenio/edit/$', views.UpdateConvenio, name='edit_convenio'),
	url(r'^convenio/list/$', views.ListConvenio, name='list_convenio'),
	# Modelo Exame
	url(r'^modeloexame/list$', views.ListModeloExame, name='list_modelo_exame'),
	url(r'^modeloexame/new$', views.CreateModeloExame, name='create_modelo_exame'),
	url(r'^modeloexame/edit/(?P<pk>\d+)$', views.UpdateModeloExame, name='edit_modelo_exame'),
	url(r'^modeloexame/delete/(?P<pk>\d+)$', views.DeleteModeloExame, name='delete_modelo_exame'),
	# Exame
	url(r'^exame/list$', views.ListExame, name='list_exame'),
	url(r'^exame/new$', views.CreateExame, name='create_exame'),
	url(r'^exame/edit/(?P<pk>\d+)$', views.UpdateExame, name='edit_exame'),
	url(r'^exame/delete/(?P<pk>\d+)$', views.DeleteExame, name='delete_exame'),
	url(r'^exame/search/$', views.SearchExame, name='search_exame'),
	# Consulta
	url(r'^consulta/list$', views.ListConsulta, name='list_consulta'),
	url(r'^consulta/new$', views.CreateConsulta, name='create_consulta'),
	url(r'^consulta/edit/(?P<pk>\d+)$', views.UpdateConsulta, name='edit_consulta'),
	url(r'^consulta/delete/(?P<pk>\d+)$', views.DeleteConsulta, name='delete_consulta'),
	# Diagnostico
	url(r'^diagnostico/list$', views.ListDiagnostico, name='list_diagnostico'),
	url(r'^diagnostico/new$', views.CreateDiagnostico, name='create_diagnostico'),
	url(r'^diagnostico/edit/(?P<pk>\d+)$', views.UpdateDiagnostico, name='edit_diagnostico'),
	url(r'^diagnostico/delete/(?P<pk>\d+)$', views.DeleteDiagnostico, name='delete_diagnostico'),
]