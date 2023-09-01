from django.urls import path
from .views import home, words_list, add_word
urlpatterns = [
    path('', home),
    path('home/', home),
    path('words_list/', words_list, name='words_list'),
    path('add_word/', add_word, name='add_word'),
]


