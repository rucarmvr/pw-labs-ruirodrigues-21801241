from django.contrib import admin

from .models import Projetos, Home_projets, Home_Web, Web, About, Educacao, Certificados, Interesses_hobbies, \
    Licenciatura

# register

admin.site.register(Home_projets)
admin.site.register(Home_Web)
admin.site.register(Projetos)
admin.site.register(Web)
admin.site.register(Licenciatura)
admin.site.register(About)
admin.site.register(Educacao)
admin.site.register(Certificados)
admin.site.register(Interesses_hobbies)
