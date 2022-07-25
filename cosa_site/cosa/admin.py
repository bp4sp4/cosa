from django.contrib import admin
from .models import Pmain

class PmainAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Pmain, PmainAdmin)

