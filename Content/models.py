from django.db import models
from django.utils import timezone
from Images.models import Images
from Comments.models import Comments
# from Images import Images
from django import forms

class Content(models.Model):
    content = models.TextField()
    data = models.DateField(default=timezone.now)
    image = models.ForeignKey('Images.Images', on_delete=models.CASCADE, blank=True, null=True)
    reaction_positive = models.PositiveSmallIntegerField(blank=True, null=True)
    reaction_negative = models.PositiveSmallIntegerField(blank=True, null=True)
    # last_comment = models.ForeignKey('Comments.Comments', on_delete=models.CASCADE)
    comments_amount = models.PositiveSmallIntegerField(blank=True, null=True)



