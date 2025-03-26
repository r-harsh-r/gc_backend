from rest_framework import serializers
from .models import Employee, MoodHistory, Activity, Reward, Calendar, UpcomingTask

class MoodHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodHistory
        fields = ['date', 'value']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['activity', 'timestamp']

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ['reward', 'date']

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ['event', 'date']

class UpcomingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingTask
        fields = ['task', 'due']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeDetailSerializer(serializers.ModelSerializer):
    mood_history = MoodHistorySerializer(many=True)
    activities = ActivitySerializer(many=True)
    rewards = RewardSerializer(many=True)
    calendar_events = CalendarSerializer(many=True)
    upcoming_tasks = UpcomingTaskSerializer(many=True)

    class Meta:
        model = Employee
        fields = ['employee_id', 'name', 'post', 'mood_history', 'activities', 'rewards', 'calendar_events', 'upcoming_tasks']
