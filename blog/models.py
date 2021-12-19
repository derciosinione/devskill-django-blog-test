from django.db import models


class Post(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=256)
    body = models.TextField()
    date = models.DateTimeField()
