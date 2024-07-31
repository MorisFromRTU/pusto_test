from django.db import models
from datetime import datetime

class Player(models.Model):
    player_id = models.CharField(max_length=100, unique=True)
    first_login = models.DateTimeField(auto_now_add=True)
    points = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.player_id

class Boost(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class PlayerBoost(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    boost = models.ForeignKey(Boost, on_delete=models.CASCADE)
    assigned_date = models.DateTimeField(auto_now_add=True)

class Level(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Prize(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class PlayerLevel(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    completed = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)

class LevelPrize(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    received = models.DateTimeField(auto_now_add=True)
