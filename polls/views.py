#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .forms import *
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from polls.models import *

class Index(TemplateView):
    template_name = "polls/index.html"


class ConvenioList(ListView):
	model = Convenio

class PatientList(ListView):
    model = Patient

class MedicoList(ListView):
    model = Medico

class PatientCreate(CreateView):
    model = Patient
    success_url = reverse_lazy('patient_list')
    form_class = PatientForm

class PatientUpdate(UpdateView):
    model = Patient
    success_url = reverse_lazy('patient_list')
    form_class = PatientForm

class PatientDelete(DeleteView):
    model = Patient
    success_url = reverse_lazy('patient_list')

    def get(self, *a, **kw):
        return self.delete(*a, **kw)

class ConvenioCreate(CreateView):
    model = Convenio
    success_url = reverse_lazy('convenio_list')
    form_class = ConvenioForm

class ConvenioUpdate(UpdateView):
    model = Convenio
    success_url = reverse_lazy('convenio_list')
    form_class = ConvenioForm

class ConvenioDelete(DeleteView):
    model = Convenio
    success_url = reverse_lazy('convenio_list')

    def get(self, *a, **kw):
        return self.delete(*a, **kw)

class MedicoCreate(CreateView):
    model = Medico
    success_url = reverse_lazy('medico_list')
    form_class = MedicoForm

class MedicoUpdate(UpdateView):
    model = Medico
    success_url = reverse_lazy('medico_list')
    form_class = MedicoForm

class MedicoDelete(DeleteView):
    model = Medico
    success_url = reverse_lazy('medico_list')

    def get(self, *a, **kw):
        return self.delete(*a, **kw)
