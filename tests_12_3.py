import unittest
from module_12_2 import Runner, Tournament

def freeze_tests(func):
    def wrapper(*args, **kwargs):
        if getattr(args[0], 'is_frozen', False):
            print('Тесты в этом кейсе заморожены')
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return func(*args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @freeze_tests
    def test_walk(self):
        runner = Runner("Усэйн", speed=10)
        runner.walk()
        self.assertEqual(runner.distance, 10)

    @freeze_tests
    def test_run(self):
        runner = Runner("Андрей", speed=9)
        runner.run()
        self.assertEqual(runner.distance, 18)

    @freeze_tests
    def test_challenge(self):
        runner = Runner("Ник", speed=3)
        runner.run()
        runner.walk()
        self.assertEqual(runner.distance, 9)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @freeze_tests
    def test_first_tournament(self):
        tournament = Tournament(90, Runner("Усэйн", speed=10), Runner("Ник", speed=3))
        results = tournament.start()
        self.assertEqual(results[1].name, "Усэйн")

    @freeze_tests
    def test_second_tournament(self):
        tournament = Tournament(90, Runner("Андрей", speed=9), Runner("Ник", speed=3))
        results = tournament.start()
        self.assertEqual(results[1].name, "Андрей")

    @freeze_tests
    def test_third_tournament(self):
        tournament = Tournament(90, Runner("Усэйн", speed=10), Runner("Андрей", speed=9), Runner("Ник", speed=3))
        results = tournament.start()
        self.assertEqual(results[1].name, "Андрей")

if __name__ == '__main__':
    unittest.main()
