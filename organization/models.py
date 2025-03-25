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


from django.db import models

# class Employee(models.Model):
#     employee_id = models.IntegerField(unique=True)
#     name = models.CharField(max_length=255)
#     post = models.CharField(max_length=255)

class MoodHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.IntegerField()

class Activity(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    activity = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

class Reward(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    reward = models.CharField(max_length=255)
    date = models.DateField()

class CalendarEvent(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event = models.CharField(max_length=255)
    date = models.DateField()

class Task(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    due = models.DateTimeField()
