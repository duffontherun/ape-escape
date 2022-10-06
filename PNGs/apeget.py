import os

for x in range(0,10001):
  print(x)
  os.system("wget https://storage.googleapis.com/nftimagebucket/tokens/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/%s.png &" % x)
