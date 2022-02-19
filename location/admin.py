from django.contrib import admin

from location.models import State, LGA

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'zone']


@admin.register(LGA)
class LGAAdmin(admin.ModelAdmin):
    list_display = ['state', 'name']