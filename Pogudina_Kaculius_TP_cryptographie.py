# -*- coding: utf-8 -*-
"""
Question 1 : Démontrer la propriété (1) à l'aide de tables de vérité.

Propriété : XOR(XOR(A,B),B) = A (1) 
   ____________________________
   |                          |
   | A | B |A XOR B | B | XOR |
   |__________________________|
   | 0 | 0 |    0   | 0 |  0  |
   ----------------------------
   | 0 | 1 |    1   | 1 |  0  |
   ----------------------------
   | 1 | 0 |    1   | 0 |  1  |
   ----------------------------
   | 1 | 1 |    0   | 1 |  1  |
   ----------------------------
   

            

############################################


Question 2 : Convertisseur texte en binaire 
    
"""

def convertit_texte_en_binaire(texte):
    code_numero = [format(ord(char), '08b') for char in texte]
    
    
    return ''.join(code_numero)


resultat = convertit_texte_en_binaire("NSI")
print("le texte convertit en binaire est :",resultat)  


############################################
"""
Question 3 : Convertisseur binaire en entier base

"""


def convertit_binaire_vers_entier_base_10(binaire):
    return int(binaire,2)

resultat = convertit_binaire_vers_entier_base_10("010100")
print("le binaire convertit en entier de base 10 est:",resultat)

###############################################

"""
Question 4 : Convertit binaire en texte 
"""

def convertit_binaire_en_texte(chaine_binaire):
    
    texte = ''
    for i in range(0,len(chaine_binaire),8):
        o = chaine_binaire[i:i+8]
        char = chr(int(o,2))
        texte += char 
    return texte 

print(convertit_binaire_en_texte("010011100101001101001001"))



####################################################


