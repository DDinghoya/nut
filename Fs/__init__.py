from Fs.Xci import Xci
from Fs.Nca import Nca
from Fs.Nsp import Nsp
from Fs.Rom import Rom
from Fs.Nacp import Nacp
from Fs.Pfs0 import Pfs0
from Fs.Ticket import Ticket
from Fs.Cnmt import Cnmt
from Fs.File import File

def factory(name):
	if name.endswith('.xci'):
		f = Xci()
	elif name.endswith('.nsp'):
		f = Nsp()
	elif name.endswith('.nsx'):
		f = Nsp()
	elif name.endswith('.nca'):
		f =  Nca()
	elif name.endswith('.nacp'):
		f =  Nacp()
	elif name.endswith('.tik'):
		f =  Ticket()
	elif name.endswith('.cnmt'):
		f =  Cnmt()
	else:
		f = File()

	return f