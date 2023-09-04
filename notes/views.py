from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'reg.html', {'title':'Регистрация'})

def login(request):
    return render(request, 'login.html', {'title':'Вход'})