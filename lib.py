import sqlite3
from sqlite3 import Error


def triBulleAsc(tab):
    """
	Trier les élements d'un tableau par ordre croissant
	:param tab: = Tableau à trier
	:param tab = Tableau à trier:
	:return = Tableau trié:
	"""
    t = tab.copy()
    test = True
    while test:
        test = False
        for i in range(len(t) - 1):
            if t[i] > t[i + 1]:
                temp = t[i]
                t[i] = t[i + 1]
                t[i + 1] = temp
                test = True
    return t


def triBulleDesc(tab):
    """
	Trier les élements d'un tableau par ordre décroissant
	:param tab:
	:param tab = Tableau à trier:
	:return = Tableau trié:
	"""
    t = tab.copy()
    test = True
    while test:
        test = False
        for i in range(len(t) - 1):
            if t[i] < t[i + 1]:
                temp = t[i]
                t[i] = t[i + 1]
                t[i + 1] = temp
                test = True
    return t


def connexion(base):
    """
	Créer une connexion en SQLite sur la
	base de données passée en paramètre
	:param base = nom de la base de donnée :
	:return = la connexion et le curseur :
	"""
    try:
        db = sqlite3.connect(base)
        cur = db.cursor()
        return db, cur
    except Error as e:
        print(e)
        return None


def division(nbr1, nbr2):
    """
	Diviser deux nombres entre eux
	en évitant les erreurs
	:param nbr1:
	:param nbr2:
	:return:
	"""
    global result
    try:
        result = nbr1 / nbr2
    except:
        result = "Division impossible"
    finally:
        return result


def numOnly(string):
    """
	Fonction qui retourne seulement
	les valeurs numériques d'une chaine
	:return Chaine composée uniquement des chiffres:
	"""
    retour = ""
    for i in string:
        if i.isdecimal():
            retour += i
    return retour


def moyenne(tab):
    """
    Retourne la moyenne de valeurs stockées dans un tableau
    :param tab:
    :param tab = tableau:
    :return = Moyenne:
    """
    nbrNotes = len(tab)
    somme = 0
    for i in range(nbrNotes):
        somme += int(tab[i])
    moyenne = somme / nbrNotes
    return moyenne


def isfloat(value):
    """
	Vérification du type de la valeur
	source: stackoverflow
	:param value = Valeur à vérifier:
	:return = True/False:
	"""
    try:
        float(value)
        return True
    except:
        return False


def isint(value):
    """
	Vérification du type de la valeur
	:param value = Valeur à vérifier:
	:return = True/False:
	"""
    try:
        value + 2
        return True
    except:
        return False


def calculIMC(height, weight):
    """
	Calcul l'imc avec la taille et le poids
	:param height = Taille en mètres:
	:param weight = Poids en kilos:
	:return = imc:
	"""
    imc = float(weight) / (float(height) ** 2)
    return imc


def verifVCS(VCS):
    """
	Vérifie numéro VCS (str via numOnly)
	:param VCS = string ne contenant que les chiffres:
	:return = True : Code bon / False : Code mauvais:
	"""
    # Vérification longeur num
    if len(VCS) != 12:
        return False
    # Séparation Dividende(8) et Contrôle(2)
    div = int(VCS[:len(VCS) - 2])
    cont = int(VCS[len(VCS) - 2:])
    print(div)
    print(cont)
    return (div % 97 == cont or (div % 97 == 0 and cont == 97))


def verifNumID(NumID):
    """
	Vérifie numéro ID belge (str via numOnly)
	:param NumID = string ne contenant que les chiffres:
	:return = True : ID bon / False : ID mauvais:
	"""
    num = numOnly(NumID)
    # Vérification longeur num
    if len(num) != 10:
        return False
    # Séparation Dividende(8) et Contrôle(2)
    div = int(num[:len(num) - 2])
    cont = int(num[len(num) - 2:])
    # Test
    return div % 97 == 97 - cont

typoError = "Nous n'avons pas compris, veuiller réessayer. "
if __name__ == "__main__":
    print("Ceci n'est qu'un ensemble de fonctions sans rien d'éxecutable.")
