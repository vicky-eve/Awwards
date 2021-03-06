# Generated by Django 3.2.9 on 2022-04-10 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awardapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='average',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='project',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='awardapp.project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='creativity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='design',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='developer',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='usability',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
