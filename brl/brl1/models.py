from django.db import models
class satya(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    moobile = models.IntegerField(max_length=10)
