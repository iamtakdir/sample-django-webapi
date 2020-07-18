from django.contrib import admin
from .models import*

class Name_Admin(admin.ModelAdmin):
    list_display=('id' , 'name')

class Member_Admin(admin.ModelAdmin):
    list_display = ('name', 'designation')

admin.site.register(Name,Name_Admin)
admin.site.register(Member,Member_Admin)
