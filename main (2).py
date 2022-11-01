from random import randint
import time

vertices = 10
arestasMin = 0
arestasMax = 3

repetições = 1

randintMin = 1
randintMax = 100

verticesList=[]
arr=[]
pesos=[]

for repet in range(repetições):
  
  start_time = time.time()
  
  for y in range(vertices):
    pesosTemp=[]
    arrTemp=[]
    z=randint(randintMin,randintMax)
    verticesList.append(z)
    arrTemp.append(z)
    for x in range(randint(arestasMin,arestasMax)):
      
      pesosTemp.append(randint(1,vertices))
      arrTemp.append(randint(randintMin,randintMax))
    arr.append(arrTemp)
    pesos.append(pesosTemp)
  #print(arr, '\n' ,pesos,'bbbbbbbbbbbbbb', pesosTemp, 'cccccccccccc',verticesList)


  sorthestpath=[]
  pesos2=[]
  for x in range(len(arr)):
    sorthestpathTemp=[]
    pesos2Temp=[]
    for y in range(len(arr[x])):
      
      if arr[x][y] in verticesList and y!=0:
        try:
          sorthestpathTemp.append(arr[x][0])
          sorthestpathTemp.append(arr[x][y])
          pesos2Temp.append(pesos[x][y-1])
        
        except:
          break
    pesos2.append(pesos2Temp)
    sorthestpath.append(sorthestpathTemp)
        
print('Caminhos entre A e B: ')
print(sorthestpath)
print('Menor Caminho: ')
print(pesos2)