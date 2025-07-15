from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from trineo.models import Trineo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ListadoTrineos(ListView):
    model = Trineo
    context_object_name = 'listado_de_trineos'
    template_name = 'trineo/trineos.html'
    
    
class CrearTrineos(LoginRequiredMixin, CreateView):
    model = Trineo
    template_name = 'trineo/crear_trineo.html'
    fields = ['marca', 'color', 'anio']
    success_url = reverse_lazy('trineos')
    
class EditarTrineos(LoginRequiredMixin, UpdateView):
    model = Trineo
    template_name = 'trineo/editar_trineo.html'
    fields = ['marca', 'color', 'anio']
    success_url = reverse_lazy('trineos')
    
class DetalleTrineos(DetailView):
    model = Trineo
    template_name = 'trineo/detalle_trineo.html'

class EliminarTrineos(LoginRequiredMixin, DeleteView):
    model = Trineo
    template_name = 'trineo/eliminar_trineo.html'
    success_url = reverse_lazy('trineos')