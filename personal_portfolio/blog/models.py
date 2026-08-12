from django.db import models

# Create your models here.
class Article(models.Model): #import from module 'models' that support database
    title = models.CharField (max_length=200)
    description  = models.TextField ()
    image = models.ImageField (upload_to='blog/images/')
    url = models.URLField (blank=True) # 'blank' allows to open page in the new page

    def __str__(self): #this func return name of an object when cursor is on
        return self.title