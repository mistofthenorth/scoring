from django.contrib import admin

from .models import Score, Workout, Team, Event, Athlete, Division

admin.site.register(Score)
admin.site.register(Workout)
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(Athlete)
admin.site.register(Division)
