from urllib.request import urlopen
base_url = 'https://raw.githubusercontent.com/Uniuxify/ms_test4/main/'
with urlopen(base_url + 'init.py') as response:
	_init = response.read().decode().split('\n\n')
with urlopen(base_url + 'mu1.py') as response:
	_mu1 = response.read().decode().split('\n\n')
with urlopen(base_url + 'mu2.py') as response:
	_mu2 = response.read().decode().split('\n\n')
with urlopen(base_url + 'sigma1.py') as response:
	_sigma1 = response.read().decode().split('\n\n')
with urlopen(base_url + 'sigma2.py') as response:
	_sigma2 = response.read().decode().split('\n\n')
with urlopen(base_url + 'mumu.py') as response:
	_mumu = response.read().decode().split('\n\n')
with urlopen(base_url + 'mumumu.py') as response:
	_mumumu = response.read().decode().split('\n\n')
del response
del base_url
del urlopen