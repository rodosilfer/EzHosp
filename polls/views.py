#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .forms import PatientForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from polls.models import Patient

class Index(TemplateView):
    template_name = "polls/index.html"

class PatientList(ListView):
    model = Patient

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