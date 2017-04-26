#coding:utf-8
'''
Created on 2017年4月26日

@author: Administrator
'''
import os
class datasrc():
    def __init__(self):
        self.conn
        self.table
        self.thdata
        
    def getcon(self):
        return self.conn
    
    def gettable(self):
        return self.table
    
    def getdata(self):
        return self.thdata