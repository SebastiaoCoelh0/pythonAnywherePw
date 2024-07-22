# Generated by Django 5.0.6 on 2024-07-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_alter_docente_disciplinas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='ano',
            field=models.IntegerField(choices=[(1, '1º Ano'), (2, '2º Ano'), (3, '3º Ano')]),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='semestre',
            field=models.CharField(choices=[('1º Semestre', '1º Semestre'), ('2º Semestre', '2º Semestre'), ('Anual', 'Anual')], max_length=20),
        ),
    ]
