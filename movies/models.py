from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE   
    )
title = models.CharField(max_length=100)
date_watched = models.DateField()
rating = models.IntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(10)]
)
review = models.TextField(blank=True)

def __str__(self):
    return self.name