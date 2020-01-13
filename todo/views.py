from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from .models import todo


def addtodo(request):
    if(request.POST['content']!=''):
        new = todo(content=request.POST['content'],name=request.POST['name'])
        new.save()
    return HttpResponseRedirect('/todo/')

def deletetodo(request,tdo_id):
    a=todo.objects.get(id=tdo_id)
    a.delete()
    return HttpResponseRedirect('/todo/')

def add(request):
    a=todo.objects.all()
    return render(request, 'todo/tod.html', {'a': a})


