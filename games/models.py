from django.db import models


class GameScore(models.Model):
    ANAGRAM = "ANAGRAM"
    MATH = "MATH"
    #
    GAME_CHOICES = [
        (ANAGRAM, "Anagram Hunt"),
        (MATH, "Math Facts"),
    ]
    #
    user_name = models.TextField()
    game = models.TextField(choices=GAME_CHOICES, default=MATH)
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
 