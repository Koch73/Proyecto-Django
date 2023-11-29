from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template import loader

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    
    
#primera vista
def saludo(request):
    p1 = Persona("David", "Koch")
    temas = ["hola", "como", "estas?"]
    fecha_actual = datetime.datetime.now()
    doc_externo = loader.get_template("plantilla.html")
   
    ctx = {"nombre":p1.nombre, "apellido": p1.apellido, "fecha": fecha_actual,"temas": temas}
    
    doc = doc_externo.render(ctx)
    
    return HttpResponse(doc)