# -*- encoding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
	#Autenticacao
	url(r'^$', views.Index.as_view(), name='index'),
	url(r'^login/$', views.login, name='login_list'), #login_user .as_view()#
	url(r'^logout/$', views.logout_user, name='logout'),

	url(r'^exame/$', views.ExameList.as_view(), name='exame_list'),
	url(r'^hospital/$', views.HospList.as_view(), name='hospital_list'),
	url(r'^convenio/$', views.ConvenioList.as_view(), name='convenio_list'),
	url(r'^patient/$', views.PatientList.as_view(), name='patient_list'),
	url(r'^medico/$', views.MedicoList.as_view(), name='medico_list'),
	url(r'^consulta/$', views.ConsultaList.as_view(), name='consulta_list'),
	url(r'^gerenciarexame/$', views.GerenciarExame.as_view(), name='gerenciarexame_list'),

	url(r'^exame/new$', views.ExameCreate.as_view(), name='exame_new'),
	url(r'^hospital/new$', views.HospCreate.as_view(), name='hospital_new'),
	url(r'^convenio/new$', views.ConvenioCreate.as_view(), name='convenio_new'),
	url(r'^patient/new$', views.PatientCreate.as_view(), name='patient_new'),
	url(r'^medico/new$', views.MedicoCreate.as_view(), name='medico_new'),
	url(r'^consulta/new$', views.ConsultaCreate.as_view(), name='consulta_new'),

	url(r'^exame/edit/(?P<pk>\d+)$$', views.ExameUpdate.as_view(), name='exame_edit'),
	url(r'^hospital/edit/(?P<pk>\d+)$', views.HospUpdate.as_view(), name='hospital_edit'),
	url(r'^convenio/edit/(?P<pk>\d+)$', views.ConvenioUpdate.as_view(), name='convenio_edit'),
	url(r'^patient/edit/(?P<pk>\d+)$', views.PatientUpdate.as_view(), name='patient_edit'),
	url(r'^medico/edit/(?P<pk>\d+)$', views.MedicoUpdate.as_view(), name='medico_edit'),
	url(r'^consulta/edit/(?P<pk>\d+)$', views.ConsultaUpdate.as_view(), name='consulta_edit'),

	url(r'^exame/delete/(?P<pk>\d+)$', views.ExameDelete.as_view(), name='exame_delete'),
	url(r'^hospital/delete/(?P<pk>\d+)$', views.HospDelete.as_view(), name='hospital_delete'),
	url(r'^convenio/delete/(?P<pk>\d+)$', views.ConvenioDelete.as_view(), name='convenio_delete'),
	url(r'^patient/delete/(?P<pk>\d+)$', views.PatientDelete.as_view(), name='patient_delete'),
	url(r'^medico/delete/(?P<pk>\d+)$', views.MedicoDelete.as_view(), name = 'medico_delete'),
	url(r'^consulta/delete/(?P<pk>\d+)$', views.ConsultaDelete.as_view(), name='consulta_delete'),

	url(r'^medico/(?P<pk>\d+)$', views.MedicoView.as_view(), name = 'medico_view'),
	url(r'^medico/search/', views.MedicoSearchView, name = 'medico_search'),
	url(r'^convenio/search/', views.ConvenioSearchView, name = 'convenio_search'),
        url(r'^exame/search/', views.ExameSearchView, name = 'exame_search'),
	url(r'^exame/marcar/', views.MarcarExameCreate, name = 'exame_marcar')

]
