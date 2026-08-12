from django.shortcuts import render
from .models import Project


# Create your views here.
def homepage(request):
    projects = Project.objects.all() #in such way Django imports all data from database - return list
    return render(request, 'portfolio/homepage.html', {'projects': projects})
