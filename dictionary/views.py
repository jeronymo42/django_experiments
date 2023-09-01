from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
# Create your views here.

def home(request):
    context={'title':'My dictionary'}
    return render(request, 'main.html', context)

def words_list(request):
    if request.method == 'POST':
        with open("dictionary/file", "a", encoding="utf-8") as file:
            file.write(request.POST['word1'] + "-" + request.POST['word2'] + '\n')
    with open('dictionary/file', encoding="utf-8") as file:
        dictionary = [line.strip().split('-') for line in file.readlines()]
        context = {'dictionary': dictionary}
        return render(request, 'list.html', context)

def add_word(request):
    if request.method == 'POST':
        with open("dictionary/file", "a", encoding="utf-8") as file:
            file.write(request.POST['word1'] + "-" + request.POST['word2'] + '\n')
            return redirect('words_list')
    return render(request, 'new.html')