from django.db import models
from django.utils import timezone


class Admin(models.Model):

    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    date_of_hiring = models.DateField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.firstName
