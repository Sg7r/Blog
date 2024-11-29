from django.db import models

class Images(models.Model):
    name = models.TextField()
    url = models.ImageField(upload_to='pictures/')
    size = models.CharField()

