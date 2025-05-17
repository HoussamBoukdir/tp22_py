def decompose_montant(montant):
    billets_pieces = [200, 100, 50, 20, 10, 5, 2, 1] 
    resultat = {}

    for valeur in billets_pieces:
        quantite = montant // valeur 
        if quantite > 0:
            resultat[valeur] = quantite
            montant %= valeur  

    return resultat

montant = 2978
decomposition = decompose_montant(montant)
for valeur, quantite in decomposition.items():
    print(f"Le nombre de {valeur} dirhams est : {quantite}")
