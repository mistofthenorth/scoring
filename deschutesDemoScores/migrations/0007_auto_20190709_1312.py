# Generated by Django 2.2 on 2019-07-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deschutesDemoScores', '0006_auto_20190617_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='minutes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='reps',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='seconds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
