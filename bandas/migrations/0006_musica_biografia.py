# Generated by Django 4.0.6 on 2024-07-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0005_musica_letra'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='biografia',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
