# Generated by Django 3.2.6 on 2021-09-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afirmacoes', '0002_afirmacao_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='afirmacao',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]