from django.db import models


class Post(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    text = models.CharField(max_length=200)

    def __str__(self):
        # выводим текст поста
        return self.text
