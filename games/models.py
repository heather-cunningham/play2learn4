from django.db import models
from django.contrib.auth.models import User


class FinalScore(models.Model):
    ANAGRAM = "anagram_hunt"
    MATH = "math_facts"
    #
    GAME_NAME_CHOICES = [
        (ANAGRAM, "Anagram Hunt"),
        (MATH, "Math Facts"),
    ]
    #
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game_name = models.CharField(max_length=25, choices=GAME_NAME_CHOICES, default=ANAGRAM)    
    settings = models.JSONField()
    final_score = models.IntegerField()
    game_date_time = models.DateTimeField(auto_now_add=True)
    #
    def __str__(self):
        """ toString() """
        return f"Player: {self.player.username}, Game: {self.game_name}, Final Score: {self.final_score}, Game Date: {self.game_date_time}"
## END class
 