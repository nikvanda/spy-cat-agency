from django.db import models

from .validators import positive_validator, breed_validator


class SpyCat(models.Model):
    name = models.CharField(max_length=50)
    work_experience = models.PositiveSmallIntegerField()
    breed = models.CharField(max_length=100, validators=[breed_validator])
    salary = models.DecimalField(max_digits=8, decimal_places=2, validators=[positive_validator])

    def __str__(self):
        return self.name
