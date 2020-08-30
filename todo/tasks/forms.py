from django import forms

from .models import Task #molde do formulario//respeita os campos do formulario

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title' , 'description')
