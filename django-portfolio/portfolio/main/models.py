import os
from django.db import models
from django.conf import settings
#from django.templatetags.static import static
#from django.conf.urls.static import static

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    thumbnail = models.FilePathField(path=os.path.join(settings.STATIC_ROOT, 'main'))
    #thumbnail = models.FilePathField(path='/home/psetman/django-portfolio/portfolio/static/main')
    text = models.CharField(max_length = 4000)
    hyperlink = models.URLField(max_length = 200, blank=True)

    def __str__(self):
        return self.title

    @property
    def thumb_path(self):
        return self.thumbnail.replace(str(settings.BASE_DIR), '')