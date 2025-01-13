# Generated by Django 5.1.4 on 2025-01-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameRoomInfo',
            fields=[
                ('room_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('player1', models.CharField(max_length=150, null=True)),
                ('player2', models.CharField(max_length=150, null=True)),
                ('choice1', models.CharField(max_length=10, null=True)),
                ('choice2', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
