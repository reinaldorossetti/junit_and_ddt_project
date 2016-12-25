from subprocess import Popen
import glob

tests = glob.glob('test_login.py')
processes = []
for test in tests:
    processes.append(Popen('nosetests --with-json-extended -q -s %s' % test, shell=True))

for process in processes:
    process.wait()
