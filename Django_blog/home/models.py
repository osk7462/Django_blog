from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, DateField
from datetime import date, datetime

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = datetime.now().date()
    date_posted = models.DateField(default=date)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.title