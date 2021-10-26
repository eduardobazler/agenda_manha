from django.db import models


class Tarefa(models.Model):

    STATUS = (
        ('fazendo', 'Fazendo'),
        ('feita', 'Feita'),
    )

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    done = models.CharField(
        max_length=7,
        choices=STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
