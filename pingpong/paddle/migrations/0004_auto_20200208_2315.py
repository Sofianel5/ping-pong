# Generated by Django 3.0.3 on 2020-02-08 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paddle', '0003_auto_20200208_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default='Art History', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(max_length=10),
        ),
    ]
