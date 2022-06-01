from django.shortcuts import render
from portfolio.models import Projetos, Home, Home_Web, Web


def home_page_view(request):
    context = {'home': Home.objects.all()}
    return render(request, 'portfolio/home.html', context)


def home_web_page_view(request):
    context = {'home_web': Home_Web.objects.all()}
    return render(request, 'portfolio/home.html', context)


def web_page_view(request):
    context = {'web': Web.objects.all()}
    return render(request, 'portfolio/web.html', context)


def about_page_view(request):
    return render(request, 'portfolio/about.html')


def projects_page_view(request):
    context = {'projects': Projetos.objects.all()}
    return render(request, 'portfolio/projects.html', context)


def contact_page_view(request):
    return render(request, 'portfolio/contact.html')


def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')


def blog_page_view(request):
    return render(request, 'portfolio/blog.html')

