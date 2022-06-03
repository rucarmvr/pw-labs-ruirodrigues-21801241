from django.shortcuts import render
from portfolio.models import Projetos, Home, Home_Web, Web, Licenciatura, About, Educacao, Certificados, \
    Interesses_hobbies


def home_page_view(request):
    context = {'home': Home.objects.all(), 'home_web': Home_Web.objects.all()}
    return render(request, 'portfolio/home.html', context)


def web_page_view(request):
    context = {'web': Web.objects.all()}
    return render(request, 'portfolio/web.html', context)


def about_page_view(request):
    context = {'about': About.objects.all()}
    return render(request, 'portfolio/about.html', context)


def projects_page_view(request):
    context = {'projects': Projetos.objects.all()}
    return render(request, 'portfolio/projects.html', context)


def contact_page_view(request):
    return render(request, 'portfolio/contact.html')


def licenciatura_page_view(request):
    context = {'licenciatura': Licenciatura.objects.all()}
    return render(request, 'portfolio/licenciatura.html', context)


def blog_page_view(request):
    return render(request, 'portfolio/blog.html')


def educacao_page_view(request):
    context = {'educacao': Educacao.objects.all()}
    return render(request, 'portfolio/educacao.html', context)


def certificados_page_view(request):
    context = {'certificados': Certificados.objects.all()}
    return render(request, 'portfolio/certificados.html', context)


def interesses_hobbies_page_view(request):
    context = {'interesses_hobbies': Interesses_hobbies.objects.all()}
    return render(request, 'portfolio/interesses_hobbies.html', context)
