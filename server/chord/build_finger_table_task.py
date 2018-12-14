from __future__ import absolute_import
import os
import ConfigParser

from grpc import insecure_channel
from server_side_pb2_grpc import P2PStub

from asyncService import AsyncService
from time import sleep
import sys


CONFIG = ConfigParser.ConfigParser()
CONFIG.read(os.path.dirname(__file__) + u'/../../config.py')

class Build_finger_table(AsyncService):

    def __init__(self, node):
        AsyncService.__init__(self)
        self.node = node
        self.wait_time = CONFIG.getint(u'p2p', u'SLEEP_BUILD_FT')


    def run(self):
        self.build_cluster_stubs()
        while not self.stopEvent.isSet():
            sleep(self.wait_time)
            # print("Building finger table...")
            self.node.chord.fill_finger_table()
            self.print_table()
            self.wait_time += 5

        self.stopEvent.clear()
        self.stopFinish.set()
        print u"Exiting build finger table..."

    def build_cluster_stubs(self):
        if not self.node.is_cluster_builded:
            aux = []
            for ip in self.node.ip_cluster:
                channel = insecure_channel(ip + ':' + self.node.cluster_port)
                stub = P2PStub(channel)
                aux.append(stub)
            self.node.cluster_table = aux
            self.node.is_cluster_builded = True

    def print_table(self):

        ft = self.node.fingerTable
        if len(ft) > 1:
            print u"\n"
            print u"My predecessor is ", ft[0][0]
            print u"My successor is   ", ft[1][0]

            if len(ft) > 2:
                print u"My finger table is [",; sys.stdout.write(u"")
                for i in xrange(1,len(ft)):
                    print ft[i][0],; sys.stdout.write(u"")
                    if i != len(ft)-1:
                        print u', ',; sys.stdout.write(u"")
                print u"]"
            else:
                print u"Finger Table empty"
            print u"\n"