# Generated by Django 3.0.3 on 2020-03-03 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0007_player_currentworld'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='world',
            field=models.IntegerField(default=0),
        ),
    ]
