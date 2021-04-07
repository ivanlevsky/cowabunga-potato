from python_common.file_and_system.windows_os_utils import *
from python_common.string_utils import *
from python_common.global_param import aapt_path,android_apk_list
from python_common.file_and_system.file_utils import *


def android_device_list():
    return get_command_output('adb devices').split('\n')[1].replace('device', '').strip()


def android_version():
    return get_command_output('adb shell getprop ro.build.version.release')


def android_api_version():
    return get_command_output('adb shell getprop ro.build.version.sdk')


def android_current_opened_app_info():
    msg = get_shell_output(['adb', 'shell'], 'dumpsys window windows | grep -E \'mCurrentFocus|mFocusedApp\'')
    msg = split_string_by_regex('{|}', msg)[1].split(' ')[2]
    return msg.split('/')[0], msg.split('/')[1]


def android_check_app_active(app_package):
    msg = get_shell_output(['adb', 'shell'], 'dumpsys window windows | grep -e \'Window #\'').split('\r\n')
    for m in msg:
        if m.__contains__(app_package):
            msg = split_string_by_regex('{|}', m.strip())[1].split(' ')[2]
            return msg.split('/')[0], msg.split('/')[1]
    return 'not_find', 'not_find'


def android_aapt_install():
    print(get_command_output(' '.join(('adb push', aapt_path, '/data/local/tmp'))))
    print(get_command_output('adb shell chmod 0755 /data/local/tmp/aapt-arm-pie'))



def android_home_button():
    get_shell_output(['adb', 'shell'], 'am start -W -c android.intent.category.HOME -a android.intent.action.MAIN')


def android_all_package_list():
    msg = filter(None, get_shell_output(['adb', 'shell'], 'pm list packages -3 -f').split('\r\n'))
    package_list = []
    for ms in msg:
        ms = android_aapt_get_app_info(ms[ms.index('/'):ms.rindex('=')]).replace('\r\n', '').split('\'')
        if ms.count('package: name=') == 1:
            pkg = ms[ms.index('package: name=') + 1]
        else:
            pkg = ''
        if ms.count('application-label-zh-CN:') == 1:
            name = ms[ms.index('application-label-zh-CN:') + 1]
        elif ms.count('application-label:') == 1:
            name = ms[ms.index('application-label:') + 1]
        elif ms.count('application: label=') == 1:
            name = ms[ms.index('application: label=') + 1]
        else:
            name = 'no label name'
        if ms.count('launchable-activity: name=') == 1:
            launch = ms[ms.index('launchable-activity: name=') + 1]
        else:
            launch = android_search_app_activity(pkg)
        package_list.append(','.join((pkg, name, launch)))

    write_string_to_file(android_apk_list, package_list,'utf8')
    return package_list


def android_aapt_get_app_info(app_path):
    cmd = ' '.join(('/data/local/tmp/aapt-arm-pie d badging', app_path, '|grep -E',
                    '\'package|launchable-activity|application-label\''))
    msg = (get_shell_output(['adb', 'shell'], cmd))
    return msg


def android_search_app_activity(app_package):
    cmd = ' '.join(('cmd package resolve-activity', app_package, '|grep name'))
    msg = (get_shell_output(['adb', 'shell'], cmd))
    if msg == '':
        msg = 'no activity info'
    else:
        msg = msg.replace('\r\n', '').split('name=')[1].strip()
    return msg


def android_search_package_by_name(app_name):
    read_list = list(read_file(android_apk_list, 'utf8').strip('][').replace('\'', '').split(', '))
    for rl in read_list:
        if rl.__contains__(app_name):
            return rl.split(',')[0],rl.split(',')[2]


def android_check_screen_is_locked():
    cmd = 'dumpsys window | grep mDreamingLockscreen'
    msg = (get_shell_output(['adb', 'shell'], cmd))
    return msg.__contains__('mDreamingLockscreen=true')


# pkg, laun = android_search_package_by_name('微信')
# print(pkg)
# print(laun)

def android_find_app_user_id(app_package):
    cmd = ''.join(('dumpsys package ',app_package,' | grep userId'))
    msg = get_shell_output(['adb', 'shell'], cmd)
    return msg


def android_backup_app_apk(app_package, backup_path):
    cmd = ''.join(('pm path ',app_package))
    msg = get_shell_output(['adb', 'shell'], cmd)
    cmd = ''.join(('adb pull ', msg.replace('package:','').strip(),' ', backup_path))
    get_command_output(cmd)



