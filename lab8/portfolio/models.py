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


class Home(models.Model):
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
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    texto = models.TextField()
    texto2 = models.TextField()
    texto3 = models.TextField()
    texto4 = models.TextField()


class About(models.Model):
    logo = models.ImageField(upload_to='image', null=True)
    titulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=200)


class Educacao(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=200)


class Certificados(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=200)


class Interesses_hobbies(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=200)
