from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

def summary(self):
    return self.title

def summary(self):
    return self.body[:100]

    # Register your models here.

