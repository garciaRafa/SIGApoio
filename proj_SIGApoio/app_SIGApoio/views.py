from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LocalForm, RecursoForm, TipoRecursoForm, ReservaForm
from .models import TipoRecurso, Recurso, Local, Reserva, Usuario, Horario
from .bo.horarios import converter_horarios
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json

def home(request):
    return render(request,'usuarios/home.html')  

def cad_local(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page') 
    else:
        form = LocalForm()
    return render(request, 'usuarios/cad_page.html', {'form': form})

def success_page(request):
    return render(request, 'usuarios/success_page.html')

def cadastroRecurso(request):
    if request.method != 'POST':
        form = RecursoForm()
    else:
        form = RecursoForm(request.POST)
        for i in Recurso.objects.all():
            if str(i.tipo) == TipoRecurso.objects.get(pk = form.data['tipo']).tipo and str(i.codigo) == str(form.data['codigo']):
                context = {'erro':'Recurso já cadastrado','form':form}
                return render(request, 'recurso/cadastro_recurso.html', context)
            
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cadastro-recurso'))
        
    context = {'form': form}
    return render(request, 'recurso/cadastro_recurso.html', context)

def cadastroTipoRecurso(request):
    if request.method != 'POST':
        form = TipoRecursoForm()
    else:
        form = TipoRecursoForm(request.POST)
        for i in TipoRecurso.objects.all():
            if str(i).lower() == form.data['tipo'].lower():
                context = {'erro':'Tipo de recurso já cadastrado','form':form}
                return render(request, 'recurso/cadastro_tipo_recurso.html', context)
                   
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cadastro-tipo-recurso'))
            
    context = {'form':form}
    return render(request, 'recurso/cadastro_tipo_recurso.html', context)

def cadastroReserva(request):
    if request.method != 'POST':
        form = ReservaForm()
        context = {'form': form}
        return render(request, 'reserva/cadastroReserva.html', context)
    else:
        req = request.POST
        form = ReservaForm()
        # try:
        context = {'form': form, 'message': 'Reserva cadastrada com sucesso!'}
        resp = Usuario.objects.get(matricula=req['matResponsavel'])
        solic = Usuario.objects.get(matricula=req['matSolicitante'])
        local = Local.objects.get(id=req['local'])
        horarios = Horario.objects.filter(id__in=req['horarios'])
        novaReserva = Reserva.objects.create(local=local, matResponsavel=resp, matSolicitante=solic)
        novaReserva.horarios.set(horarios)
        novaReserva.save()
        return render(request, 'reserva/cadastroReserva.html', context)
        # except:
        #     context = {'form': form, 'message': 'Erro no cadastro da reserva'}
        #     return render(request, 'reserva/cadastroReserva.html', context)
    
@csrf_exempt
def getLocais(request):
    data = json.loads(request.body)
    horarios = data['horarios']
    dias = data['dias']
    horarios_final = converter_horarios(dias, horarios)
    reservas_filt = Reserva.objects.filter(
        Q(horarios__id__in=horarios_final)
    )
    locais_ocupados = map(lambda reserva: reserva.local, reservas_filt)
    locais = Local.objects.exclude(
        Q(nome__in=locais_ocupados)
    )
    context = {'locais':locais}
    return render(request, 'reserva/local_option.html', context)