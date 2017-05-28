from terminal import Terminal
from host import Host
from network import Network
from files import Folder


f1 = Folder('home')

f2 = Folder('Documents')

f2.add_subfolder(Folder('python'))
f2.add_subfolder(Folder('cv'))

f3 = Folder('Music')

f3.add_subfolder(Folder('Death Grips'))
f3.add_subfolder(Folder('Franz Ferdinand'))
f3.add_subfolder(Folder('Skrillex'))
f4 = Folder('Ratatat')
f3.add_subfolder(f4)

f1.add_subfolder(f2)
f1.add_subfolder(f3)
f1.add_subfolder(Folder('Pictures'))

network = Network('Internet')
host = Host('jcd', 'jcd-l', 'dupa')
host2 = Host('nsa', '123.456.7.8', 'xkey')
network.add_host(host)
network.add_host(host2)
terminal = Terminal('jcd', host, f4)
host.terminal = terminal
host.connect()
