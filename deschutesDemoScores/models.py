from django.db import models


class Event(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Workout(models.Model):
    description = models.CharField(max_length=100)
    description_extended = models.TextField(null=True, blank=True)
    scoringStyleChoices = (
        ('W', 'weight'),
        ('R', 'reps'),
        ('T', 'time'),)
    scoringStyle = models.CharField(
        max_length=1,
        choices=scoringStyleChoices,
        default='T')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    includeInFinalResults = models.BooleanField(default=True)

    def __str__(self):
        return self.description


class Division(models.Model):
    description = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Team(models.Model):
    team = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Athlete(models.Model):
    description = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Score(models.Model):
    weight = models.IntegerField(null=True, blank=True)
    minutes = models.IntegerField(null=True, blank=True)
    seconds = models.IntegerField(null=True, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.team.description) + ' ' + str(self.workout.description)

    class Meta:
        unique_together = ('team', 'workout', 'event')
