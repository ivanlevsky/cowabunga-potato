import os, subprocess


def kill_process_by_name(name):
    os.system('taskkill /f /im  ' + name)


def run_process_by_name(name):
    os.system(name)


def check_process_running(name):
    running = False
    if name.__contains__('\\'):
        name = name[name.rfind('\\'):].replace('\\','')
    elif name.__contains__('/'):
        name = name[name.rfind('/'):].replace('/','')
    elif name.__contains__('//'):
        name = name[name.rfind('//'):].replace('//','')
    (status, output) = subprocess.getstatusoutput(''.join(('tasklist /nh /fi  \"Imagename eq ', name, '\"')))

    if status == 0:
        if output.strip().startswith(name):
            running = True
        return running


def get_command_output(cmd):
    (status, output) = subprocess.getstatusoutput(cmd)
    if status == 0:
        return output


def get_shell_output(shell_cmd, execute_cmd):
    shell_cmd.append(execute_cmd)
    return subprocess.Popen(shell_cmd, stdout=subprocess.PIPE).communicate()[0].decode('utf8')



