from unittest import TestCase

from pyga import Fitness


class FitnessTestCase(TestCase):
    def test_init(self):
        self.assertEqual(str(Fitness(123)), '123')
        self.assertEqual(str(Fitness(-123, is_natural=False)), '-123')
        self.assertEqual(int(Fitness(123)), 123)
        self.assertEqual(float(Fitness(123.5)), 123.5)

    def test_math(self):
        self.assertEqual(Fitness(123)+1, 124)
        self.assertEqual(Fitness(123)-1, 122)
        self.assertEqual(Fitness(123)*2, 246)
        self.assertEqual(abs(Fitness(-123)), 123)

    def test_logic(self):
        self.assertTrue(Fitness(123))
        self.assertTrue(Fitness(-123))
        self.assertTrue(Fitness(0))
        self.assertFalse(Fitness(None))

        self.assertTrue(Fitness(123) == 123)
        self.assertFalse(Fitness(123) == 122)

        self.assertTrue(Fitness(123) != 122)
        self.assertFalse(Fitness(123) != 123)

        self.assertTrue(Fitness(123) < 124)
        self.assertFalse(Fitness(123) < 123)
        self.assertFalse(Fitness(123) < 122)

        self.assertTrue(Fitness(123) <= 124)
        self.assertTrue(Fitness(123) <= 123)
        self.assertFalse(Fitness(123) <= 122)

        self.assertTrue(Fitness(123) > 122)
        self.assertFalse(Fitness(123) > 123)
        self.assertFalse(Fitness(123) > 124)

        self.assertTrue(Fitness(123) >= 122)
        self.assertTrue(Fitness(123) >= 123)
        self.assertFalse(Fitness(123) >= 124)
