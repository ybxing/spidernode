#coding:utf-8
'''
Created on 2017年4月25日

@author: Administrator
'''
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
class machine():
    def __init__(self):
        self.interface=[]
        self.totalmemory,self.freememory,self.usedmemory=self.memory_stat()
        self.cpu=self.cpu_stat()
        self.loadavg=self.load_stat()
        self.getnetwork()
    
    def memory_stat(self):  
        mem = {}  
        with open("/proc/meminfo") as f:  
            lines = f.readlines()   
        for line in lines:  
            if len(line) < 2: continue  
            name = line.split(':')[0]  
            var = line.split(':')[1].split()[0]  
            mem[name] = long(var) * 1024.0  
        mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']  
        return  mem['MemTotal'],mem['MemFree'],mem['MemUsed']
    
    def cpu_stat(self):  
        cpu = []  
        cpuinfo = {}  
        with open("/proc/cpuinfo") as f:  
            lines = f.readlines()  
        for line in lines:  
            if line == '\n':  
                cpu.append(cpuinfo)  
                cpuinfo = {}  
            if len(line) < 2: continue  
            name = line.split(':')[0].rstrip()  
            var = line.split(':')[1]  
            cpuinfo[name] = var  
        return cpu  
    
    def load_stat(self): 
        loadavg = {} 
        with open("/proc/loadavg") as f: 
            con = f.read().split() 
        loadavg['lavg_1']=con[0] 
        loadavg['lavg_5']=con[1] 
        loadavg['lavg_15']=con[2] 
        loadavg['nr']=con[3] 
        loadavg['last_pid']=con[4] 
        return loadavg 
    
    def getnetwork(self):
        with open('/proc/net/dev') as f:
            ifstat = f.readlines()
        itftmp=[]
        for interface in  ifstat:
            interfacetmp=interface.split()
            if len(interfacetmp)!=17:
                continue
            itftmp.append({'name':interfacetmp[0],
                                       'rx':float(interfacetmp[1]),
                                       'tx':float(interfacetmp[9])
                })
        time.sleep(1)
        with open('/proc/net/dev') as f:
            fstat = f.readlines()
        for interface in  fstat:
            interfacetmp=interface.split()
            if len(interfacetmp)!=17:
                continue
            ifname=interfacetmp[0]
            for itf in itftmp:
                if itf['name'] == ifname:
                    self.interface.append({'name':ifname,
                    'rx':(float(interfacetmp[1])-itf['rx'])/1024,
                    'tx':(float(interfacetmp[9])-itf['tx'])/1024
                    })
    
    def updatestat(self):
        self.interface=[]
        self.totalmemory,self.freememory,self.usedmemory=self.memory_stat()
        self.cpu=self.cpu_stat()
        self.loadavg=self.load_stat()
        self.getnetwork()
    
    def updateloadavg(self):
        self.loadavg=self.load_stat()
        
    def updatememory(self):
        self.totalmemory,self.freememory,self.usedmemory=self.memory_stat()
    
    def updatecpu(self):
        self.cpu=self.cpu_stat()
    
    def updatenetwork(self):
        self.getnetwork()
        
if __name__ == '__main__':
    machine1=machine()
    machine1.getnetwork()
    for i in machine1.interface: 
        for key,value in i.items():
            print key,value
        
        
        