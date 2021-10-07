from django.db import models

# Create your models here.
class FlUpload(models.Model):
    file = models.FileField()
    name = models.TextField()

    def __str__(self):
        return self.name
