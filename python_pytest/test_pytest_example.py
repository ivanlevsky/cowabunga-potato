import pytest

def sum_num(num_one, num_two):
    return num_one + num_two

# this works like x-unit setup class and teardown class
@pytest.fixture(scope='class', autouse=True)
def run_before_class():
    print('class start')
    yield
    print('class end')


class TestPytestExample:
    num_one = None
    num_two = None
    num_three = None
    num_four = None
    num_sum_one = None
    num_sum_two = None
    num_sum_three = None
    '''
    # x-unit style setup and teardown
        def setup_class(self):
            print('setup')

        def teardown_class(self):
            print('teardown')

        @staticmethod
        def setup():
            print('case start')

        @staticmethod
        def teardown():
            print('case end')
    '''

    '''
    # use pytest fixture to setup and teardown test class 
    # after 'yield' run to teardown
    # this function will run before every test function
        @pytest.fixture equals @pytest.fixture(scope='function')
    # use 'autouse=True' to run fixture function before every test function
    '''

    @pytest.fixture(autouse=True)
    def setup_params(self):
        self.num_one = 2
        self.num_two = 3
        self.num_three = 8
        self.num_four = 1
        self.num_sum_one = 5
        self.num_sum_two = 9
        self.num_sum_three = 11
        print("\r\n setup")
        yield
        print("\r\n teardown")

    def test_add_num_one(self):
        assert self.num_sum_one == sum_num(self.num_one, self.num_two)

    def test_add_num_two(self):
        assert self.num_sum_two == sum_num(self.num_three, self.num_four)

    def test_add_num_three(self):
        assert self.num_sum_three == sum_num(self.num_two, self.num_three)


if __name__ == '__main__':
    '''
        # this will run all pytest class
        pytest.main(['-s'])
        # use file name to run one class
        pytest.main(['-s', 'test_xxx.py'])
        # this will only run test_pytest_example.py on rootdir
        pytest.main(['-s', 'test_pytest_example.py'])
        # set cache-dir with '-o' and 'cache_dir=path'
        pytest.main(['-o', 'cache_dir=D:/abc.../123../.pytest_cache'])
        # set rootdir or pytest will run all pytest files in this project
        pytest.main(['--rootdir=../../python_pytest/'])
        # use ignore to skip test file
        pytest.main(['--ignore=../python_pytest/test_windows_os_utils.py'])
    '''
    pytest.main([
                 '--rootdir=../python_pytest/',
                 '--ignore=../python_pytest/test_pytest_example.py',
                 '--html=../test file/test reports/pytest/report.html',
                 '-o', 'cache_dir=../test file/test reports/pytest/.pytest_cache'
                 ])