from django.contrib import admin
from .models import Employee, MoodHistory, Activity, Reward, DailyStreak, Calendar, UpcomingTask, DetailedSummary

# Register models to appear in Django Admin
admin.site.register(Employee)
admin.site.register(MoodHistory)
admin.site.register(Activity)
admin.site.register(Reward)
admin.site.register(DailyStreak)
admin.site.register(Calendar)
admin.site.register(UpcomingTask)
admin.site.register(DetailedSummary)
