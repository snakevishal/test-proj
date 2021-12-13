from django.db import models

class Post(models.Model):

    post = models.TextField()

    def __str__(self):
        return self.post