# Generated by Django 5.0.6 on 2024-07-22 16:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0004_utilizador_email'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilizador',
            name='data_nascimento',
        ),
        migrations.RemoveField(
            model_name='utilizador',
            name='email',
        ),
        migrations.RemoveField(
            model_name='utilizador',
            name='nome',
        ),
        migrations.AddField(
            model_name='utilizador',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='utilizador',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]