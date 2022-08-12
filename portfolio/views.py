from django.shortcuts import render
from .models import Project


def home(request):
    """Собираем все объекты модели и отображаем на странице"""
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
