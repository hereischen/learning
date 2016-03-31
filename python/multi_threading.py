# -*- coding: utf-8 -*-
from time import ctime, sleep


def music():
    for i in range(2):
        print "激情听歌 %s" % ctime()
        sleep(2)


def move():
    for i in range(2):
        print "激情看电影 %s" % ctime()
        sleep(5)

if __name__ == '__main__':
    music()
    move()
    print "完成>>>>> %s" % ctime()
