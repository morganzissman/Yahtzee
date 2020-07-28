import unittest

from Die import Die


class Yahtzee():
    def __init__(self):
        self.chosen = ()
        self.d1 = Die(6)
        self.d2 = Die(6)
        self.d3 = Die(6)
        self.d4 = Die(6)
        self.d5 = Die(6)
        self.cup_of_dice = [self.d1, self.d2, self.d3, self.d4, self.d5]
        self.choices = {"Yahtzee": False}

    def score(self, numbers):
        a = numbers.count(numbers[0])
        if a == 5:
            return 50
        else:
            return numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]
        # figure out if numbers which is a list of 5 numbers between 1 and 6
        # if they are all the same and return 50 if that is the case
        # if not, return the sum of all the numbers

    def roll(self):
        if len(self.chosen) == 0:
            rolled_dice = [self.d1.roll(), self.d2.roll(), self.d3.roll(), self.d4.roll(), self.d5.roll()]
            return rolled_dice
        else:
            for v in self.chosen:
                self.cup_of_dice[v].active = False
            rolled_dice = [self.d1.roll(), self.d2.roll(), self.d3.roll(), self.d4.roll(), self.d5.roll()]
            return rolled_dice

    def choose(self, choice):
        self.chosen = choice

    def newchoose(self, key, myroll):
        if myroll.count(myroll[0]) == 5:
            if self.choices[key] == True:
                return False
            else:
                self.choices[key] = True
                return True
        else:
            return False


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
        self.game.choose((0, 1))
        new_values = self.game.roll()
        print(new_values)
        self.assertEquals(values[0], new_values[0])
        self.assertEquals(values[1], new_values[1])

    def test_newchoose(self):
        self.game = Yahtzee()
        values = [1, 1, 1, 1, 1]
        self.assertFalse(self.game.newchoose("Yahtzee", [1, 2, 3, 4, 5]))
        self.assertTrue(self.game.newchoose("Yahtzee", values))
        self.assertFalse(self.game.newchoose("Yahtzee", values))
        self.assertTrue(self.game.newchoose("Chance", [1, 2, 3, 4, 5]))
        self.assertFalse(self.game.newchoose("Chance", [1, 2, 3, 4, 5]))

    def test_score(self):
        self.game = Yahtzee()
        values = [1, 1, 1, 1, 1]
        self.assertTrue(self.game.score(values) == 50)
        values = [1, 2, 3, 4, 5]
        self.assertTrue(self.game.score(values) == 15)


if __name__ == '__main__':
    unittest.main()
