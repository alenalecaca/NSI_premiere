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



########################ASYMETRIQUE###########################
def genere_clefs_publique_et_privee(a1, b1, a2, b2):
    M = a1 * b1 - 1
    e = a2 * M + a1
    d = b2 * M + b1
    n = (e * d - 1) // M
    clef_publique = (e, n)
    clef_privee = (d, n)
    return clef_publique, clef_privee

# Exemple simple
clef_publique, clef_privee = genere_clefs_publique_et_privee(5, 3, 7, 5)
print("Clé publique :", clef_publique)
print("Clé privée :", clef_privee)



def chiffre_message(message, clef_publique):
    e, n = clef_publique
    message_chiffre = []
    for caractere in message:
        ascii_caractere = ord(caractere)
        chiffre = (ascii_caractere * e) % n
        message_chiffre.append(chiffre)
    return message_chiffre

# Exemple de chiffrement avec la clé publique (103, 537)
message_chiffre = chiffre_message("a", (103, 537))
print("Message chiffré :", message_chiffre)



def dechiffre_message(message_chiffre, clef_privee):
    d, n = clef_privee
    message_dechiffre = ""
    for chiffre in message_chiffre:
        ascii_caractere = (chiffre * d) % n
        caractere = chr(ascii_caractere)
        message_dechiffre += caractere
    return message_dechiffre

# Exemple de déchiffrement
message_original = dechiffre_message([325], (73, 537))
print("Message déchiffré :", message_original)



def bruteForceKidRSA(e, n):
    for d in range(1, n):
        if (e * d - 1) % n == 0:
            return d
    return None

# Exemple d'attaque :
e = 53447
n = 5185112
d = bruteForceKidRSA(e, n)
print("Clé privée trouvée par force brute :", d)




def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(e, n):
    g, x, y = egcd(e, n)
    if g != 1:
        return None
    else:
        return x % n


e = 230884490440319
n = 194326240259798261076
d = modinv(e, n)
print("Clé privée trouvée avec Euclide étendu :", d)


# Q13:

# taille des clés couramment utilisées par RSA :
#   Actuellement, la taille standard pour sécuriser les données sur Internet avec RSA est généralement de 2048 bits. Pour une sécurité renforcée, certaines applications sensibles utilisent même des clés de 4096 bits.

# *Nouvelle technologie pouvant casser RSA rapidement :
#   La **technologie quantique** (ordinateurs quantiques) représente une menace sérieuse pour RSA. Un ordinateur quantique puissant pourrait casser le chiffrement RSA (en factorisant rapidement de grands nombres premiers) en quelques secondes ou minutes, là où un ordinateur classique prendrait des milliers d'années.

