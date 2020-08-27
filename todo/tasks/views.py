from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def helloworld(request):
    return HttpResponse('hello world')

def tasklist(request):#sempre recebe o requeste
     return render(request, 'tasks/list.html')

def yourName(request, name): #receber o nome que o usuario vai digitar na url
    return render(request, 'tasks/yourname.html', {'name': name}) #construção de dicionario