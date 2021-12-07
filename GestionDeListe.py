
if __name__ == '__main__':
    liste = [17, 38, 10, 25, 72]
    print("Liste à trier : " + str(liste))

    # Trier la liste et l'afficher
    liste_triee = sorted(liste)
    print("Liste triée : " + str(liste_triee))

    # Ajout d'un élément à la liste et l'afficher
    liste_triee.append(12)
    liste_triee = sorted(liste_triee)
    print("Liste triée avec ajout de la valeur 12 : " + str(liste_triee))

    # Affichage de l'indice de l'élément 17
    print("L'élément 17 est positionné à l'indice " + str(liste_triee.index(17)))