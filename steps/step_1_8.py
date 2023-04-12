import random


class Server:
    number = 1
    servers = []

    def __init__(self, buffer=[], link=''):
        self.buffer = buffer[:]
        self.ip = Server.number
        self.link = link
        Server.number += 1
        Server.servers.append(self)
    def send_data(self,data):  # для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);
        self.data = data
        Router(self.link).buffer.append(data)

    def get_data(self):  # возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список) и очищает входной буфер;
        a = self.buffer[:]
        self.buffer = []
        return a

    def get_ip(self):
        return self.ip


class Router:

    def __init__(self, links=[], buffer=[]):
        self.links = links  # список для хранения link_ов Routera
        self.buffer = buffer[:]  # список для хранения принятых от серверов пакетов (объектов класса Data).

    def link(self, servers):
        self.links.append(servers)
        servers.link = self
        # print (self)

    def unlink(self, servers):
        self.links.remove(servers)
        servers.link = ''

    def send_data(self):  # для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам (после отправки буфер должен очищаться)
        ips = [a.ip for a in self.links]
        for b in Server.servers:
            for a in self.buffer:
                if a.ip in ips:
                    if a.ip == b.ip:
                        b.buffer.append(a)
        self.buffer=[]

class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
# msg_lst_from = sv_from.get_data()
# msg_lst_to = sv_to.get_data()

#print(sv_from.buffer,sv_from.ip)


