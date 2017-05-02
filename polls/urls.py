from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.Index.as_view(), name='index'),
	url(r'^convenio/$', views.ConvenioList.as_view(), name='convenio_list'),
	url(r'^patient/$', views.PatientList.as_view(), name='patient_list'),
	url(r'^convenio/new$', views.ConvenioCreate.as_view(), name='convenio_new'),
	url(r'^patient/new$', views.PatientCreate.as_view(), name='patient_new'),
	url(r'^convenio/edit/(?P<pk>\d+)$', views.ConvenioUpdate.as_view(), name='convenio_edit'),
	url(r'^patient/edit/(?P<pk>\d+)$', views.PatientUpdate.as_view(), name='patient_edit'),
	url(r'^convenio/delete/(?P<pk>\d+)$', views.ConvenioDelete.as_view(), name='convenio_delete'),
	url(r'^patient/delete/(?P<pk>\d+)$', views.PatientDelete.as_view(), name='patient_delete')
]
