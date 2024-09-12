# cook your dish here
from time import perf_counter

# SOMME RECURSIVE

def somme_rec(L):
    n = len(L)
    if n == 0:
        return 0
    else:
        return L[0] + somme_rec(L[1:])

L1 = [1, 8, 9, -3]


#TIMER 

debut = perf_counter()  
resultat_rec=somme_rec(L1)
fin = perf_counter()
print( "LE RESULTAT SOMME RECURSIVE",resultat_rec)
duree_rec = fin - debut 
print(f"La durée d'exécution pour somme_rec est de {duree_rec:.6f} secondes.")

#######################################################################################

#SOMME ITTERATIVE

def somme_iterative(L):
    n =len(L1)
    somme=0
    for i in range(n):
        somme += L[i]
    #print(somme)
    return(somme)
s = somme_iterative(L1)
print(s,"RESULTAT SOMME ITERATIVE")

#TIMER

debut = perf_counter()  
somme_iterative(L1)
fin = perf_counter() 
duree_itter = fin - debut 
print(f"La durée d'exécution pour somme_iterative est de {duree_itter:.6f} secondes.")

#######################################################################################

#RAPPORT ENTRE LES TEMPS

rapport=duree_itter/duree_rec
print(f"le rapport entre les deux temps est rapport {rapport:f} secondes. ")

#######################################################################################

# FONCTION FACTORIELLE

def facto_r(n):
    if n == 0:
        return 1
    else:
        return n * facto_r(n - 1)

n = 6  
print(facto_r(n) , "RESULTAT FONCTION FACTORIELLE")

#TIMER

debut = perf_counter()  
facto_r(36)  
fin = perf_counter()  

duree = fin - debut  
print(f"La durée d'exécution pour facto_r(36) est de {duree:.6f} secondes.")

######################################################################################
 
#FIBONACCI ITTERATIVE

def fibo_iter(n):
     " " " renvoie le n-ieme terme de la suite fibonnaci , n entier naturel type int " " "
     if n==0:
        return 0
     
     if n == 1:
        return 1 
     else:
        a=0
        b=1
     for i in range(1,n):
        c = a + b
        a = b 
        b = c
     return c 

print("TEST FIBO ITTERATIVE")

nb=35

print("n=", nb)
print(fibo_iter(nb))

#TIMER

debut = perf_counter()  
fibo_iter(nb)
fin = perf_counter() 
duree_iter = fin - debut 
print(f"La durée d'exécution pour Fibonacci est de {duree_iter:.6f} secondes.")
 
#######################################################################################

#FIBONACCI RECURSIVE 

def fibo_rec(n):
    if n == 0 :
        return 0
    elif n==1 :
        return 1
    else :
        return fibo_rec(n-1)+fibo_rec(n-2)

print("TEST FIBO RECURSIVE")


print("n=", nb)
print(fibo_rec(nb))

#TIMER

debut = perf_counter()  
fibo_rec(nb)
fin = perf_counter() 
duree_rec = fin - debut 
print(f"La durée d'exécution pour Fibonacci est de {duree_rec:.6f} secondes.")

##########################################################################################

#RAPPORT ENTRE LES TEMPS

rapport=duree_itter/duree_rec
print(f"le rapport entre les deux temps est rapport {rapport:f} secondes. ")
 
###########################################################################################
 
 
 