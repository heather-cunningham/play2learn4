from django.db import models


class GameFinalScore(models.Model):
    ANAGRAM_GAME = "ANAGRAM_GAME"
    MATH_GAME = "MATH_GAME"
    #
    GAME_CHOICES = [
        (ANAGRAM_GAME, "Anagram Hunt"),
        (MATH_GAME, "Math Facts"),
    ]
    #
    username = models.TextField()
    game_name = models.TextField(choices=GAME_CHOICES, default=ANAGRAM_GAME)
    final_score = models.IntegerField()
    game_datetime = models.DateTimeField(auto_now_add=True)
 