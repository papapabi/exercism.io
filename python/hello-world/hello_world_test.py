import unittest

from hello_world import hello

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class HelloWorldTest(unittest.TestCase):
    def test_hello_no_arg(self):
        self.assertEqual(hello(), 'Hello, World!')

    def test_hello_with_one_word(self):
        self.assertEqual(hello('Pabi'), 'Hello, Pabi!')
    
    def test_hello_with_long_word(self):
        self.assertEqual(hello('Joshua Isaac De Castro Pabilona'), 'Hello,' \
                               ' Joshua Isaac De Castro Pabilona!')


if __name__ == '__main__':
    unittest.main()
