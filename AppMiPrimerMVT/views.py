from json import load
from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import Context, Template, loader
# Create your views here.

def familiares(request):
    familia1=Familiares(nombre="Guillermo", edad=64, fecha_de_nacimiento="1957-10-01")
    familia1.save()
    familia2=Familiares(nombre="Patricia", edad=68, fecha_de_nacimiento="1954-09-13")
    familia2.save()
    familia3=Familiares(nombre="Mercedes", edad=38, fecha_de_nacimiento="1983-11-11")
    familia3.save()
    texto=f"Familiar 1: nombre: {familia1.nombre} edad: {familia1.edad} fecha de nacimiento: {familia1.fecha_de_nacimiento}.  Familiar 2: nombre: {familia2.nombre} edad: {familia2.edad} fecha de nacimiento: {familia2.fecha_de_nacimiento} Familiar 3: nombre: {familia3.nombre} edad:{familia3.edad} fecha de nacimiento: {familia3.fecha_de_nacimiento}"
    return HttpResponse (texto)
def template(request):
    plantilla=loader.get_template('template1.html')
    contexto=Context()
    documento=plantilla.render(contexto)
    return HttpResponse (documento)

