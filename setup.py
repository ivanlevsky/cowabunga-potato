from setuptools import setup
# https://setuptools.readthedocs.io/en/latest/userguide/quickstart.html#transitioning-from-setup-py-to-setup-cfg/
# https://packaging.python.org/guides/distributing-packages-using-setuptools/

setup(
    name='cowabunga_potato',
    version='1.0',
    description='self use python module',
    long_description='ss',
    author='ivanlevsky',
    author_email='ivanlevsky@gmail.com',
    maintainer='ivanlevsky',
    maintainer_email='ivanlevsky@gmail.com',
    url='https://github.com/ivanlevsky/cowabunga-potato',
    package_data={
        'cowabunga_potato.opencv': ['*.dll'],
    },
    # exclude_package_data={
    #     '*': ['*.txt', '*.dll'],
    # },
    package_dir= {
        'cowabunga_potato': '.',
        'cowabunga_potato.appium_test': './appium_test',
        'cowabunga_potato.databases': './databases',
        'cowabunga_potato.http_request': './http_request',
        'cowabunga_potato.machine_learning': './machine_learning',
        'cowabunga_potato.machine_learning.extra': './machine_learning/extra',
        'cowabunga_potato.opencv': './opencv',
        'cowabunga_potato.python_common': './python_common',
        'cowabunga_potato.python_common.file_and_system': './python_common/file_and_system',
        'cowabunga_potato.python_common.graphic_and_sound': './python_common/graphic_and_sound',
        'cowabunga_potato.selenium_test': './selenium_test'
    },
    packages=[
        'cowabunga_potato',
        'cowabunga_potato.appium_test',
        'cowabunga_potato.databases',
        'cowabunga_potato.http_request',
        'cowabunga_potato.machine_learning',
        'cowabunga_potato.machine_learning.extra',
        'cowabunga_potato.opencv',
        'cowabunga_potato.python_common',
        'cowabunga_potato.python_common.file_and_system',
        'cowabunga_potato.python_common.graphic_and_sound',
        'cowabunga_potato.selenium_test'
    ],

    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing'
    ]

)
