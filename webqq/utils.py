# -*- coding:utf-8 -*-
__author__ = 'webber'
import Queue

class Chat(object):
    def __init__(self):
        self.msg_queue = Queue.Queue()

    def get_msg(self, request):
        new_msgs = []
        if self.msg_queue.qsize()>0:
            for msg in range(self.msg_queue.qsize()):
                new_msgs.append(self.msg_queue.get_nowait())
        else: # no new msg, but wait for 60 secs
            try:
                print "----no new msg----"
                new_msgs.append(self.msg_queue.get(timeout=60))
                print "I have recv new msg"
            except Queue.Empty:
                print "\033[32;1m Time out , no new msg for user [%s]\033[0m" % request.user.user_profile.name
        print "-----------> recv [%s] msg " % len(new_msgs)
        return new_msgs