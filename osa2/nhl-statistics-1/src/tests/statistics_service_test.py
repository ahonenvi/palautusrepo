import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_existing_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_returns_none_if_player_not_found(self):
        self.assertIsNone(self.stats.search("Nobody"))

    def test_team_returns_players_of_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)

    def test_top_returns_best_players_first(self):
        top = self.stats.top(3)
        names = [player.name for player in top]
        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])
