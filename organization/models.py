from django.db import models

class Employee(models.Model):
    employee_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    post = models.CharField(max_length=50)
    last_mod = models.IntegerField()
    load = models.IntegerField()
    productivity = models.IntegerField()

    def __str__(self):
        return self.name
