# Generated by Django 4.0.5 on 2022-06-06 15:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0029_remove_laboratorio_texto_laboratorio_disciplina_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='laboratorio',
            name='texto',
            field=models.TextField(default=django.utils.timezone.now, max_length=16620),
            preserve_default=False,
        ),
    ]
