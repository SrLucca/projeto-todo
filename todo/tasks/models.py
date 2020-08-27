from django.db import models

# Create your models here.
#SEMRPE QUE CRIAR UM MODEL REGISTRAR NO ADMIN.PY
#DEPOIS DE CRIAR TUDO DAR MAKEMIGRATION E MIGRATE PARA APLICAR AO BANCO DE DADOS
STATUS = (
    ('doing', 'Doing'),
    ('done', 'Done'),
)

class Task(models.Model): #comportara os campos da tabela que o django criara com o migration
    #campos que serão inseridos na tabela

    title = models.CharField(max_length=255) #Charfield = campo de caracteres(char) = leva argumento obrigatorio//#maxlenght = maximo de caracteres no title
    description = models.TextField() #TextField = campo para texto maiores = nao leva argumento obrigatorio
    done = models.CharField( #se o registro ta pronta ou nao(0 ou 1)
        max_length=5,
        choices = STATUS, #possiveis escolhas(choices) para o select
    )
    created_at = models.DateTimeField(auto_now_add=True) #data do registro // auto_now_add=True = atualiza o banco de dados sempre que um registro for feito
    updated_at = models.DateTimeField(auto_now=True) #atualiza o regisstro quando for alterado

    def __str__(self):
        return self.title #para mostrar o nome da tarefa no admin alem de "TASK OBJECT"