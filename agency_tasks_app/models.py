from django.db import models


class SpyCat(models.Model):
    name = models.CharField(max_length=50)
    work_experience = models.PositiveSmallIntegerField()
    breed = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
