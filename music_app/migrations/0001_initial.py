# Generated by Django 4.1.1 on 2022-11-04 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpotifyAlarmModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('track_name', models.CharField(max_length=100)),
                ('artist_name', models.CharField(max_length=100)),
                ('switch', models.BooleanField()),
            ],
        ),
    ]
