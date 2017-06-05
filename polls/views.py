#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .forms import *
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render

from django.db.models import Q

from polls.models import *

class Index(TemplateView):
    template_name = "polls/index.html"

class ConvenioList(ListView):
	model = Convenio

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

class ConvenioCreate(CreateView):
    model = Convenio
    success_url = reverse_lazy('convenio_list')
    form_class = ConvenioForm

class ConvenioUpdate(UpdateView):
    model = Convenio
    success_url = reverse_lazy('convenio_list')
    form_class = ConvenioForm

class ConvenioView(DetailView):
    model = Convenio

def ConvenioSearchView(request):
    form = ConvenioBuscarForm()
    try:
        if request.method == 'POST':
            name = request.POST['firstName']
            conv = Convenio.objects.filter(Q(firstName=name))  # | Q(income__isnull=True)firstName=fj''')
            return redirect('/convenio/' + conv.id)

        return render(request, 'polls/convenio_search.html', {"form": form})
    except:
        return render(request, 'polls/convenio_search.html', {"form": form, "message": "Convenio não encontrado"})

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

class MedicoList(ListView):
    model = Medico

class MedicoView(DetailView):
    model = Medico

def MedicoSearchView(request):
    form = MedicoBuscarForm()
    try:
        if request.method == 'POST':
            name = request.POST['firstName']
            med = Medico.objects.filter(Q(firstName=name))# | Q(income__isnull=True)firstName=fj''')
            return redirect('/medico/' + med.id)
    
        return render(request, 'polls/medico_search.html', { "form" : form })
    except:
        return render(request, 'polls/medico_search.html', { "form" : form, "message" : "Tem esse nego não" })

class MedicoDelete(DeleteView):
    model = Medico
    success_url = reverse_lazy('medico_list')

    def get(self, *a, **kw):
        return self.delete(*a, **kw)

class HospList(ListView):
    model = Hospital

class HospCreate(CreateView):
    model = Hospital
    success_url = reverse_lazy('hospital_list')
    form_class = HospForm

class HospUpdate(UpdateView):
    model = Hospital
    success_url = reverse_lazy('hospital_list')
    form_class = HospForm

class HospDelete(DeleteView):
    model = Hospital
    success_url = reverse_lazy('hospital_list')

    def get(self, *a, **kw):
        return self.delete(*a, **kw)

class ExameList(ListView):
    model = Exame

class ExameCreate(CreateView):
    model = Exame
    success_url = reverse_lazy('exame_list')
    form_class = ExameForm

class ExameUpdate(UpdateView):
    model = Exame
    success_url = reverse_lazy('exame_list')
    form_class = ExameForm

class ExameDelete(DeleteView):
    model = Exame
    success_url = reverse_lazy('exame_list')

    def get(self, *a, **kw):
        return self.delete(*a, **kw)

class ConsultaList(ListView):
    model = Consulta

class ConsultaCreate(CreateView):
    model = Consulta
    success_url = reverse_lazy('consulta_list')
    form_class = ConsultaForm

class ConsultaUpdate(UpdateView):
    model = Consulta
    success_url = reverse_lazy('consulta_list')
    form_class = ConsultaForm

class ConsultaDelete(DeleteView):
    model = Consulta
    success_url = reverse_lazy('consulta_list')

    def get(self, *a, **kw):
        return self.delete(*a, **kw)
