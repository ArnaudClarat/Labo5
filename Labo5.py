"""Nous allons réaliser un distributeur de boissons !
3 boissons disponibles ( 5 unités en stock au départ )
Afficher la liste des boissons disponible ( pas le nombre )
L'utilisateur fait le choix d'une boisson
La machine donne le prix de la boisson.
L'utilisateur entre des pièces ( 5, 10, 20, 50, 1 ou 2 €) jusqu'aux moments ou : on arrive, ou dépasse la somme demandée
La machine rend la monnaie pour arriver à la valeur de la boisson
La machine donne la boisson
Donner la possibilité de faire un inventaire des ventes (prix et nombre de boissons).
Cette action ferme la machine.

Plus loin ....
Vous devez gérer la monnaie de la machine (prévoir une quantité en stock de départ)
Si le rendu n'est pas possible (manque de monnaie en stock ) laissé le choix a l'utilisateur d'annuler la commande
L'inventaire affichera également le stock de monnaie pour le rendu (différent des payements)"""

import csv


def updateStock(choix):
    with open('stock.csv', 'w', newline='') as csvfile:
        a = 0


def payement(stock, choix):
    somme = 0
    prix = -2
    j = 0
    for i in stock:
        if i[0].lower() == choix:
            prix = float(i[1])
            pass
    if prix > 0 :
        print("Veuillez insérer", str(prix) + "€")
    if prix <= 0 :
        print("Erreur interne, retour au menu")
        affichage(stock)
    while somme < prix:
        j += 1
        if j == 1 :
             piece = input(str(j) + "ère pièce : ")
        else :
            piece = input(str(j) + "ème pièce : ")
        somme += float(piece)
    if somme > prix:
        aRendre = somme - prix
        print(str(aRendre) + "€ rendu")
    else :
        print("Reste", prix - somme, "euros à insérer")
    updateStock(choix)


def affichage(stock):
    print("")
    for i in stock:
        if int(i[2]) > 0:
            print("\t", i[0], ":", i[1] + "€")
    choix = input("\tQue voulez-vous boire? ").lower()
    while choix not in ["coca", "fanta", "ice tea"]:
        choix = input("Nous n'avons pas compris, veuiller réessayer. ")
    return choix


def main():
    choix = "aze"
    while choix.lower() != "inv":
        stock = []
        with open("stock.csv", 'r', newline='') as csvfile:
            file = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in file:
                stock.append(row)
        print("\nBienvenue dans ce distributeur de boisson!")
        choix = affichage(stock)
        payement(stock, choix)
    # TODO fonction inventaire

if __name__ == "__main__":
    main()
