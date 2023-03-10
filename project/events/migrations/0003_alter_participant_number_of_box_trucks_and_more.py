# Generated by Django 4.1.7 on 2023-02-26 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_participant_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='number_of_box_trucks',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='participant',
            name='number_of_buses',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='participant',
            name='number_of_students_in_band',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='participant',
            name='number_of_students_in_color_guard',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='participant',
            name='number_of_students_in_drill_team',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='participant',
            name='number_of_tractor_trailer_rigs',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='participant',
            name='number_of_trailers',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='participant',
            name='status',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
