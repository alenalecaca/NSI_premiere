# -*- coding: utf-8 -*-
https://hmalherbe.fr/thalesm/gestclasse/documents/Terminale_NSI/2020-2021/TP/TP_Term_NSI_cryptographie/TP_Term_NSI_cryptographie.html


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
 
 aide personelle : 
 
   A.  ou.   B.     =
   0         0      0
   1.        0      1
   0         1      1 
   1         1      1
   
 
############################################


Question 2 : Convertisseur texte en binaire 
    
"""

def convertit_texte_en_binaire(texte):
    binaire = ''
    for char in texte:
        code = format(ord(char), '08b')
        binaire += code
    return binaire

print("conversion texte en binaire : ",convertit_texte_en_binaire("SPECIALITE NSI"))



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

print("conversion du binaire en texte : ",convertit_binaire_en_texte("010011100101001101001001"))



####################################################
""" 
Question 5 : Chiffrer la chaine binaire en message chiffre 

"""
def chiffre_xor(chaine_binaire,clef_binaire) : 
    resultat = ''
    index_cle = 0 
    for char in chaine_binaire:
        bit=int(clef_binaire[index_cle])^int(char)
        resultat += str(bit)
        index_cle += 1
        if index_cle == len(clef_binaire):
            index_cle = 0 
            
    return resultat
        
######################################
message = "SPECIALITE NSI"
clef = "TERM"
message_binaire = convertit_texte_en_binaire(message)
print(message,"en binaire",message_binaire)
clef_binaire = convertit_texte_en_binaire(clef)
print(clef,"en binaire",clef_binaire)
message_binaire_chiffre = chiffre_xor(message_binaire,clef_binaire)
print("message chiffré",message_binaire_chiffre)
message_binaire_dechiffre = chiffre_xor(message_binaire_chiffre,clef_binaire)
print("message_binaire_dechiffre",message_binaire_dechiffre)
print("message dechiffré en ASCII",convertit_binaire_en_texte(message_binaire_dechiffre))



