from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    fields = ['logo', 'trade_mark', 'title', 'slogan']


admin.site.register([User, Statistics])
