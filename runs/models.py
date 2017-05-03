import datetime
from django.db import models
from django.utils import timezone

class Run(models.Model):
    def __str__(self):
        return self.run_date


    distance = models.IntegerField
    run_date = models.DateTimeField('run date')