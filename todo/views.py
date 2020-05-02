from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import AddForm

def todo_view(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
           form.save()

    todos = Todo.objects.all()
    form = AddForm()
    data = {
        "todos" : todos,
        "form" : form,
    }

    return render(request, "todo_list.html", data)


def todo_progress_view(request):
    todos = Todo.objects.exclude(is_done=True)
    data = {
        "todos":todos,
    }

    return render(request, "todo_in_progress.html", data)

def delete_todo(request, pk):
    target = Todo.objects.get(pk=pk)
    target.delete()
    return redirect("todos")

def done_todo(request, pk):
    target = Todo.objects.get(pk=pk) #todo에서 pk 가pk인것을 가져와서
    target.is_done = True #is_done이 false이면 true로 바꿔라
    target.save()
    return redirect("todos")
           

# def done_todo(request, pk) 이하를 아래와 같이 쓰면 동작하지 않는 이유가 궁금합니다.
#if target.is_done==False:   #is_done이 false이면 true로 바꿔라
#        target.is_done==True
#        target.save()
#          print(target.is_done)
        
