from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
# Create your views here.
def usuarios(request):
    sql ="SELECT  nombre,usuario FROM usuario "
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()
    return render(request,'Organigrama/index.php',{'resultados': resultados})
