#coding:utf-8
'''
Created on 2017年2月7日

@author: Administrator
'''
import subprocess
import errno
from threading import Timer
import  threading 
import multiprocessing
import xmlrpclib
import urllib
kill = lambda process: process.kill()
def _eintr_retry_call(func, *args):
    while True:
        try:
            return func(*args)
        except (OSError, IOError) as e:
            if e.errno == errno.EINTR:
                continue
            raise
def getdata(i):
    result=urllib.urlopen(i)
    return i,result
if __name__ == '__main__':
    proxy = xmlrpclib.ServerProxy("http://localhost:8000")
    multicall = xmlrpclib.MultiCall(proxy)   
    multicall.getdata()
    result = multicall() 
    hostlist= tuple(result)
    for i in hostlist[0]:
        cmd = ["ping", i]
#         ping = subprocess.Popen(
#         cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process = multiprocessing.Process(target=getdata,args=(i,))
#         process.start()
        my_timer = Timer(5, kill, [process])
        try:
            
            my_timer.start()
            stdout1= []
        #     print dir(ping.stdout)
        #     stdout_thread = threading.Thread(target=ping._readerthread,
        #                                      args=(ping.stdout, stdout1))
        #     stdout_thread.setDaemon(True)
        #     stdout_thread.start()
        #     stdout_thread.join()
        #     print stdout1
            stdout, stderr = ping.communicate()
            print stdout
        finally:
            my_timer.cancel()