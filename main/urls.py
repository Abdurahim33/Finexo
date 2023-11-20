from django.urls import path
from main.views import Home, About, Service, Why, Team


urlpatterns = [
    path('Home/', Home.as_view(), name='home'),
    path('About/', About.as_view(), name='about'),
    path('Service/', Service.as_view(), name='Service'),
    path('Why/', Why.as_view(), name='why'),
    path('team/', Team.as_view(), name='team')
]


