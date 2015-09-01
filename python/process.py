from multiprocessing import Process
import os


def run_proc(name):
    print('run child process %s (%s)...' % (name, os.getpid()))

print('Parent process %s.' % os.getpid())
p = Process(target=run_proc, args=('test',))
print('child process will start.')
p.start()
p.join()
print('child process ends.')
