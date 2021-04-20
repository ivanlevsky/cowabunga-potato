import unittest
from python_common.string_utils import StringUtils


class TestStringUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.textToSplit1 = 'abe123*(*#*123山大佛i哦123SOEO'
        cls.textToSplit2 = '124{abiid|DKDL都是}444{123 |**@)}'
        cls.textGroup1 = ['abe', '*(*#*', '山大佛i哦', 'SOEO']
        cls.textGroup2 = ['124', 'abiid|DKDL都是', '444', '123 |**@)']

    def test_split_string_by_regex(self):
        with self.subTest():
            self.assertSequenceEqual(self.textGroup1,StringUtils.split_string_by_regex('123', self.textToSplit1))
        with self.subTest():
            self.assertSequenceEqual(self.textGroup2,StringUtils.split_string_by_regex('\\{|\\}', self.textToSplit2))


if __name__ == '__main__':
    unittest.main()