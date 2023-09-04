from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'reg.html', {'title':'Регистрация'})

def login(request):
    return render(request, 'login.html', {'title':'Вход'})

def notes(request):
    note_list = ['Заметка 1', 'Заметка 2', 'Заметка 3', 'Заметка 4', 'Заметка 5']
    return render(request, 'notes.html', {'title':'Заметки', 'notes': note_list})