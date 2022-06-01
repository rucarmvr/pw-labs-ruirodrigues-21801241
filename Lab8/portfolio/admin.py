from django.contrib import admin
from .models import Projetos, Home, Home_Web, Web

# register

admin.site.register(Home)
admin.site.register(Home_Web)
admin.site.register(Projetos)
admin.site.register(Web)
