from django.db import models

# Create your models here.
class LifePost(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.title