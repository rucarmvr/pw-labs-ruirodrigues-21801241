# Generated by Django 4.0.5 on 2022-06-03 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_about_alter_home_subtitulo_alter_home_texto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=200)),
                ('texto', models.CharField(max_length=200000000)),
            ],
        ),
    ]