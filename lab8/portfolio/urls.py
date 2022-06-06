from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('about', views.about_page_view, name='about'),
    path('projects', views.projects_page_view, name='projects'),
    path('web', views.web_page_view, name='web'),
    path('contact', views.contact_page_view, name='contact'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('blog', views.blog_page_view, name='blog'),
    path('educacao', views.educacao_page_view, name='educacao'),
    path('certificados', views.certificados_page_view, name='certificados'),
    path('interesses_hobbies', views.interesses_hobbies_page_view, name='interesses_hobbies'),
    path('fisica', views.fisica_page_view, name='fisica'),
    path('outras_habilitacoes', views.outras_habilitacoes_page_view, name='outras_habilitacoes'),
    path('laboratorio', views.laboratorio_page_view, name='laboratorio'),
    path('outsystems', views.outsystems_page_view, name='outsystems'),
    path('view-pdf', views.pdf_page_view, name='pdf_view'),
]
