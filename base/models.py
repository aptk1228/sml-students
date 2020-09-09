from django.db import models
from base.constants import MARK_CHOICES


class Student(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    birth_date = models.DateField(verbose_name="Дата рождения")
    mark = models.PositiveSmallIntegerField(
        choices=MARK_CHOICES, verbose_name="Оценка")

    def __str__(self):
        return self.full_name
