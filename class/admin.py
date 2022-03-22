from django.contrib import admin

from .models import Business,Professional,User

# Register your models here.
admin.site.register(Business)
admin.site.register(Professional)
admin.site.register(User)
