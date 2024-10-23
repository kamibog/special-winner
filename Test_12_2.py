from module_12_2 import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.name1 = Runner("Усэйн", speed=10)
        self.name2 = Runner("Андрей", speed=9)
        self.name3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_race1(self):
        tournament = Tournament(90, self.name1, self.name3)
        results = tournament.start()
        self.all_results[max(results.keys())] = results[max(results.keys())].name
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")


    def test_race2(self):
        tournament = Tournament(90, self.name2, self.name3)
        results = tournament.start()
        self.all_results[max(results.keys())] = results[max(results.keys())].name
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")

    def test_race3(self):
        tournament = Tournament(90, self.name1, self.name2, self.name3)
        results = tournament.start()
        self.all_results[max(results.keys())] = results[max(results.keys())].name
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")

if __name__ == '__main__':
    unittest.main()
