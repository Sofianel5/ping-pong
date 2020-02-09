# Generated by Django 3.0.3 on 2020-02-08 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paddle', '0002_auto_20200207_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursegroup',
            name='fulfilling_courses',
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(default='There is no description for this course.'),
        ),
        migrations.AlterField(
            model_name='course',
            name='syllabus',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='pointscounter',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]