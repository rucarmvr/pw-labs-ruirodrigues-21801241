# Generated by Django 4.0.5 on 2022-06-06 02:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0024_laboratorio_alter_outras_habilitacoes_texto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='web',
            name='url',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
