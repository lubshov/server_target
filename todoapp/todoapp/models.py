from django.db import models


# Create your models here.

class ListeningResponses(models.Model):
    text = models.CharField(max_length=150)

    def __str__(self):
        return self.text
