from django.shortcuts import render
from .models import organigrama
from django.db import connection
from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

# Create your views here.
""" class CustomView(TemplateView):
    pass """



""" usuario = CustomView.as_view(template_name="index.php") """

def usuarios(request):
    template = loader.get_template('Sistemas/index.php')
    usuarios = organigrama.objects.all() 
    context = {
        'Organigrama':organigrama
    }
    sql ="SELECT nombre,usuario FROM usuario"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    
    """ return HttpResponse(template.render(context,request,{'resultados':resultados})) """
    return render(request,'Sistemas/index.php',{'resultados': resultados})

