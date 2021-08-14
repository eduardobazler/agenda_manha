from django import forms
from django.db import models


class Afirmacao(models.Model):
    """ ecreva suas afirmações com determinado tema"""
    titulo = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..."


class AfirmacaoForm(forms.ModelForm):
    class Meta:
        model = Afirmacao
        fields = ['titulo', 'text']
        labels = {'titulo': '', 'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
