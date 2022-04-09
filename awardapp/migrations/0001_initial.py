# Generated by Django 3.2.9 on 2022-04-09 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usability', models.IntegerField(default=0)),
                ('design', models.IntegerField(default=0)),
                ('creativity', models.IntegerField(default=0)),
                ('content', models.IntegerField(default=0)),
                ('developer', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('landingpage_pic', models.ImageField(null=True, upload_to='images/')),
                ('description', models.TextField(max_length=200)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('link', models.URLField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(blank=True, max_length=50)),
                ('bio', models.TextField(blank=True, max_length=200)),
                ('contact_info', phone_field.models.PhoneField(blank=True, max_length=11)),
                ('profile_pic', models.ImageField(upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]