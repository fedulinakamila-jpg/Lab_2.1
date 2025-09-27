import unittest
from guess_number import guess_number2, guess_number


class TestGuessNumberFunctions(unittest.TestCase):

    def test_guess_number2_mid(self):  # угадать число посередине
        self.assertEqual(guess_number2(secret=5, low=1, high=10), (5, 5))

    def test_guess_number2_end(self):  # угадать последнее число
        self.assertEqual(guess_number2(secret=1, low=1, high=10), (1, 1))

    def test_guess_number2_start(self):  # угадать первое число
        self.assertEqual(guess_number2(secret=10, low=1, high=10), (10, 10))

    def test_guess_number2_not_found(self):  # число вне диапазона
        with self.assertRaises(ValueError) as cm:
            guess_number2(secret=15, low=1, high=10)
        self.assertEqual(str(cm.exception), "Число не найдено")

    def test_guess_number2_dublicat(self):  # повторяющиеся числа
        result = guess_number2(secret=5, low=5, high=5)
        self.assertEqual(result, (5, 1))

    def test_guess_number2_zero_range_not_found(self):  # первое и последнее числа одинаковые
        with self.assertRaises(ValueError):
            guess_number2(secret=6, low=5, high=5)

    def test_guess_number_start(self):  # угадать первое число
        self.assertEqual(guess_number(secret=7, elements=[7, 8, 9]), (7, 1))

    def test_guess_number_secret_end(self):  # угадать последнее число
        self.assertEqual(guess_number(secret=3, elements=[1, 2, 3]), (3, 3))

    def test_guess_number_secret_not_found(self):  # число отсутствует в списке
        with self.assertRaises(ValueError):
            guess_number(secret=5, elements=[1, 2, 3])

    def test_guess_number_empty(self):  # пустой список
        with self.assertRaises(ValueError):
            guess_number(secret=1, elements=[])


if __name__ == '__main__':
    unittest.main()
