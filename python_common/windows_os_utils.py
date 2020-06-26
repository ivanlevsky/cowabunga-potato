import os, subprocess


def kill_process_by_name(name):
    os.system('taskkill /f /im  ' + name)


def get_command_output(cmd):
    (status, output) = subprocess.getstatusoutput(cmd)
    if status == 0:
        return output


def get_shell_output(shell_cmd, execute_cmd):
    shell_cmd.append(execute_cmd)
    return subprocess.Popen(shell_cmd, stdout=subprocess.PIPE).communicate()[0].decode('utf8')

