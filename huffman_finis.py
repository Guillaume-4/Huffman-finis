
from operator import attrgetter

class NOEUD:
    def __init__(self,gauche, carac, valeur,droite):
        self.carac = carac
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite


def table_frequences(p):
    dico = {}
    for i in p:
        if i in dico == False:
            dico[i] = 0
        dico[i] = dico.get(i, 0) + 1
    return dico



def creation_liste_feuille(dico):

    tab = []
    for i in dico:
        tab.append(NOEUD(None,i,dico[i],None))
    return tab

def recherche_min(tab):
    min = tab[0]
    for i in tab:
        if i.valeur<min.valeur:
            min = i
    return min


def creation_arbre(liste):
    while len(liste)>1:
        n1=recherche_min(liste)
        liste.remove(n1)
        n2= recherche_min(liste)
        liste.remove(n2)
        total = n1.valeur + n2.valeur
        new_noeud = NOEUD(n1,None,total,n2)
        liste.append(new_noeud)
    return liste[0]

def arbre_code(prefixe,arbre):
    global dico_code
    if arbre.gauche == None or arbre.droite == None:
        dico_code[arbre.carac] = prefixe

    else:
        arbre_code(prefixe + "1", arbre.gauche)
        arbre_code(prefixe+"0", arbre.droite)
        return dico_code

def fichier_ecrire(phrase_code, code):
    f = open("code.txt", "w")
    f.write(f"{phrase_code}")
    f.write("\n")
    for i in code:
        f.write(f"{i}:{code[i]};;")
    f.close
    return("code.txt")


def decoder(fichier):
    phrase = ""
    dico_decodage={}
    fichier = open(f"{fichier}","r")
    code_phrase = fichier.readline()
    code_lettre = fichier.readline()
    split_code = code_lettre.split(";;")
    split_code.pop(-1)
    split_phrase = code_phrase.split(" ")
    for i in split_code:
        lettre = i.split(":")
        dico_decodage[lettre[0]] = lettre[1]
    for mot in split_phrase:
        for key, value in dico_decodage.items():
            if value == mot:
                phrase = phrase + key
    return phrase



def encrypter_phrase(phrase, code):
    code_phrase = ''
    for i in phrase:
        for x in code:
            if x == i:
                code_phrase = f"{code_phrase + code[i]} "
    return code_phrase
    

dico_code = {}
phrase = "Mettez votre phrase ici"
dico_phrase = table_frequences(phrase)
feuille = creation_liste_feuille(dico_phrase)
arbre = creation_arbre(feuille)
code = arbre_code("",arbre)
encoder = encrypter_phrase(phrase,code)
fichier_code = fichier_ecrire(encoder, dico_code)
print(f"après décodage : {decoder(fichier_code)}")
#Noeud_Dessin.dessin_arbre(abr)

