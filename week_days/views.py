from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

dict_day = {
    'monday': 'День недели - Понедельник. Это первый день недели.',
    'tuesday': 'День недели - Вторник. Это второй день недели.',
    'wednesday': 'День недели - Среда. Это третий день недели.',
    'thursday': 'День недели - Четверг. Это четвертый день недели.',
    'friday': 'День недели - Пятница. Это пятый день недели.',
    'saturday': 'День недели - Суббота. Это шестой день недели.',
    'sunday': 'День недели - Воскресенье. Это седьмой день недели.',

}


def get_days_week(request, get_day: str):
    day = dict_day.get(get_day, None)
    if day:
        return HttpResponse(f'День недели - {day}. Это первый день недели.')
    else:
        return HttpResponseNotFound(f'День недели {get_day} не найден')


def get_days_week_numb(request, get_day: int):
    days = list(dict_day)
    if get_day > len(days):
        return HttpResponseNotFound(f'День недели {get_day} не обнаружен.')
    else:
        day = days[get_day-1]
        return HttpResponseRedirect(f'/week_days/{day}')

