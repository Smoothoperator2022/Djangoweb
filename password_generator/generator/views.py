from django.shortcuts import render #'render' func allows to execute html from templates
from django.http import HttpResponse
import random

# Create your views here.

def home(request): #request from server
    return render (request, 'generator/home.html')

def password(request):

    characters = list ('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get ('uppercase'): #
        characters.extend(list ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))  #add need list of capitalized symbols

    if request.GET.get ('special'): #
        characters.extend(list ('!@#$%^&*()_+-='))

    if request.GET.get ('numbers'): #
        characters.extend(list ('1234567890'))

    length = int (request.GET.get('length', 12)) #will take value from home.select and we can change it
    # quantity of symbols in page`s url above, '12'-default quantity

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render (request, 'generator/password.html', {'password':thepassword})

def about(request): #request from server
    return render (request, 'generator/about.html')