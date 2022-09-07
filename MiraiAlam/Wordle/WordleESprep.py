import random

x=open("castellano.txt","r")
p=x.readlines()
x.close()

class color: 
  green = '\033[92m' 
  yellow = '\033[93m' 
  end = '\033[0m' 

palabras5=[]
palabras6=[]
palabras7=[]
for i in p:
    i=i.replace("\n","")
    i=i.lower()
    if len(i)==5:
      if "á" in i or "é" in i or "í" in i or "ó" in i or "ú" in i:
        i=i.replace("á","a")
        i=i.replace("é","e")
        i=i.replace("í","i")
        i=i.replace("ó","o")
        i=i.replace("ú","u")
      palabras5.append(i)
    elif len(i)==6:
      if "á" in i or "é" in i or "í" in i or "ó" in i or "ú" in i:
        i=i.replace("á","a")
        i=i.replace("é","e")
        i=i.replace("í","i")
        i=i.replace("ó","o")
        i=i.replace("ú","u")
      palabras6.append(i)
    elif len(i)==7:
      if "á" in i or "é" in i or "í" in i or "ó" in i or "ú" in i:
        i=i.replace("á","a")
        i=i.replace("é","e")
        i=i.replace("í","i")
        i=i.replace("ó","o")
        i=i.replace("ú","u")
      palabras7.append(i)
    else:
      pass
