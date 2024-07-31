from django.core.management.base import BaseCommand
from myapp.utils import assign_prize_to_player

class Command(BaseCommand):
    help = 'Assign a prize to a player for completing a level'

    def add_arguments(self, parser):
        parser.add_argument('player_id', type=str)
        parser.add_argument('level_id', type=int)
        parser.add_argument('prize_id', type=int)

    def handle(self, *args, **kwargs):
        player_id = kwargs['player_id']
        level_id = kwargs['level_id']
        prize_id = kwargs['prize_id']
        assign_prize_to_player(player_id, level_id, prize_id)
        self.stdout.write(self.style.SUCCESS('Successfully assigned prize'))
