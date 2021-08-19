from django.db import models
from django import forms


class Diario(models.Model):
    """Campo para escrever um diário"""
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..."


class DiarioForm(forms.ModelForm):
    class Meta:
        model = Diario
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
