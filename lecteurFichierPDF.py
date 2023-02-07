#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader

"""
Fonction permettant la lecture du document PDF
et la récupération des informations de celui-ci.
"""
def lecteurPDF(fichier):
    print("Analyse de " + fichier + " en cours ..." )

    #Récupération du nom du document
    NOM_FICHIER = extractionNomFichier(fichier)
    print(NOM_FICHIER)
    
    #Lecture du fichier pdf
    try:
        lecteur = PdfReader(fichier)
    except:
        print(fichier + " introuvable")
        return 
    
    #Récupération des informations du fichier
    info = lecteur.metadata
    titre = info.title
    auteurs = info.author

    #Récupération du texte
    #TODO Distinguer les différents paragraphes.
    nb_page = len(lecteur.pages)
    page = lecteur.pages[0]
    text = page.extract_text()
    #print(text)


def extractionNomFichier(fichier):
    return fichier.split('/')[-1]  #.split('.')[0] Pour retirer le '.pdf'