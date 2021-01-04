import unittest

import emojicode


class TestStringMethods(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(emojicode.emoji_encode(
            'Hello World!'), '😡😄😋😋😎😵😰😎😑😋😃😴')

    def test_decode(self):
        self.assertEqual(emojicode.emoji_decode(
            '😡😄😋😋😎😵😰😎😑😋😃😴'), 'Hello World!')
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
