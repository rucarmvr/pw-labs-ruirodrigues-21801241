# Generated by Django 4.0.5 on 2022-06-06 02:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0026_outsystems'),
    ]

    operations = [
        migrations.AddField(
            model_name='outsystems',
            name='texto2',
            field=models.TextField(default=django.utils.timezone.now, max_length=20000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='outsystems',
            name='subtitulo',
            field=models.CharField(max_length=200),
        ),
    ]