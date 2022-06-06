from django.db import models

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
    url = models.CharField(max_length=250)


class Home_projets(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=200)
    url = models.CharField(max_length=250)
    image = models.ImageField(upload_to='image', null=True)


class Projetos(models.Model):
    titulo = models.CharField(max_length=202)
    subtitulo = models.CharField(max_length=204)
    texto = models.TextField(max_length=20000)
    image = models.ImageField(upload_to='image', null=True)
    url = models.CharField(max_length=250)


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


class Laboratorio(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=20)
    link = models.URLField(max_length=120)
    disciplina = models.CharField(max_length=120)
    texto = models.TextField(max_length=16620)


class Outras_Habilitacoes(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=20)
    texto = models.TextField(max_length=20000)


class OutSystems(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    texto = models.TextField(max_length=20000)
    texto2 = models.TextField(max_length=20000)
    url = models.CharField(max_length=250)
