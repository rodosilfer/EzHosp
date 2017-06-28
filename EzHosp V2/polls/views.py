from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

from polls.forms import *
from polls.models import *

def Home(request):
	user = request.user
	if hasattr(user, 'paciente'):
		return redirect('paciente')
	elif hasattr(user, 'medico'):
		return redirect('medico')
	elif hasattr(user, 'hospital'):
		return redirect('hospital')
	elif hasattr(user, 'convenio'):
		return redirect('convenio')

	return render(request, 'index.html')

# Verificações
def isPaciente(user):
	return hasattr(user, 'paciente') or user.is_superuser

def isMedico(user):
	return hasattr(user, 'medico') or user.is_superuser

def isHospital(user):
	return hasattr(user, 'hospital') or user.is_superuser

def isConvenio(user):
	return hasattr(user, 'convenio') or user.is_superuser

# Paciente
@user_passes_test(isPaciente, login_url='/login/')
def HomePaciente(request):
	data = {'user': request.user}
	return render(request, 'Paciente/menu.html', data)

@user_passes_test(isPaciente, login_url='/login/')
def UpdatePaciente(request):
	user_form = EditUserForm(request.POST or None, instance=request.user)
	paciente_form = PacienteForm(request.POST or None, instance=request.user.paciente)
	if request.method == 'POST':
		if user_form.is_valid() and paciente_form.is_valid():
			user_form.save()
			paciente_form.save()
			messages.success(request, 'Paciente salvo com sucesso!')
			return redirect('paciente')
		else:
			messages.error(request, 'Please correct the error below.')
	return render(request, 'Paciente/paciente_form.html', {
		'user_form': user_form,
		'paciente_form': paciente_form
	})

def CreatePaciente(request, template_name='Paciente/paciente_form.html'):
	if request.user.is_authenticated and not request.user.is_superuser:
		messages.success(request, 'Voce ja esta logado!')
		return redirect('paciente')
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		paciente_form = PacienteForm(request.POST)
		if paciente_form.is_valid() and user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			paciente = paciente_form.save(commit=False)
			paciente.user = user
			paciente.save()
			messages.success(request, 'Paciente criado com sucesso!')
			return redirect('home')
	else:
		user_form = UserForm()
		paciente_form = PacienteForm()
	return render(request, template_name, {
		'user_form': user_form,
		'paciente_form': paciente_form
	})

@login_required
def ListPaciente(request, template_name='Paciente/paciente_list.html'):
	data = {}
	pacientes = {}
	if isMedico(request.user):
		pacientes = Paciente.objects.filter(consulta__medico=request.user.medico)
	elif isHospital(request.user):
		pacientes = Paciente.objects.filter(consulta__medico__hospital=request.user.hospital)
	data['object_list'] = pacientes
	return render(request, template_name, data)

# Medico
@user_passes_test(isMedico, login_url='/login/')
def HomeMedico(request):
	return render(request, 'Medico/menu.html')

@user_passes_test(isMedico, login_url='/login/')
def UpdateMedico(request):
	user_form = EditUserForm(request.POST or None, instance=request.user)
	medico_form = MedicoForm(request.POST or None, instance=request.user.medico)
	if request.method == 'POST':
		if user_form.is_valid() and medico_form.is_valid():
			user_form.save()
			medico_form.save()
			messages.success(request, 'Medico salvo com sucesso!')
			return redirect('medico')
		else:
			messages.error(request, 'Please correct the error below.')
	return render(request, 'Medico/medico_form.html', {
		'user_form': user_form,
		'medico_form': medico_form
	})

def CreateMedico(request, template_name='Medico/medico_form.html'):
	if request.user.is_authenticated and not request.user.is_superuser:
		messages.success(request, 'Voce ja esta logado!')
		return redirect('medico')
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		medico_form = MedicoForm(request.POST)
		if medico_form.is_valid() and user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			medico = medico_form.save(commit=False)
			medico.user = user
			medico.nota = 0
			medico.save()
			messages.success(request, 'Medico criado com sucesso!')
			return redirect('home')
	else:
		user_form = UserForm()
		medico_form = MedicoForm()
	return render(request, template_name, {
		'user_form': user_form,
		'medico_form': medico_form
	})

