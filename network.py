

class Network(object):

    def __init__(self, name):
        self.name = name
        self.hosts = []

    def add_host(self, host):
        self.hosts.append(host)
        host.network = self

    def get_host(self, address):
        for h in self.hosts:
            if h.name == address:
                return h
        return None
