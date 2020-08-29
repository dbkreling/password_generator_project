from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    length=int(request.GET.get('length', 12))
    possible_options = list('abcdefghijklmnopqrstuvwxyz')
    the_passoword=''

    if request.GET.get('uppercase'):
        possible_options.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        possible_options.extend('1234567890')
    if request.GET.get('special'):
        possible_options.extend('!@#$%&^~?*()')

    for x in range(length):
        the_passoword += random.choice(possible_options)

    return render(request, 'generator/password.html', {'password':the_passoword})
