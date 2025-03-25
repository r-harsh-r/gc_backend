from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


from rest_framework import serializers
from .models import Employee, MoodHistory, Activity, Reward, CalendarEvent, Task

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
        model = CalendarEvent
        fields = ['event', 'date']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task', 'due']

class EmployeeDetailSerializer(serializers.ModelSerializer):
    mood_history = MoodHistorySerializer(many=True, source="moodhistory_set")
    activity = ActivitySerializer(many=True, source="activity_set")
    rewards = RewardSerializer(many=True, source="reward_set")
    calendar = CalendarSerializer(many=True, source="calendarevent_set")
    upcoming_tasks = TaskSerializer(many=True, source="task_set")

    class Meta:
        model = Employee
        fields = ['employee_id', 'name', 'post', 'mood_history', 'activity', 'rewards', 'calendar', 'upcoming_tasks']
