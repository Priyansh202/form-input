from django.db import models

class MyModel(models.Model):
    count_1 = models.IntegerField(default=0)
    count_2 = models.IntegerField(default=0)