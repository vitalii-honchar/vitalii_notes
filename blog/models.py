from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
