import os, subprocess


def kill_process_by_name(name):
    os.system('taskkill /f /im  ' + name)


def get_command_output(cmd):
    (status, output) = subprocess.getstatusoutput(cmd)
    if status == 0:
        return output

