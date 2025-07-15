from django import forms 

class BasePaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()

class CrearPaletaFormulario(BasePaletaFormulario):
   ...
   
class EditarPaletaFormulario(BasePaletaFormulario):
    ...
    
class BusquedaPaletaFormulario(BasePaletaFormulario):  
    marca = forms.CharField(max_length=30, required=False)  


class BaseAutoFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()
    
class CrearAutoFormulario(BaseAutoFormulario):
   ...
   
class EditarAutoFormulario(BaseAutoFormulario):
    ...
    
class BusquedaAutoFormulario(BaseAutoFormulario):  
    marca = forms.CharField(max_length=30, required=False)      

class BaseMotoFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()

class CrearMotoFormulario(BaseMotoFormulario):
   ...
   
class EditarMotoFormulario(BaseMotoFormulario):
    ...
    
class BusquedaMotoFormulario(BaseMotoFormulario):  
    marca = forms.CharField(max_length=30, required=False)   
