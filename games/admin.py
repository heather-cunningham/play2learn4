from django.contrib import admin
from games.models import Game, FinalScore


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    model = Game
    list_display = ["game_name", "created", "settings", ]
    list_display_links = ("game_name", "created",)
    list_filter = ("game_name", "created",)
    search_fields = ("game_name",)
    #
    #
    def get_readonly_fields(self, request, obj=None):
        if(obj):
            return ("game_name", "settings", "created",)
        return ()


@admin.register(FinalScore)
class FinalScoreAdmin(admin.ModelAdmin):
    model = FinalScore
    list_display = [ "game_name", "id_of_game", "final_score", "game_date_time", "settings", "player"]
    list_display_links = ("game_name", "id_of_game", "final_score", "game_date_time",)
    list_filter = ("game_name", "game_date_time",)
    search_fields = ("game_name", "final_score", "player",)
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
            return ("player", "game_id", "game_name", "final_score", "game_date_time", "settings", )
        return ()