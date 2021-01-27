from django.test import TestCase
from .models import Gamemodel, Player

class GamemodelTest(TestCase):
    @classmethod
    def test_game_name(clsself):
        game=Gamemodel.object.get(id=1)
        self.assertEquals(game.name, 'Grand Theft Auto 2')

    def game_remove_test(self):
        count = Gamemodel.objects.count()
        game = Gamemodel.objects.get(id=2)
        game.delete()
        self.assertEqual(game.objects.count(), count-1)

    def test_game_year(self):
        game = Gamemodel.objects.get(id=2)
        self.assertEquals(game.year, '1999')
