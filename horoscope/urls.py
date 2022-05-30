from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:sing_zodiac>', views.get_info_sing_zodiac_numb),
    path('<str:sing_zodiac>', views.get_info_sing_zodiac),
]