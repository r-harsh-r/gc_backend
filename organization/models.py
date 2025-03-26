from django.db import models

class Employee(models.Model):
    employee_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    post = models.CharField(max_length=100)
    last_mood = models.IntegerField()
    load = models.IntegerField()
    productivity = models.IntegerField()

    def __str__(self):
        return self.name

class MoodHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="mood_history")
    date = models.DateField()
    value = models.IntegerField()

class Activity(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="activities")
    activity = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

class Reward(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="rewards")
    reward = models.CharField(max_length=255)
    date = models.DateField()

class DailyStreak(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="daily_streaks")
    streak = models.JSONField()  # List of streak values

class Calendar(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="calendar_events")
    event = models.CharField(max_length=255)
    date = models.DateField()

class UpcomingTask(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="upcoming_tasks")
    task = models.CharField(max_length=255)
    due = models.DateTimeField()

class DetailedSummary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="detailed_summaries")
    performance = models.CharField(max_length=255)
    feedback = models.TextField()
