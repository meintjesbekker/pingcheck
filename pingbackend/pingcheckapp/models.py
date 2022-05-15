from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# This is your database.

class PingCheckModel(models.Model):
    title = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    comment = models.TextField(blank=TRUE)

    # set to current time
    craeted = models.DateTimeField(auto_now_add=TRUE)
    completed = models.BooleanField(default=False)

    # user who created this
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
