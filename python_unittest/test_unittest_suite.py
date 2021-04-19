import unittest

from python_unittest.test_crypto_utils import TestCryptoUtils
from python_unittest.test_string_utils import TestStringUtils
from python_unittest.test_windows_os_utils import TestWindowsOsUtil
from python_unittest.test_global_param import TestGlobalParam


def suite():
    loader = unittest.TestLoader()
    suites = unittest.TestSuite()
    # suite.addTest(TestCryptoUtils('test_bin_encode'))
    # suite.addTest(TestCryptoUtils('test_bin_decode'))
    # suite.addTest(TestCryptoUtils('test_url_encode'))
    suites.addTests(loader.loadTestsFromTestCase(TestGlobalParam))
    suites.addTests(loader.loadTestsFromTestCase(TestCryptoUtils))
    suites.addTests(loader.loadTestsFromTestCase(TestWindowsOsUtil))
    suites.addTests(loader.loadTestsFromTestCase(TestStringUtils))
    return suites


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())