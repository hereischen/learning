# -*- coding: utf-8 -*-
import threading
from time import ctime, sleep


def music(name):
    for i in range(2):
        print "激情听歌 %s. 听完已经是 %s" % (name, ctime())
        sleep(2)


def movie(name):
    for i in range(2):
        print "激情看电影 %s. 看完已经是 %s" % (name, ctime())
        sleep(5)

threads = []
t1 = threading.Thread(target=music, args='七子之歌')
threads.append(t1)
t2 = threading.Thread(target=movie, args='荒野猎人')
threads.append(t2)
if __name__ == '__main__':
    for th in threads:
        th.setDaemon(True)
        th.start()

    print "完成>>>>> %s" % ctime()
