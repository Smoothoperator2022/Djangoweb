from django.db import models

# Create your models here.

class Project(models.Model): #import from module 'models' that support database
    title = models.CharField (max_length=100)
    description  = models.CharField (max_length=250)
    image = models.ImageField (upload_to='portfolio/images/')
    url = models.URLField (blank=True) # 'blank' allows to open page in the new page

    def __str__(self): #this func return name of an object when cursor is on
        return self.title

