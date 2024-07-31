from .models import PlayerLevel, LevelPrize, Prize
from datetime import datetime
import csv

def assign_prize_to_player(player_id, level_id, prize_id):
    try:
        player_level = PlayerLevel.objects.get(player_id=player_id, level_id=level_id, is_completed=True)
        LevelPrize.objects.create(level_id=level_id, prize_id=prize_id, received=datetime.now())
    except PlayerLevel.DoesNotExist:
        print(f'Player {player_id} has not completed level {level_id}.')

def export_player_level_data_to_csv(file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Player ID', 'Level Title', 'Is Completed', 'Prize Title'])

        player_levels = PlayerLevel.objects.all().select_related('player', 'level')
        level_prizes = LevelPrize.objects.all().select_related('level', 'prize')

        for player_level in player_levels:
            prize = level_prizes.filter(level=player_level.level).first()
            prize_title = prize.prize.title if prize else 'No Prize'
            writer.writerow([player_level.player.player_id, player_level.level.title, player_level.is_completed, prize_title])
