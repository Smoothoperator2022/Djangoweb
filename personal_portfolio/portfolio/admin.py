from django.contrib import admin

# Register your models here.
from .models import Project # from current folder.file'models' import class Project

admin.site.register(Project) #register models we want to see in admin - this adds new section 'Project'