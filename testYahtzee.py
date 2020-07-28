import unittest

from Die import Die


class Yahtzee:
    def __init__(self):
        self.chosen = ()
        self.d1 = Die(6)
        self.d2 = Die(6)
        self.d3 = Die(6)
        self.d4 = Die(6)
        self.d5 = Die(6)
        self.cup_of_dice = [self.d1, self.d2, self.d3, self.d4, self.d5]

    def roll(self):
        if len(self.chosen) == 0:
            rolled_dice = [self.d1.roll(), self.d2.roll(), self.d3.roll(), self.d4.roll(), self.d5.roll()]
            return rolled_dice
        else:
            for v in self.chosen:
                self.cup_of_dice[v].active = False
            rolled_dice = [self.d1.roll(), self.d2.roll(), self.d3.roll(), self.d4.roll(), self.d5.roll()]
            return rolled_dice

    def choose(self,choice):
        self.chosen = choice


class MyTestCase(unittest.TestCase):
    def test_yahtzee(self):
        self.game = Yahtzee()

    def test_roll(self):
        self.game = Yahtzee()
        values = self.game.roll()
        self.assertEqual(5, len(values))

    def test_die(self):
        d = Die(6)
        v = d.roll()
        self.assertGreater(v, 0)
        self.assertLess(v, 7)

    def test_choose(self):
        self.game = Yahtzee()
        values = self.game.roll()
        print(values)
        self.game.choose((0,1))
        new_values = self.game.roll()
        print(new_values)
        self.assertEquals(values[0], new_values[0])
        self.assertEquals(values[1], new_values[1])


if __name__ == '__main__':
    unittest.main()
