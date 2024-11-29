from django.db import models
from django.utils import timezone

class Comments(models.Model):
    data = models.DateField(default=timezone.now)
    content_body = models.TextField()
    blog = models.ForeignKey('Content.Content', on_delete=models.CASCADE)
    # user = models.ForeignKey()


    def __str__(self):
        return f'Comment at {self.data}'


class M2MComentsTable(models.Model):
    blog = models.ForeignKey('Content.Content', on_delete=models.CASCADE)
    coment = models.ForeignKey(Comments, on_delete=models.CASCADE)