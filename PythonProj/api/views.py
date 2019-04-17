from django.shortcuts import render
from django.http import JsonResponse
from .utils import math

def add(request):
    res = math.add(int(request.GET["num1"]), int(request.GET["num2"]))
    return JsonResponse({
        "result": res
    })

def minus(request):
    res = math.minus(int(request.GET["num1"]), int(request.GET["num2"]))
    return JsonResponse({
        "result": res
    })

