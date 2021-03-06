from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.title
