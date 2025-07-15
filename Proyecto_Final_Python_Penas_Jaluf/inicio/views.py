from django.shortcuts import render, redirect
from inicio.models import Paleta, Auto, Moto
from inicio.forms import CrearPaletaFormulario, CrearMotoFormulario, CrearAutoFormulario, EditarPaletaFormulario, EditarAutoFormulario, EditarMotoFormulario
from django.contrib.auth.decorators import login_required


def inicio(request):
    
    return render(request, 'inicio/inicio.html', {})


def paletas(request):
    
    marca_a_buscar = request.GET.get('marca')    
    
    if marca_a_buscar:
        listado_de_paletas = Paleta.objects.filter(marca__icontains = marca_a_buscar)
    else:
        listado_de_paletas = Paleta.objects.all()

    
    return render(request, 'inicio/paletas.html', {'listado_de_paletas': listado_de_paletas})

def autos(request):
    
    marca_a_buscar = request.GET.get('marca')    
    
    if marca_a_buscar:
        listado_de_autos = Auto.objects.filter(marca__icontains = marca_a_buscar)
    else:
        listado_de_autos = Auto.objects.all()

    
    return render(request, 'inicio/autos.html', {'listado_de_autos': listado_de_autos})

def motos(request):
    
    marca_a_buscar = request.GET.get('marca')    
    
    if marca_a_buscar:
        listado_de_motos = Moto.objects.filter(marca__icontains = marca_a_buscar)
    else:
        listado_de_motos = Moto.objects.all()

    
    return render(request, 'inicio/motos.html', {'listado_de_motos': listado_de_motos})

@login_required
def crear_paleta(request):
    
    if request.method == 'POST' :
        formulario = CrearPaletaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            
            paleta = Paleta(marca=marca.lower(), descripcion=descripcion, anio=anio)
            paleta.save()
            
            return redirect('paletas')
        
        else:
            return render(request, 'inicio/crear_paleta.html', {'formulario' : formulario})
    
    formulario = CrearPaletaFormulario()
    return render(request, 'inicio/crear_paleta.html', {'formulario' : formulario})

@login_required
def crear_auto(request):
    
    if request.method == 'POST' :
        formulario = CrearAutoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            modelo = info_limpia.get('modelo')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            
            auto = Auto(marca=marca.lower(), modelo=modelo ,descripcion=descripcion, anio=anio)
            auto.save()
            
            return redirect('autos')
        
        else:
            return render(request, 'inicio/crear_autos.html', {'formulario' : formulario})
    
    formulario = CrearAutoFormulario()
    return render(request, 'inicio/crear_auto.html', {'formulario': formulario})

@login_required
def crear_moto(request):

    if request.method == 'POST' :
        formulario = CrearMotoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            
            moto = Moto(marca=marca.lower(), descripcion=descripcion, anio=anio)
            moto.save()
            
            return redirect('motos')
        
        else:
            return render(request, 'inicio/crear_moto.html', {'formulario' : formulario})
    
    formulario = CrearMotoFormulario()
    return render(request, 'inicio/crear_moto.html', {'formulario' : formulario})

@login_required
def eliminar_paleta(request, paleta_id):
    paleta_a_eliminar = Paleta.objects.get(id=paleta_id)
    paleta_a_eliminar.delete()
    
    return redirect('paletas')

@login_required 
def editar_paleta(request, paleta_id):
    paleta_a_editar = Paleta.objects.get(id=paleta_id)
    
    if request.method == 'POST':
        formulario = EditarPaletaFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            paleta_a_editar.marca = info_nueva.get('marca')
            paleta_a_editar.descripcion = info_nueva.get('descripcion')
            paleta_a_editar.anio = info_nueva.get('anio')
            
            paleta_a_editar.save()
            return redirect ('paletas')
        return render(request, 'inicio/editar_paleta.htmls', {'formulario': formulario})
    
    
    formulario = EditarPaletaFormulario(initial={'marca': paleta_a_editar.marca, 'descripcion': paleta_a_editar.descripcion, 'anio': paleta_a_editar.anio})
    return render(request, 'inicio/editar_paleta.html', {'formulario': formulario})

def detalle_paleta(request, paleta_id):
    paleta = Paleta.objects.get(id=paleta_id)
    
    return render(request,'inicio/detalle_paleta.html', {'paleta' : paleta})

def eliminar_auto(request, auto_id):
    auto_a_eliminar = Auto.objects.get(id=auto_id)
    auto_a_eliminar.delete()
    
    return redirect('autos')

@login_required 
def editar_auto(request, auto_id):
    auto_a_editar = Auto.objects.get(id=auto_id)
    
    if request.method == 'POST':
        formulario = EditarAutoFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            auto_a_editar.marca = info_nueva.get('marca')
            auto_a_editar.descripcion = info_nueva.get('descripcion')
            auto_a_editar.anio = info_nueva.get('anio')
            
            auto_a_editar.save()
            return redirect ('autos')
        return render(request, 'inicio/editar_auto.htmls', {'formulario': formulario})
    
    
    formulario = EditarAutoFormulario(initial={'marca': auto_a_editar.marca, 'descripcion': auto_a_editar.descripcion, 'anio': auto_a_editar.anio})
    return render(request, 'inicio/editar_auto.html', {'formulario': formulario})

def detalle_auto(request, auto_id):
    auto = Auto.objects.get(id=auto_id)
    
    return render(request,'inicio/detalle_auto.html', {'auto' : auto})

def eliminar_moto(request, moto_id):
    moto_a_eliminar = Moto.objects.get(id=moto_id)
    moto_a_eliminar.delete()
    
    return redirect('motos')

@login_required 
def editar_moto(request, moto_id):
    moto_a_editar = Moto.objects.get(id=moto_id)
    
    if request.method == 'POST':
        formulario = EditarMotoFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            moto_a_editar.marca = info_nueva.get('marca')
            moto_a_editar.descripcion = info_nueva.get('descripcion')
            moto_a_editar.anio = info_nueva.get('anio')
            
            moto_a_editar.save()
            return redirect ('motos')
        return render(request, 'inicio/editar_moto.htmls', {'formulario': formulario})
    
    
    formulario = EditarMotoFormulario(initial={'marca': moto_a_editar.marca, 'descripcion': moto_a_editar.descripcion, 'anio': moto_a_editar.anio})
    return render(request, 'inicio/editar_moto.html', {'formulario': formulario})

def detalle_moto(request, moto_id):
    moto = Moto.objects.get(id=moto_id)
    
    return render(request,'inicio/detalle_moto.html', {'moto' : moto})


def about_me(request):
    return render(request, 'inicio/about_me.html')

