from django.contrib.auth.models import User
from django.db import models

save_as = True


class Home_Web(models.Model):
    logo = models.ImageField(upload_to='image', null=True)
    titulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=200)


class Home(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image', null=True)


class Projetos(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image', null=True)


class Web(models.Model):
    logo = models.ImageField(upload_to='image', null=True)
    titulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=200)
