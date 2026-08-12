from django.contrib import admin

# Register your models here.
from .models import Article # from current folder.file'models' import class Project

admin.site.register(Article)