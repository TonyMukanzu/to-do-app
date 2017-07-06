from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 32)


class Tasks(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length = 32)
    description = models.CharField(max_length = 120)
    date_created = models.DateTimeField(auto_now_add = True)
    due_date = models.DateTimeField()
    marked_done = models.BooleanField()
    category_id = models.ForeignKey(Category)
