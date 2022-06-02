from django.contrib import admin
from .models import Projetos, Home, Home_Web, Web, Licenciatura, About

# register

admin.site.register(Home)
admin.site.register(Home_Web)
admin.site.register(Projetos)
admin.site.register(Web)
admin.site.register(Licenciatura)
admin.site.register(About)