@user_passes_test(isMedico, login_url='/login/')
def ListMedico(request, template_name='Medico/medico_list.html'):
	medicos = Medico.objects.all()
	data = {}
	data['object_list'] = medicos
	return render(request, template_name, data)

@login_required
def SearchMedico(request, template_name='Medico/medico_search.html'):
	form = SearchUserForm(request.POST or None)
	data = {"form": form}

	if request.method == 'POST':
		name = request.POST['first_name']
		data['object_list'] = Medico.objects.filter(user__first_name__iexact=name)  # | Q(income__isnull=True)firstName=fj''')
	return render(request, template_name, data)

@login_required
def ViewMedico(request, pk, template_name='Medico/medico_detail.html'):
	medico = get_object_or_404(Medico, id=pk)
	podeVotar = request.GET.get('d', '1')
	data = {'medico': medico, 'podeVotar': podeVotar}
	print(medico)
	return render(request, template_name, data)

@login_required
def medico_up(request, pk):
	medico = Medico.objects.get(id=pk)
	if medico.nota is not None:
		medico.nota = medico.nota + 1
	else:
		medico.nota = 0

	medico.save()
	return redirect('/medico/view/' + pk + '?d=0')

@login_required
def medico_down(request, pk):
	medico = Medico.objects.get(id=pk)
	if medico.nota is not None:
		medico.nota = medico.nota - 1
	else:
		medico.nota = 0

	medico.save()
	return redirect('/medico/view/' + pk + '?d=1')

# Hospital
@user_passes_test(isHospital, login_url='/login/')
def HomeHospital(request):
	data = {'user': request.user}
	return render(request, 'Hospital/menu.html', data)

@user_passes_test(isHospital, login_url='/login/')
def UpdateHospital(request):
	user_form = EditUserForm2(request.POST or None, instance=request.user)
	hospital_form = HospitalForm(request.POST or None, instance=request.user.hospital)
	if request.method == 'POST':
		if user_form.is_valid() and hospital_form.is_valid():
			user_form.save()
			hospital_form.save()
			messages.success(request, 'Hospital salvo com sucesso!')
			return redirect('hospital')
		else:
			messages.error(request, 'Please correct the error below.')
	return render(request, 'Hospital/hospital_form.html', {
		'user_form': user_form,
		'hospital_form': hospital_form
	})

def CreateHospital(request, template_name='Hospital/hospital_form.html'):
	if request.user.is_authenticated and not request.user.is_superuser:
		messages.success(request, 'Voce ja esta logado!')
		return redirect('hospital')
	if request.method == 'POST':
		user_form = UserForm2(request.POST)
		hospital_form = HospitalForm(request.POST)
		if hospital_form.is_valid() and user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			hospital = hospital_form.save(commit=False)
			hospital.user = user
			hospital.save()
			messages.success(request, 'Hospital criado com sucesso!')
			return redirect('home')
	else:
		user_form = UserForm2()
		hospital_form = HospitalForm()
	return render(request, template_name, {
		'user_form': user_form,
		'hospital_form': hospital_form
	})

@user_passes_test(isHospital, login_url='/login/')
def ListHospital(request, template_name='Hospital/hospital_list.html'):
	hospitals = Hospital.objects.all()
	data = {}
	data['object_list'] = hospitals
	return render(request, template_name, data)

# Convenio
@user_passes_test(isConvenio, login_url='/login/')
def HomeConvenio(request):
	data = {'user': request.user}
	return render(request, 'Convenio/menu.html', data)

@user_passes_test(isConvenio, login_url='/login/')
def UpdateConvenio(request):
	user_form = EditUserForm2(request.POST or None, instance=request.user)
	convenio_form = ConvenioForm(request.POST or None, instance=request.user.convenio)
	if request.method == 'POST':
		if user_form.is_valid() and convenio_form.is_valid():
			user_form.save()
			convenio_form.save()
			messages.success(request, 'Convenio salvo com sucesso!')
			return redirect('convenio')
		else:
			messages.error(request, 'Please correct the error below.')
	return render(request, 'Convenio/convenio_form.html', {
		'user_form': user_form,
		'convenio_form': convenio_form
	})

