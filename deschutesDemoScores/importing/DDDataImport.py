from django.db import models
from deschutesDemoScores.models import Score, Workout, Team, Division, Event
import sys
import os
import csv

importFilePath = (os.path.abspath("importing/DDDemoData.csv"))


def importDDData():
    importFile = open(
        "/Users/briano/Python/virtualenvironment/DeschutesDemo/scoring/deschutesDemoScores/importing/DDDemoData.csv")
    with importFile as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Score.objects.get_or_create(
                weight=row[0],
                minutes=row[1],
                seconds=row[2],
                reps=row[3],
                team=Team.objects.get(pk=row[4]),
                workout=Workout.objects.get(pk=row[5]),
                event=Event.objects.get(pk=1)
            )
            print(row)
    # creates a tuple of the new object or
    # current object and a boolean of if it was created


def importDDTeams():
    importFile = open(
        "/Users/briano/Python/virtualenvironment/DeschutesDemo/scoring/deschutesDemoScores/importing/DDDemoTeams.csv")
    with importFile as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Team.objects.get_or_create(
                team=row[0],
                description=row[1],
                division=Division.objects.get(pk=row[2]),
                event=Event.objects.get(pk=1)
            )
            print(row)
            # creates a tuple of the new object or
            # current object and a boolean of if it was created
