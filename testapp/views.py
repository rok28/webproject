import json

from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


def get_example(request):
    response = "Hola"
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


@csrf_exempt
def post_example(request):
    response = {'request': {'time': datetime.now().isoformat(),
                            'method': request.method,
                            'path': request.path,
                            'params': request.GET,
                            'headers': dict(request.headers),
                            'body': request.body.decode()}}
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


def gallery(request):
    return render(request, 'testapp/gallery.html')


def gallery_photo(request, photo):
    context = {'photo': photo}
    return render(request, 'testapp/gallery_photo.html', context)


@csrf_exempt
def sumar(request):
    ayb = json.loads(request.body.decode())
    a = ayb["a"]
    b = ayb["b"]

    response = int(a) + int(b)
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


@csrf_exempt
def restar(request):
    ayb = json.loads(request.body.decode())
    a = ayb["a"]
    b = ayb["b"]

    response = int(a) - int(b)
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


@csrf_exempt
def multiplicar(request):
    ayb = json.loads(request.body.decode())
    a = ayb["a"]
    b = ayb["b"]

    response = int(a) * int(b)
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


@csrf_exempt
def dividir(request):
    ayb = json.loads(request.body.decode())
    a = ayb["a"]
    b = ayb["b"]

    response = int(a) / int(b)
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})

