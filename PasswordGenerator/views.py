from django.shortcuts import render
import random
import string
# Create your views here.


def passHome(request):
    return render(request,'pass.html')

def passGen(request):
    length = int(request.GET.get('length', 12))
    up = request.GET.get('up', 0)
    num = request.GET.get('num', 0)
    sp = request.GET.get('sp', 0)
    chars = string.ascii_lowercase
    if up:
        chars += string.ascii_uppercase
    if num:
        chars += string.digits
    if sp:
        chars += string.punctuation
    urPassword = ''.join(random.choices(chars, k=length))
    params = {'password': urPassword}
    return render(request,'generated.html', params)