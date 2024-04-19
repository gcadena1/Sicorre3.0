from django.shortcuts import render
from django.db import connection
from django.template import loader
from django.http import HttpResponse
from .models import organigrama

""" def usuarios(request):
    usuarios = organigrama.objects.all()
    sql = "SELECT * FROM usuario"
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
    return render(request,'miTemplate.php',{'organigrama':result}) """

def usuarios(request):
  reports = organigrama.objects.all()
  template = loader.get_template('miTemplate.php')
  context = {
        'organigrama':organigrama
        }
  return render(request,'miTemplate.php')