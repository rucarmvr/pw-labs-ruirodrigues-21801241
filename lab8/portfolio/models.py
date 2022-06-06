from django.db import models
from django.urls import reverse

save_as = True


class Home_Web(models.Model):
    logo = models.ImageField(upload_to='image', null=True)
    titulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=200)
    url = models.CharField(max_length=250)


class Web(models.Model):
    logo = models.ImageField(upload_to='image', null=True)
    titulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=200)


class Home_projets(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=200)
    url = models.CharField(max_length=250)
    image = models.ImageField(upload_to='image', null=True)


class Projetos(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image', null=True)


class Licenciatura(models.Model):
    link = models.URLField(max_length=120)
    disciplina = models.CharField(max_length=120)
    semestre = models.CharField(max_length=200)
    ect = models.IntegerField(default=5)


class About(models.Model):
    logo = models.ImageField(upload_to='image', null=True)
    titulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=50)
    url = models.CharField(max_length=250)


class Educacao(models.Model):
    logo = models.ImageField(upload_to='image', null=True)
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    texto = models.TextField(max_length=200)


class Certificados(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    texto = models.TextField(max_length=20000)


class Interesses_hobbies(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=200)


class Outras_habilitacoes(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=200)
