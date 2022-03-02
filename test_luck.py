"""There is a function called find_luck(). We do not know its code, but we know exactly how it works — given a string, it returns an object if 'luck' is contained in the string, and None otherwise. Write tests for this function (use assertIsNotNone and assertIsNone).
In this Code Challenge, you do not need to import the module with the function at the beginning of the code. To call the function, just type its name, find_luck().

"""
# tests for the function
import unittest


class TestFindLuck(unittest.TestCase):

    def test_strings_with_luck(self):
        # checks that find_luck finds 'luck' in all of the strings with 'luck'
        strings_with_luck = [
            'luck',
            'hereluckthere',
            'hereluck',
            'luckhere',
            'luck is great but most of life is hard work',
        ]

        # write your test here
        for s in strings_with_luck:
            self.assertIsNotNone(find_luck(s))

    def test_strings_without_luck(self):
        # checks that find_luck finds 'luck' in all of the strings with 'luck'
        strings_without_luck = ['here', 'duck', 'four', 'uckl']

        # write your test here
        for s in strings_without_luck:
            self.assertIsNone(find_luck(s))


if __name__ == '__main__':
    unittest.main()