from distutils.core import setup
import py2exe

setup(console=['cameraMonitor.py'], data_files=[('.', ['config.ini', ])])
