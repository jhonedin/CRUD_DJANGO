from django.shortcuts import render
from .models import Curso
# Create your views here.
def home(request):
    cursos_listado = Curso.objects.all()
    return render(request, "gestionCursos.html",{"cursos": cursos_listado})
