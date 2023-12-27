import requests
base_url = 'https://raw.githubusercontent.com/Uniuxify/ms_test4/main/'
response = requests.get(base_url + 'init.py')
init = response.text.split('\n\n')
response = requests.get(base_url + 'mu1.py')
mu1 = response.text.split('\n\n')
response = requests.get(base_url + 'mu2.py')
mu2 = response.text.split('\n\n')
response = requests.get(base_url + 'sigma1.py')
sigma1 = response.text.split('\n\n')
response = requests.get(base_url + 'sigma2.py')
sigma2 = response.text.split('\n\n')
response = requests.get(base_url + 'mumu.py')
mumu = response.text.split('\n\n')
response = requests.get(base_url + 'mumumu.py')
mumumu = response.text.split('\n\n')
del response
del base_url