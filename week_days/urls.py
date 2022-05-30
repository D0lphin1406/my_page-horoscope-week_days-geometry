from . import views
from django.urls import path

urlpatterns = [
    path('<int:get_day>', views.get_days_week_numb),
    path('<str:get_day>', views.get_days_week),
]