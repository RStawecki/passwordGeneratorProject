from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    numbers ='0123456789'
    lowerLetters = 'abcdefghijklmnoprstuwxyz'
    upperLetters = lowerLetters.upper()
    specialCharacters = '!@#$%^&*'
    listAllCharacters = list(lowerLetters)

    if request.GET.get("upper"):
        listAllCharacters += list(upperLetters)
    if request.GET.get("specials"):
        listAllCharacters += list(specialCharacters)
    if request.GET.get("numbers"):
        listAllCharacters += list(numbers)

    length = int(request.GET.get("length"))
    password = ''
    for _ in range(length):
        el = random.choice(listAllCharacters)
        password += el
    
    return render(request, 'generator/password.html', {'password': password})