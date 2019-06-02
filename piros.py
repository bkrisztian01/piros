import urllib
import os, glob
from PIL import Image

sorok = 0
with open('kepek.txt') as f:
    sorok = sum(1 for _ in f)
if not os.path.exists('kepek'):
    os.makedirs('kepek')

remfajl=glob.glob('kepek\\*.png')

for i in remfajl:
	os.remove(i)

fajlnevek=['kepek\\'+str(i)+".png" for i in range(sorok)]

f=open("kepek.txt")
for i in range(sorok):
	temp=f.readline()
	if temp[0:2]=="//":
		temp="http:"+temp
	urllib.urlretrieve(temp,fajlnevek[i])

piros=[]
for i in range(sorok):
	img = Image.open(fajlnevek[i])
	img=img.convert('RGB')
	piros.append([0,i])
	counter=0
	for j in img.getdata():
		piros[i][0]+=j[0]
		counter+=sum(j)
	piros[i][0]=float(piros[i][0])/counter

piros=sorted(piros,reverse=True)

fajlnevek2=['kepek\\0'+str(i)+".png" for i in range(sorok)]
for i in range(sorok):
	os.rename(fajlnevek[piros[i][1]],fajlnevek2[i])

print piros