import random


class Server:
    def __init__(self, buffer=[], ip=random.randint(0, 10), link = ''):
        self.buffer = buffer
        self.ip = ip
        self.link = link

    def send_data(self,data):  # для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);
        self.data = data
        self.link.buffer.append(self.data)

    def get_data(self):  # возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список) и очищает входной буфер;
        a = self.buffer[:]
        self.buffer = []
        return a

    def get_ip(self):
        return self.ip


sv_from = Server()
sv_from2 = Server()
print(Server.)