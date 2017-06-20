# -*- encoding: utf-8 -*-
#Define funcoes em python que recebe um objeto HttpRequest e retorna um objeto HttpResponse
#HttpRequest: criado automaticamente pelo Django. Contem os dados da requisicao que chegou.
#HttpResponse: responsabilidade do programador. Todas views precisam retornar esse objeto.

#from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-
from .forms import *
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render
from django.db.models import Q
from polls.models import *
from django.shortcuts import render
from django.contrib.auth import login, logout

#################################### PAGINA INICIAL ###################################
class Index(TemplateView):
    template_name = "polls/index.html"

##################################### Autenticaçao ####################################
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = request.POST['user'] #Valor digitado na pg HTML
            passw = request.POST['password'] #Valor digitado na pg HTML
            #print "user: ", user
            #print "password: ", password
            paciente=None
            hospital=None
            convenio=None
            medico=None
            try:
                paciente = Patient.objects.get(login=user, password=passw)
            except:
                pass

            try:
                hospital = Hospital.objects.get(login=user, password=passw)
            except:
                pass

            try:
                convenio = Convenio.objects.get(login=user, password=passw)
            except:
                pass

            try:
                medico = Medico.objects.get(login=user, password=passw)
            except:
                pass

            loguser=None
            flag=0
            if paciente is not None:
                loguser = paciente
                flag=1
                print("OK 1")
            elif hospital is not None:
                loguser = hospital
                flag=2
                print("OK 2")
            elif convenio is not None:
                loguser = convenio
                flag = 3
                print("OK 3")
            elif medico is not None:
                loguser = medico
                flag = 4
                print("OK 4")

            #Faz o login
            if loguser is not None: #user is not None:
                print("loguser: ", loguser)
                if flag==1:
                    return render(request, 'polls/pPaciente.html', {'paciente': paciente})
                elif flag==2:
                    return render(request, 'polls/pHospital.html', {'hospital': hospital})
                elif flag==3:
                    return render(request, 'polls/pConvenio.html', {'convenio': convenio})
                elif flag==4:
                    return render(request, 'polls/pMedico.html', {'medico': medico})
                else:
                    return redirect("polls/login.html")#'/admin/')
            else:
                return render(request, 'polls/login.html', {'form': form, 'erro': True})
                print("ERRO")
        else:
            return render(request, 'polls/login.html', {'form': form, 'erro': True})
    else:
        form = LoginForm()

    return render(request, 'polls/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')


##################################### PACIENTE #########################################
class PatientList(ListView):
    model = Patient
    template_name = 'polls/Paciente/patient_list.html'

class PatientCreate(CreateView):
    model = Patient
    success_url = reverse_lazy('patient_list')
    form_class = PatientForm
    template_name = 'polls/Paciente/patient_form.html'

class PatientUpdate(UpdateView):
    model = Patient
    success_url = reverse_lazy('patient_list')
    form_class = PatientForm
    template_name = 'polls/Paciente/patient_form.html'

class PatientDelete(DeleteView):
    model = Patient
    success_url = reverse_lazy('patient_list')
    template_name = 'polls/Paciente/patient_confirm_delete.html'

    def get(self, *a, **kw):
        return self.delete(*a, **kw)

##################################### Convenio #########################################
class ConvenioList(ListView):
    model = Convenio
    template_name = 'polls/Convenio/convenio_list.html'

class ConvenioCreate(CreateView):
    model = Convenio
    success_url = reverse_lazy('convenio_list')
    form_class = ConvenioForm
    template_name = 'polls/Convenio/convenio_form.html'

class ConvenioUpdate(UpdateView):
    model = Convenio
    success_url = reverse_lazy('convenio_list')
    form_class = ConvenioForm
    template_name = 'polls/Convenio/convenio_form.html'

def ConvenioSearchView(request):
    form = ConvenioBuscarForm()
    try:
        if request.method == 'POST':
            name = request.POST['firstName']
            conv = Convenio.objects.filter(Q(firstName=name))  # | Q(income__isnull=True)firstName=fj''')
            return redirect('/convenio/' + conv.id)

        return render(request, 'polls/Convenio/convenio_search.html', {"form": form})
    except:
        return render(request, 'polls/Convenio/convenio_search.html', {"form": form, "message": "Convenio não encontrado"})

class ConvenioDelete(DeleteView):
    model = Convenio
    success_url = reverse_lazy('convenio_list')

    def get(self, *a, **kw):
        return self.delete(*a, **kw)



##################################### MEDICO #########################################
class MedicoCreate(CreateView):
    model = Medico
    success_url = reverse_lazy('medico_list')
    form_class = MedicoForm
    template_name = 'polls/Medico/medico_form.html'

