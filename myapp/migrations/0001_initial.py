# Generated by Django 5.0.7 on 2024-07-31 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.CharField(max_length=100, unique=True)),
                ('first_login', models.DateTimeField(auto_now_add=True)),
                ('points', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerBoost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateTimeField(auto_now_add=True)),
                ('boost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.boost')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.player')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('score', models.PositiveIntegerField(default=0)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.level')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.player')),
            ],
        ),
        migrations.CreateModel(
            name='LevelPrize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received', models.DateTimeField(auto_now_add=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.level')),
                ('prize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.prize')),
            ],
        ),
    ]
