import unittest,warnings
from file_and_system.windows_os_utils import WindowsOsUtil


class TestWindowsOsUtil(unittest.TestCase):
    processIsRunning = ''
    processNotRunning = ''
    processToTestRunAndKill = ''
    command = ''

    @classmethod
    def setUpClass(cls):
        cls.processIsRunning = 'python.exe'
        cls.processNotRunning = 'retroarch.exe'
        cls.processToTestRunAndKill = 'notepad.exe'
        cls.command = 'echo 123'

    @classmethod
    def tearDownClass(cls):
        if WindowsOsUtil.check_process_running(cls.processToTestRunAndKill):
            WindowsOsUtil.kill_process_by_name(cls.processToTestRunAndKill)

    def test_kill_and_run_process_by_name(self):
        warnings.simplefilter('ignore', ResourceWarning)
        WindowsOsUtil.run_process_by_name(self.processToTestRunAndKill)
        self.assertTrue(WindowsOsUtil.check_process_running(self.processToTestRunAndKill))

        WindowsOsUtil.kill_process_by_name(self.processToTestRunAndKill)
        self.assertFalse(WindowsOsUtil.check_process_running(self.processToTestRunAndKill))

    def test_check_process_running(self):
        with self.subTest():
            self.assertTrue(WindowsOsUtil.check_process_running(self.processIsRunning))
        with self.subTest():
            self.assertFalse(WindowsOsUtil.check_process_running(self.processNotRunning))

    def test_get_command_output(self):
        self.assertEqual('123', WindowsOsUtil.get_command_output(self.command))

    def test_get_shell_output(self):
        self.assertEqual('123', WindowsOsUtil.get_shell_output(['powershell'], self.command))


if __name__ == '__main__':
    unittest.main(warnings='ignore')