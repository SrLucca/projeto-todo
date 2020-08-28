from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Task #deve importar para poder mandar para o site
# Create your views here.

def helloworld(request):
    return HttpResponse('hello world')

def tasklist(request):#sempre recebe o requeste
     tasks = Task.objects.all() #PEGANDO TODOS OS OBJETOS DO BANCO DE DADOS//mandar as tasks do banco de dado para o template(site)
     return render(request, 'tasks/list.html', {'tasks' : tasks}) #dicionario que seleciona as tasks para mandar para o site

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)  #tenta pegar regitro no banco, se nao tiver reporta um erro 404(get_object_or_404)
    #pk = primary key
    return render(request, 'tasks/task.html', {'task': task})

def yourName(request, name): #receber o nome que o usuario vai digitar na url
    return render(request, 'tasks/yourname.html', {'name': name}) #construção de dicionario
