# Generated by Django 3.0.3 on 2020-02-09 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paddle', '0007_auto_20200209_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='graduationrequirements',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='paddle.GraduationRequirements'),
        ),
        migrations.AlterField(
            model_name='student',
            name='reportCard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='paddle.ReportCard'),
        ),
        migrations.AlterField(
            model_name='student',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='paddle.Schedule'),
        ),
    ]
