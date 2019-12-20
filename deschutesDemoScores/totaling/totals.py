from deschutesDemoScores.models import Score, Workout, Team, Event


def getSingleWorkoutTotal(workout, division):

    workoutProperties = Workout.objects.get(id=workout)
    setOfTeams = Team.objects.filter(division=division)
    setOfScores = Score.objects.filter(
        workout=workoutProperties.id, team__division=division)

    if workoutProperties.scoringStyle == 'T':
        setOfScores = sorted(setOfScores, key=lambda x: (
            (x.minutes or float('inf')), (x.seconds or float('inf')), -int(x.reps or 0)))
    elif workoutProperties.scoringStyle == 'R':
        setOfScores = sorted(setOfScores, key=lambda x: (-int(x.reps or 0)))
    elif workoutProperties.scoringStyle == 'W':
        setOfScores = sorted(setOfScores, key=lambda x: (-int(x.weight or 0)))
    else:
        pass
    # Add blank entries for teams that have no scores on this workout
    teamList = [x.team for x in setOfTeams]
    scoreTeamList = [x.team.team for x in setOfScores]
    missingTeamsList = set(teamList) - set(scoreTeamList)

    for team in missingTeamsList:
        (blankScore, created) = Score.objects.get_or_create(weight=None, minutes=None, seconds=None, reps=None,
                                                            team=Team.objects.get(pk=team), workout=Workout.objects.get(pk=workout), event=Event.objects.get(pk=1))
        setOfScores.append(blankScore)

    listOfScores = []
    for (rank, score) in enumerate(setOfScores, 1):
        recordedScore = rankedScore(score, rank)
        listOfScores.append(recordedScore)

    for (i, score) in enumerate(listOfScores):
        isTie = False
        if i == 0:
            continue  # Don't run this check on the first item since no tie is possible with previous score

        if workoutProperties.scoringStyle == 'T':
            if (listOfScores[i].score.minutes or float('inf')) == (listOfScores[i - 1].score.minutes or float('inf')) and (listOfScores[i].score.seconds or float('inf')) == (listOfScores[i - 1].score.seconds or float('inf')) and (listOfScores[i].score.reps or 0) == (listOfScores[i - 1].score.reps or 0):
                isTie = True
        elif workoutProperties.scoringStyle == 'R':
            if (listOfScores[i].score.reps or 0) == (listOfScores[i - 1].score.reps or 0) and (listOfScores[i].score.minutes or 0) == (listOfScores[i - 1].score.minutes or 0) and (listOfScores[i].score.seconds or 0) == (listOfScores[i - 1].score.seconds or 0):
                isTie = True
        elif workoutProperties.scoringStyle == 'W':
            if (listOfScores[i].score.weight or 0) == (listOfScores[i - 1].score.weight or 0) and (listOfScores[i].score.minutes or 0) == (listOfScores[i - 1].score.minutes or 0) and (listOfScores[i].score.seconds or 0) == (listOfScores[i - 1].score.seconds or 0):
                isTie = True
        else:
            isTie = False

        if isTie:
            listOfScores[i].rank = listOfScores[i - 1].rank

    return listOfScores


def getAllWorkoutsTotal(division):

    setOfWorkouts = Workout.objects.filter(event=1)

    listOfWorkoutScores = []
    for workout in setOfWorkouts:
        if workout.includeInFinalResults:
            listOfWorkoutScores.append(
                getSingleWorkoutTotal(workout.id, division))

    allEventScores = {}
    for workout in listOfWorkoutScores:
        for score in workout:
            if score.score.team.team in allEventScores:
                allEventScores[score.score.team.team].append(score)
            else:
                allEventScores[score.score.team.team] = [score]

    listOfFinalResults = []
    for total in allEventScores:
        listOfFinalResults.append(finalResult(total, allEventScores[total]))

    sortedlistOfFinalResults = sorted(
        listOfFinalResults, key=lambda x: (x.score))

    for (rank, score) in enumerate(sortedlistOfFinalResults, 1):
        score.rank = rank

    for (i, score) in enumerate(sortedlistOfFinalResults):
        if i == 0:
            continue

        if sortedlistOfFinalResults[i].score == sortedlistOfFinalResults[i - 1].score:
            sortedlistOfFinalResults[i].rank = sortedlistOfFinalResults[i - 1].rank

    return sortedlistOfFinalResults


class rankedScore:
    def __init__(self, score, rank):
        self.score = score
        self.rank = rank


class finalResult:
    def __init__(self, team, eventScores):
        self.team = team
        self.rank = 0
        self.eventScores = eventScores
        self.score = sum(x.rank for x in eventScores)
