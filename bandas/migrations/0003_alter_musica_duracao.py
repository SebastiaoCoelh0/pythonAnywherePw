# Generated by Django 5.0.6 on 2024-06-08 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0002_banda_banda_ativa_banda_lancamento_primeiro_album_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='duracao',
            field=models.CharField(max_length=6),
        ),
    ]