def CreateConvenio(request, template_name='Convenio/convenio_form.html'):
	if request.user.is_authenticated and not request.user.is_superuser:
		messages.success(request, 'Voce ja esta logado!')
		return redirect('convenio')
	if request.method == 'POST':
		user_form = UserForm2(request.POST)
		convenio_form = ConvenioForm(request.POST)
		if convenio_form.is_valid() and user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			convenio = convenio_form.save(commit=False)
			convenio.user = user
			convenio.save()
			messages.success(request, 'Convenio criado com sucesso!')
			return redirect('home')
	else:
		user_form = UserForm2()
		convenio_form = ConvenioForm()
	return render(request, template_name, {
		'user_form': user_form,
		'convenio_form': convenio_form
	})

@user_passes_test(isConvenio, login_url='/login/')
def ListConvenio(request, template_name='Convenio/convenio_list.html'):
	convenios = Convenio.objects.all()
	data = {}
	data['object_list'] = convenios
	return render(request, template_name, data)

# Modelo Exame
@user_passes_test(isHospital, login_url='/login/')
def UpdateModeloExame(request, pk):
	modelo = get_object_or_404(ModeloExame, id=pk)
	form = ModeloExameForm(request.POST or None, instance=modelo)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			messages.success(request, 'Exame salvo com sucesso!')
			return redirect('hospital')
		else:
			messages.error(request, 'Please correct the error below.')
	return render(request, 'ModeloExame/modelo_exame_form.html', { 'form': form, })

@user_passes_test(isHospital, login_url='/login/')
def CreateModeloExame(request, template_name='ModeloExame/modelo_exame_form.html'):
	form = ModeloExameForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			modelo = form.save(commit=False)
			hospital = request.user.hospital
			modelo.hospital = hospital
			modelo.save()
			messages.success(request, 'Exame criado com sucesso!')
			return redirect('hospital')
	return render(request, template_name, { 'form': form })

@user_passes_test(isHospital, login_url='/login/')
def ListModeloExame(request, template_name='ModeloExame/modelo_exame_list.html'):
	modelos = ModeloExame.objects.filter(hospital=request.user.hospital)
	data = {}
	data['object_list'] = modelos
	return render(request, template_name, data)

@user_passes_test(isHospital, login_url='/login/')
def DeleteModeloExame(request, pk):
	modelo = get_object_or_404(ModeloExame, id=pk)
	if modelo.hospital == request.user.hospital:
		modelo.delete()
		return redirect('list_modelo_exame')
	return redirect('login')

# Exame
@user_passes_test(isPaciente, login_url='/login/')
def UpdateExame(request, pk):
	exame = get_object_or_404(Exame, id=pk)
	form = ExameForm(request.POST or None, instance=exame)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			messages.success(request, 'Exame editado com sucesso!')
			return redirect('list_exame')
		else:
			messages.error(request, 'Please correct the error below.')
	return render(request, 'Exame/exame_form.html', { 'form': form, })

@user_passes_test(isPaciente, login_url='/login/')
def CreateExame(request, template_name='Exame/exame_form.html'):
	form = ExameForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			exame = form.save(commit=False)
			paciente = request.user.paciente
			exame.paciente = paciente
			exame.save()
			messages.success(request, 'Exame marcado com sucesso!')
			return redirect('list_exame')
	return render(request, template_name, { 'form': form })

@login_required
def ListExame(request, template_name='Exame/exame_list.html'):
	exames = {}
	data = {}
	if isPaciente(request.user):
		exames = Exame.objects.filter(paciente=request.user.paciente)
		data['isPaciente'] = True
	elif isHospital(request.user):
		exames = Exame.objects.filter(nome__hospital=request.user.hospital)
	data['object_list'] = exames
	return render(request, template_name, data)

@login_required
def DeleteExame(request, pk):
	exame = get_object_or_404(Exame, id=pk)
	if isHospital(request.user) and exame.nome.hospital == request.user.hospital:
		exame.delete()
		return redirect('list_exame')
	if isPaciente(request.user) and exame.paciente== request.user.paciente:
		exame.delete()
		return redirect('list_exame')
	return redirect('login')

