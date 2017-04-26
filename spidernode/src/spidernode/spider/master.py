#coding:utf-8
'''
Created on 2017年1月13日

@author: Administrator
'''
from SimpleXMLRPCServer import SimpleXMLRPCServer 
from ..datasrc import datasrc
class simplemaster():
    def __init__(self,ip,port,datasrc):
        self.ip=ip
        self.port=port
        self.putdict={}
        self.server = SimpleXMLRPCServer((self.ip, self.port))   
        print "Listening on port 8000..." 
        self.server.register_multicall_functions()   
        self.server.register_function(self.add, 'add')   
        self.server.register_function(self.subtract, 'subtract')   
        self.server.register_function(self.multiply, 'multiply')   
        self.server.register_function(self.divide, 'divide')   
        self.server.register_function(self.getdata, 'getdata') 
        self.server.register_function(self.curstatus, 'curstatus') 
        self.server.register_function(self.deldata, 'deldata') 
        self.datasrc=datasrc
         
    def add(self,x,y):   
        return x+y   
        
    def subtract(self,x, y):   
        return x-y   
        
    def multiply(self,x, y):   
        return x*y   
        
    def divide(self,x, y):   
        return x/y 
    
    def getdata(self):
        return datasrc.getdata(self)
    
    def curstatus(self):
        return len(self.putdict)
    
    def deldata(self,x):
        self.putdict.pop(x)
        print len(self.putdict)
        return len(self.putdict)
        
    def start(self):
        self.server.serve_forever()
if __name__ == '__main__':
    master = simplemaster('127.0.0.1',8000)
    master.start()
    # A simple server with simple arithmetic functions   
    