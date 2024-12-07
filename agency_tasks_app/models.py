from django.db import models

from .validators import breed_validator


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
        constraints = [
            models.CheckConstraint(check=models.Q(salary__gte=0), name='salary_gte_0'),
        ]

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        mission_count = 0
        try:
            mission_count = self.mission.all()
        except ValueError:
            pass
        if not mission_count:
            return super().save(*args, force_insert, force_update, using, update_fields)
        raise ValueError('Cat is already on a mission. You cannot and another one.')

    def __str__(self):
        return self.name


class Mission(Task):
    name = models.CharField(max_length=50, default='tese')
    is_complete = models.BooleanField(default=False)

    spy_cat = models.ForeignKey(SpyCat, on_delete=models.SET_NULL, null=True, related_name='mission')

    def __str__(self):
        return self.name


class Target(Task):
    country = models.CharField(max_length=100)
    notes = models.TextField()

    mission = models.ForeignKey(Mission, on_delete=models.SET_NULL, null=True, related_name='targets')

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):

        super().save(*args, force_insert, force_update, using, update_fields)
        related_mission = self.mission
        related_targets_count = related_mission.targets.count()
        completed_targets = related_mission.targets.filter(is_complete=True).count()

        if related_targets_count == completed_targets:
            related_mission.is_completed = True
            related_mission.save()

    def __str__(self):
        return self.name
