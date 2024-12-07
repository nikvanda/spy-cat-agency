from django.db import models

from .validators import positive_validator, breed_validator


class Task(models.Model):
    name = models.CharField(max_length=50)
    is_complete = models.BooleanField()

    class Meta:
        abstract = True


class SpyCat(models.Model):
    name = models.CharField(max_length=50)
    work_experience = models.PositiveSmallIntegerField()
    breed = models.CharField(max_length=100, validators=[breed_validator])
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        constraints = [models.CheckConstraint(check=models.Q(salary__gte=0), name='salary_gte_0')]

    def __str__(self):
        return self.name


class Mission(Task):
    spy_cat = models.ForeignKey(SpyCat, on_delete=models.SET_NULL, null=True, related_name='mission')

    def __str__(self):
        return self.name


class Target(Task):
    country = models.CharField(max_length=100)
    notes = models.TextField()

    mission = models.ForeignKey(Mission, on_delete=models.SET_NULL, null=True, related_name='targets')

    def __str__(self):
        return self.name