@login_required
def SearchExame(request, template_name='Exame/exame_search.html'):
	form = BuscaExameForm(request.POST or None)
	try:
		data = {"form": form}
		if request.method == 'POST':
			name = request.POST['first_name']
			exames = Exame.objects.filter(nome__nome__icontains=name)  # | Q(income__isnull=True)firstName=fj''')
			if isPaciente(request.user):
				data['object_list'] = exames.filter(paciente=request.user.paciente)
			elif isHospital(request.user):
				data['object_list'] = exames.filter(nome__hospital=request.user.hospital)
		return render(request, template_name, data)
	except Exception as e:
		print(e)
		return render(request, template_name, {"form": form, "message": "Medico não encontrado"})

# Consulta
@login_required
def UpdateConsulta(request, pk):
	consulta = get_object_or_404(Consulta, id=pk)
	form = ConsultaForm(request.POST or None, instance=consulta)
	if request.method == 'POST':
		if form.is_valid() :
			form.save()
			messages.success(request, 'Consulta salva com sucesso!')
			return redirect('list_consulta')
		else:
			messages.error(request, 'Please correct the error below.')
	return render(request, 'Consulta/consulta_form.html', { 'form': form })

def CreateConsulta(request, template_name='Consulta/consulta_form.html'):
	form = ConsultaForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			consulta = form.save(commit=False)
			consulta.paciente = request.user.paciente
			consulta.save()
			messages.success(request, 'Consulta marcada com sucesso!')
			return redirect('list_consulta')
	return render(request, template_name, { 'form': form })

@login_required
def ListConsulta(request, template_name='Consulta/consulta_list.html'):
	data = {}
	consultas = {}
	if isPaciente(request.user):
		consultas = Consulta.objects.filter(paciente=request.user.paciente)
		data['isPaciente'] = True
	elif isHospital(request.user):
		consultas = Consulta.objects.filter(medico__hospital=request.user.hospital)
	elif isMedico(request.user):
		consultas = Consulta.objects.filter(medico=request.user.medico)

	data['object_list'] = consultas
	return render(request, template_name, data)

@user_passes_test(isPaciente, login_url='/login/')
def DeleteConsulta(request, pk):
	consulta = get_object_or_404(Consulta, id=pk)
	if consulta.paciente == request.user.paciente:
		consulta.delete()
		return redirect('list_consulta')
	return redirect('login')

# Diagnostico
@login_required
def UpdateDiagnostico(request, pk):
	diagnostico = get_object_or_404(Diagnostico, id=pk)
	form = DiagnosticoForm(request.POST or None, instance=diagnostico)
	if request.method == 'POST':
		if form.is_valid() :
			form.save()
			messages.success(request, 'Diagnostico salvo com sucesso!')
			return redirect('list_diagnostico')
		else:
			messages.error(request, 'Please correct the error below.')
	return render(request, 'Diagnostico/diagnostico_form.html', { 'form': form })

@user_passes_test(isMedico, login_url='/login/')
def CreateDiagnostico(request, template_name='Diagnostico/diagnostico_form.html'):
	form = DiagnosticoForm(request.POST or None, user=request.user)
	if request.method == 'POST':
		if form.is_valid():
			diagnostico = form.save(commit=False)
			diagnostico.horario = datetime.now()
			diagnostico.medico = request.user.medico
			diagnostico.save()
			messages.success(request, 'Diagnostico criado com sucesso!')
			return redirect('list_diagnostico')
	return render(request, template_name, { 'form': form })

@login_required
def ListDiagnostico(request, template_name='Diagnostico/diagnostico_list.html'):
	data = {}
	diagnostico = {}
	if isPaciente(request.user):
		diagnostico = Diagnostico.objects.filter(paciente=request.user.paciente)
	elif isHospital(request.user):
		diagnostico = Diagnostico.objects.filter(medico__hospital=request.user.hospital)
	elif isMedico(request.user):
		diagnostico = Diagnostico.objects.filter(medico=request.user.medico)
		data['isMedico'] = True

	data['object_list'] = diagnostico
	return render(request, template_name, data)

@user_passes_test(isMedico, login_url='/login/')
def DeleteDiagnostico(request, pk):
	diagnostico = get_object_or_404(Diagnostico, id=pk)
	if diagnostico.medico == request.user.medico:
		diagnostico.delete()
		return redirect('list_diagnostico')
	return redirect('login')