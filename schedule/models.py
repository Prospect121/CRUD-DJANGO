from django.db import models

# Create your models here.


class Schedule(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = "schedule"
