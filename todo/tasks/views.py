from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TaskForm

from .models import Task #deve importar para poder mandar para o site
# Create your views here.

#PASSOS = URL --> VIEWS --> TEMPLATE

def helloworld(request):
    return HttpResponse('hello world') #RETURN = SERVE PARA MANDAR A FUNÇÃO PARA O FRONT END ATRAVES DO RENDER

def tasklist(request):#sempre recebe o requeste
     tasks = Task.objects.all().order_by('-created_at') #PEGANDO TODOS OS OBJETOS DO BANCO DE DADOS//mandar as tasks do banco de dado para o template(site)//order_by('-created_at') ordenar os posts de mais novos para mais velhos
     return render(request, 'tasks/list.html', {'tasks' : tasks}) #dicionario que seleciona as tasks para mandar para o site

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)  #tenta pegar regitro no banco, se nao tiver reporta um erro 404(get_object_or_404)
    #pk = primary key
    return render(request, 'tasks/task.html', {'task': task})

def newTask(request):
    if request.method == 'POST': #ver se o request é post
        form = TaskForm(request.POST) #preencher o formulario com os dados do post

        if form.is_valid(): #se o post for valido
            task = form.save(commit=False) #começar a salvar a tarefa//commit=False = para o processo de iserção de dados e aguarda salvar
            task.done = 'doing'
            task.save()
            return redirect('/') #ao salvar a tarefa, returna para a pagina inicial ('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})

def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if(form.is_valid()):
            task.save()
            return redirect('/')

        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
            
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

def yourName(request, name): #receber o nome que o usuario vai digitar na url
    return render(request, 'tasks/yourname.html', {'name': name}) #construção de dicionario
