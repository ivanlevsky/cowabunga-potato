import pytest
from python_common.string_utils import StringUtils


class TestStringUtils:
    textToSplit1 = ''
    textToSplit2 = ''
    textGroup1 = ''
    textGroup2 = ''

    @pytest.fixture()
    def setup_params(self):
        self.textToSplit1 = 'abe123*(*#*123山大佛i哦123SOEO'
        self.textToSplit2 = '124{abiid|DKDL都是}444{123 |**@)}'
        self.textGroup1 = ['abe', '*(*#*', '山大佛i哦', 'SOEO']
        self.textGroup2 = ['124', 'abiid|DKDL都是', '444', '123 |**@)']

    def test_split_string_by_regex(self, setup_params):
        assert self.textGroup1 == StringUtils.split_string_by_regex('123', self.textToSplit1)
        assert self.textGroup2 == StringUtils.split_string_by_regex('\\{|\\}', self.textToSplit2)


if __name__ == '__main__':
    pytest.main(['-s', 'test_string_utils.py'])
