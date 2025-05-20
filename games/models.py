from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    # for both games
    ANAGRAM = "anagram_hunt"
    MATH = "math_facts"
    GAME_NAME_CHOICES = [
        (ANAGRAM, "Anagram Hunt"),
        (MATH, "Math Facts"),
    ]
    game_name = models.CharField(max_length=25, choices=GAME_NAME_CHOICES, default=ANAGRAM)
    settings = models.JSONField()
    # for MathFacts
    MF_OP_DICTIONARY = {
        "+": "Addition",
        "-": "Subtraction",
        "x": "Multiplication",
        "/": "Division",
    }
    #
    def get_mf_operation(self):
        """ Returns the full word, in title-case or Pascal-case, for the operation
          based on its stored operator. """
        operation = self.settings["operation"]
        if (operation not in self.MF_OP_DICTIONARY):
            raise ValueError(f"Invalid operation: {operation}")
        return self.MF_OP_DICTIONARY[operation]
    #
    # toString(): for both games
    def __str__(self):
        """ toString(): Returns the game's name and its settings. """
        game_settings = f"Game: {self.game_name}"
        #
        #
        if self.settings:
            if ("operation" in self.settings):
                game_settings += f" | Operation: {self.get_mf_operation()}"
            if ("max_number" in self.settings):
                game_settings += f" | Max Number: {self.settings['max_number']}"
            if ("word_length" in self.settings):
                game_settings += f" | Word Length: {self.settings['word_length']}"
        return game_settings
## END class Game(models...


class FinalScore(models.Model):
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)        
    final_score = models.IntegerField()
    game_date_time = models.DateTimeField(auto_now_add=True)
    settings = models.JSONField(default=dict)
    #
    # toString()
    def __str__(self):
        """ toString(): Returns the Player's username, the game's name, final score, and date played. """
        return (f"Player: {self.player.username}, Game: {self.game.game_name}, "
                f"Game Settings: {self.game.settings}, " 
                f"Final Score: {self.final_score}, Game Date: {self.game_date_time}")
## END class FinalScore(models...
 