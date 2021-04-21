import pytest
from file_and_system.windows_os_utils import WindowsOsUtil


class TestWindowsOsUtils:
    processIsRunning = ''
    processNotRunning = ''
    processToTestRunAndKill = ''
    command = ''

    @pytest.fixture(autouse=True)
    def setup_params(self):
        self.processIsRunning = 'python.exe'
        self.processNotRunning = 'retroarch.exe'
        self.processToTestRunAndKill = 'notepad.exe'
        self.command = 'echo 123'
        yield
        if WindowsOsUtil.check_process_running(self.processToTestRunAndKill):
            WindowsOsUtil.kill_process_by_name(self.processToTestRunAndKill)

    def test_kill_and_run_process_by_name(self):
        WindowsOsUtil.run_process_by_name(self.processToTestRunAndKill)
        assert WindowsOsUtil.check_process_running(self.processToTestRunAndKill)

        WindowsOsUtil.kill_process_by_name(self.processToTestRunAndKill)
        assert not WindowsOsUtil.check_process_running(self.processToTestRunAndKill)

    def test_check_process_running(self):
        assert WindowsOsUtil.check_process_running(self.processIsRunning)
        assert not WindowsOsUtil.check_process_running(self.processNotRunning)

    def test_get_command_output(self):
        assert '123' == WindowsOsUtil.get_command_output(self.command)

    def test_get_shell_output(self):
        assert '123' == WindowsOsUtil.get_shell_output(['powershell'], self.command)


if __name__ == '__main__':
    pytest.main(['-s', 'test_windows_os_utils.py'])
