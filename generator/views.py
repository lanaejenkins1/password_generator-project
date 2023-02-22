import random

from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': '123456'}, )
    # return HttpResponse('Hello there friend!')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    # get length from request and convert to int and have default value 12
    length = int(request.GET.get('length'), 12)

    if request.GET.get('uppercase') == 'on':
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers') == 'on':
        characters.extend(list('0123456789'))
    if request.GET.get('special') == 'on':
        characters.extend(list('!@#$%^&*()_+=-[]{}|;":<>,./?'))
    thePassword = ''
    # generate password
    for x in range(length):
        thePassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thePassword})


def about(request):
    return render(request, 'generator/about.html')

# TODO: make about page - how made this work new url path/template and view w/ link
