from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    CATEGORIES = [
        ('perso', 'Personnel'),
        ('travail', 'Travail'),
        ('etude', 'Étude'),
        ('autre', 'Autre'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    categorie = models.CharField(max_length=20, choices=CATEGORIES, default='autre')
    termine = models.BooleanField(default=False)


    def __str__(self):
        return self.title
