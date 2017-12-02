#!/usr/bin/python
#-*- coding:utf8 -*-
import os,re,json

class bond():
    def __init__(self,name,ports):
        self.bond_name = name
        self.bond_ports = ports
        self.__path__ = "/etc/sysconfig/network-scripts/"
    def add(self):
        for x in self.ports:
                print x
    def del_bond(name):
        ports = self.get_bond(name)
        # print ports
        if name and len(ports) == 1:
            # print ports
            bond_file = path + "ifcfg-" + "".join(ports).split(" ", 1)[0]
            # print bond_file
            try:
                os.remove(bond_file)
            except OSError:
                return "Bond_file is not exist"
                # os.rename('path,"ifg-","".join(ports).split(" ",1)[0]','path,ifcfg-bond11')
            for port in "".join(ports).split(" ", 1)[1].split(","):
                print port
            return "SUCESSFUL"
        else:
            # print "not"
            return "bond can`t be null or isn`t exist"

    def get_bond(self,name):
        if name:
            bond_name =name
        bonds = []
        path = self.__path__
        port_file = os.listdir(path)
        master = "MASTER="+self.name
        print master
        bond_port_list = []
        port = self.name
        for e in port_file:
            if os.path.isfile(path + e):
                try:
                    f = open(path + e, 'r')
                    if master in f.read():
                        bond_port_list.append(e)
                except:
                    return "File of ports read error"
                finally:
                    f.close()
        bond_detail = {"name":self.name,"list":bond_port_list}
        bonds.append(bond_detail)
        result =json.dumps(bonds)
        return result


bond_port = ["ens1","ens2"]
bond = bond(name="bond0",ports=bond_port)
bond.add()
print bond.query_bond()



