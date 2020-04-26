from django.shortcuts import render
from django.http import HttpResponse # 장고의  http 폴더에서 HttpResponse 함수를 import

# Create your views here.

def home_view(request):
    return HttpResponse("<p>Hello World!</p>")