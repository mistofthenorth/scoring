# Generated by Django 2.2 on 2019-06-17 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deschutesDemoScores', '0004_workout_scoringstyle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='id',
        ),
        migrations.AddField(
            model_name='team',
            name='teamID',
            field=models.CharField(default='11000', max_length=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='athlete',
            name='teams',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deschutesDemoScores.Team'),
        ),
        migrations.AlterField(
            model_name='score',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deschutesDemoScores.Team'),
        ),
    ]
