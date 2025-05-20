from django.contrib import admin
from games.models import Game, FinalScore


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    model = Game
    list_display = ["game_name", "settings", "created"]
    #
    #
    def get_readonly_fields(self, request, obj=None):
        if(obj):
            return ("game_name", "settings", "created")
        return ()


@admin.register(FinalScore)
class FinalScoreAdmin(admin.ModelAdmin):
    model = FinalScore
    list_display = [ "player", "id_of_game", "game_name", "final_score", "game_date_time", "settings" ]
    #
    #
    def id_of_game(self, obj):
        return obj.game.id  # Access the implicit game_id field
    #
    #
    id_of_game.admin_order_field = 'game'  # Allows sorting by game_id
    id_of_game.short_description = 'Game ID'  # Custom column name
    #
    #
    def get_readonly_fields(self, request, obj=None):
        if(obj):
            return ("player", "game_id", "game_name", "final_score", "game_date_time", "settings")
        return ()