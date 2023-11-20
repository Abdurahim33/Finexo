from django.contrib import admin
from main.models import Home, About, Service, Why, Team

@admin.register(Home)
class Home(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'title2', 'icons')
    list_display_links = ('title', 'sub_title', 'title2', 'icons')



@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('title', 'main_title', 'sub_title')
    list_display_links = ('title', 'main_title', 'sub_title')

@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display = ('title', 'icon', 'icon_title')
    list_display_links = ('title', 'icon', 'icon_title')


@admin.register(Why)
class Why(admin.ModelAdmin):
    list_display = ('title', 'icon', 'sub_title')
    list_display_links = ('title', 'icon')


@admin.register(Team)
class Team(admin.ModelAdmin):
    list_display = ('image', 'title')
    list_display_links = ('image', 'title')