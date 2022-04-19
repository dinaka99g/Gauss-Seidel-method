from pickle import APPEND
from re import X
import numpy as np
from matplotlib import pyplot as plt


A=np.array([[3,1,0],[1,5,1],[0,0,-1]]) #Unos elemenata matrice
b=[-3,-1,-1] #Unos vektora na desnoj strani sistema 
x=[0,0,0]#Početne vrijednosti
n=len(A)
print(A)


dijagonalna=True

for i in range (0,n): 
    suma=0
    for j in range (0,n):
        if i!=j:
            suma=suma+abs(A[i,j])
        if suma>abs(A[i,i]):
            dijagonalna=False
            break
    
        
    
if dijagonalna==False:
    print("****Matrica nije dijagonalno dominantna. Pokušajte ponovno.****")
elif dijagonalna==True:
  print("****Matrica je dijagonalno dominantna.****")
  print("Rješenje sistema Gauss-Seidelovom metodom je:")


def Gaus_Seidel (A,b,x,n):
  
 for i in range (0,n):
         suma=0
         for j in range(0, n):
          if i!=j:
            suma+=A[i,j]*x[j]
    
          x[i]=(1/A[i,i])*(b[i]-suma)
          
 return x


     
k=1
kmax=10

while k<=kmax and dijagonalna==True:
    x=Gaus_Seidel(A,b,x,n)
     
    print ("Iteracija: %3d %6.3f %6.3f %6.3f " % (k, *x ))

    k=k+1

print ()





       
        
        
        
    

        







          
            




















        




    
    