class MedicoUpdate(UpdateView):
    model = Medico
    success_url = reverse_lazy('medico_list')
    form_class = MedicoForm
    template_name = 'polls/Medico/medico_form.html'

class MedicoList(ListView):
    model = Medico
    template_name = 'polls/Medico/medico_list.html'

class MedicoView(DetailView):
    model = Medico
    template_name = 'polls/Medico/medico_detail.html'

def MedicoSearchView(request):
	form = MedicoBuscarForm(request.POST or None)
	try:
		if request.method == 'POST':
			name = request.POST['firstName']
			med = Medico.objects.get(Q(firstName=name))# | Q(income__isnull=True)firstName=fj''')
			return redirect('/medico/' + str(med.id))
    
		return render(request, 'polls/Medico/medico_search.html', { "form" : form })
	except Exception as e:
		print (e)
		return render(request, 'polls/Medico/medico_search.html', { "form" : form, "message" : "Medico não encontrado" })

class MedicoDelete(DeleteView):
	model = Medico
	success_url = reverse_lazy('medico_list')

	def get(self, *a, **kw):
		return self.delete(*a, **kw)


##################################### HOSPITAL #########################################

class HospList(ListView):
	model = Hospital
	template_name = 'polls/Hospital/hospital_list.html'

class HospCreate(CreateView):
    model = Hospital
    success_url = reverse_lazy('hospital_list')
    form_class = HospForm
    template_name = 'polls/Hospital/hospital_form.html'

class HospUpdate(UpdateView):
    model = Hospital
    success_url = reverse_lazy('hospital_list')
    form_class = HospForm
    template_name = 'polls/Hospital/hospital_form.html'

class HospDelete(DeleteView):
    model = Hospital
    success_url = reverse_lazy('hospital_list')

    def get(self, *a, **kw):
        return self.delete(*a, **kw)

##################################### MODELO EXAME #########################################
class ModeloExameList(ListView):
    model = ModeloExame
    template_name = 'polls/ModeloExame/modelo_exame_list.html'

class ModeloExameCreate(CreateView):
    model = ModeloExame
    success_url = reverse_lazy('modelo_exame_list')
    form_class = ModeloExameForm
    template_name = 'polls/ModeloExame/modelo_exame_form.html'

class ModeloExameUpdate(UpdateView):
    model = ModeloExame
    success_url = reverse_lazy('modelo_exame_list')
    form_class = ModeloExameForm
    template_name = 'polls/ModeloExame/modelo_exame_form.html'

class ModeloExameDelete(DeleteView):
    model = ModeloExame
    success_url = reverse_lazy('modelo_exame_list')

    def get(self, *a, **kw):
        return self.delete(*a, **kw)

##################################### EXAME #########################################
class ExameList(ListView):
    model = Exame
    template_name = 'polls/Exame/exame_list.html'

class MarcarExameCreate(CreateView):
    model = Exame
    success_url = reverse_lazy('exame_list')
    form_class = ExameMarcar
    template_name = 'polls/Exame/exame_marcar.html'

class ExameDelete(DeleteView):
    model = Exame
    success_url = reverse_lazy('exame_list')

    def get(self, *a, **kw):
        return self.delete(*a, **kw)

def ExameSearchView(request):
    form =ExameBuscarForm()
    try:
        if request.method == 'POST':
            nome = request.POST['nome']
            exm = Exame.objects.filter(Q(nome=nome))  # | Q(income__isnull=True)firstName=fj''')
            return redirect('/exame/' + exm.id)

        return render(request, 'polls/Exame/exame_search.html', {"form": form})
    except:
        return render(request, 'polls/Exame/exame_search.html', {"form": form, "message": "Exame nao encontrado"})

class GerenciarExame(CreateView):
    model = GerenciarExame
    success_url = reverse_lazy('gerenciarexame_list')
    form_class = GerenciarExameForm


############################ CONSULTA ############################
class ConsultaList(ListView):
    model = Consulta
    template_name = 'polls/Consulta/consulta_list.html'

class ConsultaCreate(CreateView):
    model = Consulta
    success_url = reverse_lazy('consulta_list')
    form_class = ConsultaForm
    template_name = 'polls/Consulta/consulta_form.html'

class ConsultaUpdate(UpdateView):
    model = Consulta
    success_url = reverse_lazy('consulta_list')
    form_class = ConsultaForm
    template_name = 'polls/Consulta/consulta_form.html'

class ConsultaDelete(DeleteView):
    model = Consulta
    success_url = reverse_lazy('consulta_list')

    def get(self, *a, **kw):
        return self.delete(*a, **kw)
