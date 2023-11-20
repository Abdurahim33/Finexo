from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from main.models import Home, About, Service, Why, Team


class Home(ListView):
    model = Home
    template_name = 'layouts/index.html'

class About(ListView):
    model = About
    template_name = 'layouts/about.html'


class Service(ListView):
    model = Service
    template_name = 'layouts/service.html'


class Why(ListView):
    model = Why
    template_name = 'layouts/why.html'



class Team(ListView):
    model = Team
    template_name = 'layouts/team.html'