# Generated by Django 4.0.1 on 2022-01-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='std',
            field=models.CharField(max_length=10),
        ),
    ]
