from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'reg.html', {'title':'Регистрация'})