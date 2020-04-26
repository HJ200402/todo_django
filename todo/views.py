from django.shortcuts import render
from django.http import HttpResponse # 장고의  http 폴더에서 HttpResponse 함수를 import
from .models import Todo

# Create your views here.

def todo_view(request):
    todos = Todo.objects.all()
    data = {
        "todos": todos,
    }

    return render(request, "todo_list.html", data)


def todo_progress_view(request):
    todos = Todo.objects.exclude(is_done=True)
    data = {
        "todos":todos,
    }

    return render(request, "todo_in_progress.html",data)