# Generated by Django 4.0.3 on 2022-04-16 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ProfileImage',
            field=models.FileField(default='default.png', upload_to='profile/'),
        ),
    ]
