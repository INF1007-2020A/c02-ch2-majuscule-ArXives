#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    distance_entre_min_et_maj = ord('a') - ord('A')
    resultat = ''
    for lettre in mot:
        # TODO completer la fonction ici
        if ord('a') <= ord(lettre) and ord(lettre) <= 122
        lettre = ord(lettre) - distance_entre_min_et_maj 
        resultat += chr(lettre)
    return resultat


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
