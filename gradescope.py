# -*- coding: utf-8 -*-
"""
    Nom du fichier: gradescope.py
    Auteur: Jérôme Soucy
    Date de création: 2022-05-05
    Dernière modification: 2022-06-09
    Python Version: 3.9
"""

"""
Créer une liste de notes pouvant être exportée vers monPortail à partir
de Gradescope. L'utilisateur doit déposer dans le même dossier que ce
fichier .py les éléments suivants:
    - Un ou des fichiers CSV nommés A.csv, B.csv, etc.
    - Un fichier nommé obligatoirement deGS.csv.
Les fichiers de type A.csv sont les exportations des pages du classeur
obtenu de monPortail. Le fichier deGS.csv est celui obtenu de Gradescope.
"""

import csv
import os
"""
Identification du fichier provenant de Gradescope. Normalement il contient
la chaîne de caractère dans le nom, d'ou l'importance de ne pas le renommer.
"""
PATH = os.path.dirname(os.path.realpath(__file__))
for root, dirs, files in os.walk(PATH):
    for file in files:
        if "scores" in file:
             fichierGS=file
             break

"""
La fonction prend un contenu CSV en entrée et un chaîne. Elle retourne le 
numéro de la colonne (débute à la colonne 0) où la chaîne apparaît pour la 
première fois. Utile pour identifier la colonne où se trouve le matricule et 
le résultat.
"""
def TrouverColonne(CSVFile, string):
    FichierOuvert=open(CSVFile)
    ContenuCSV=csv.reader(FichierOuvert)
    for rowCSV in ContenuCSV:
        for x in range(len(rowCSV)):
            if rowCSV[x]==string:
                FichierOuvert.close()
                return x

"""
Fonction qui prend comme arguments deux fichiers CSV : l'un correspondant
à la feuille du classeur Excel correspondant à une section donnée et l'autre
provenant de Gradescope (commun à toutes les sections).

fOut est un fichier ouvert en écriture dans lequel on ira inscrire les éléments
suivants : 
    - le NRC de la section
    - la liste des étudiants de la section (nom+matricule+note). Si l'étudiant
      a abandonné et qu'il a eu une note dans Gradescope, elle est substituée
      par une chaîne vide, car monPortail refuse d'attribuer une note à un
      étudiant qui a abandonné.
    - La liste ListeManquante regroupe tous les étudiants qui n'ont pas
      abandonné le cours, mais qui n'ont pas de note dans Gradescope. Ils ont
      peut-être droit à une reprise. Utile pour s'assurer que les copies ont
      toutes été numérisées.
"""
def WriteSection(fichierUL, fichierGS):
    ColonneScore=TrouverColonne(fichierGS, "Total Score")
    ColonneMatriculeGS=TrouverColonne(fichierGS, "SID")
    ColonneMatriculeUL=TrouverColonne(fichierUL, "Identifiant")
    ColonneNomUL=TrouverColonne(fichierUL, "Nom")
    fOut.write("Section "+fichierUL[0:-4]+"\n")
    listeManquante=[]
    fUL=open(fichierUL)
    csv_fUL=csv.reader(fUL)
    for rowUL in csv_fUL:
        if len(rowUL[ColonneMatriculeUL])==9:
            NoteExistante=0
            fGS=open(fichierGS)
            csv_fGS=csv.reader(fGS)
            for rowGS in csv_fGS:
                if not("Abandon") in rowUL[ColonneNomUL] and rowUL[ColonneMatriculeUL]==rowGS[ColonneMatriculeGS] and rowGS[ColonneScore]!="":
                    NoteExistante=1
                    fOut.write(rowUL[ColonneNomUL])
                    fOut.write(",")
                    fOut.write(rowUL[ColonneMatriculeUL])
                    fOut.write(",")
                    fOut.write(rowGS[ColonneScore])
                    fOut.write("\n")
                    break
            fGS.close()
            if NoteExistante==0:
                fOut.write(rowUL[ColonneNomUL])
                fOut.write(",")
                fOut.write(rowUL[ColonneMatriculeUL])
                fOut.write(",")
                fOut.write("\n")
                fGS.close()
                if not("Abandon") in rowUL[ColonneNomUL]:
                    listeManquante+=[[rowUL[ColonneNomUL],rowUL[ColonneMatriculeUL]]]
    fUL.close()
    fOut.write("\n")
    if len(listeManquante)==0:
        fOut.write("Tous les étudiants de cette section encore inscrits au cours on une note d'attribuée.\n")
    else:
        fOut.write("Les étudiants ci-dessous sont encore inscrits au cours mais n'ont pas de résultat d'attribué.\n")
        for etudiant in listeManquante:
            fOut.write(etudiant[0]+","+etudiant[1]+","+"\n")
    fOut.write("\n")

"""
La liste ListeSection regroupe les fichiers CSV qui ne contiennent pas
la chaîne "score". Normalement il s'agit des fichiers CSV obtenu de monportail.
""" 
ListeSection=[]
for root, dirs, files in os.walk(PATH):
    for file in files:
        if not("scores") in file and file.endswith(".csv"):
             ListeSection+=[file]

"""
Le fichier "ToutesLesNotes.csv" est celui qui contiendra l'information à être
copier/coller dans le fichier Excel que monPortail doit recevoir. Les notes des
étudiants de toutes les sections sont placées dans le même fichier pour limiter
l'ouverture/fermeture de différents fichiers.
"""
fOut=open("ToutesLesNotes.csv","w")
for fichierUL in ListeSection:
    WriteSection(fichierUL, fichierGS)
fOut.close()