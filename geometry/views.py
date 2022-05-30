from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Площадь прямоугольника размером {width}х{height} равна {width * height}')


def get_square_area(request, width: int):
    return HttpResponse(f'Площадь квадрата размером {width}х{width} равна {width * width}')


def get_circle_area(request, radius: int):
    return HttpResponse(f'Площадь круга с радиусом {radius} равна {2 * 3.14 * radius ** 2}')


def lite_name_rectangle(request, width, height):
    return HttpResponseRedirect(f'/calculate_geometry/get_rectangle_area/{width}/{height}')

def lite_name_square(request, width: int):
    return HttpResponseRedirect(f'/calculate_geometry/get_square_area/{width}')

def lite_name_circle(request, radius: int):
    return HttpResponseRedirect(f'/calculate_geometry/get_circle_area/{radius}')