# Generated by Django 3.2.9 on 2022-04-11 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awardapp', '0003_auto_20220410_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='date_posted',
        ),
    ]
