from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    length=12
    possible_options = list('abcdefghijklmnopqrstuvwxyz')
    the_passoword=''

    for x in range(length):
        the_passoword += random.choice(possible_options)

    return render(request, 'generator/password.html', {'password':the_passoword})
