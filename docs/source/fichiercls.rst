============================
Le fichier Gradescope.cls
============================

Le fichier **Gradescope.cls** est une classe personnalisée qui regroupe les éléments suivants:

- Elle appelle les paquets nécessaires à la compilation du document maître, soit le fichier **Examen.tex**.
- On y définit certains éléments qui pourront être utilisé dans le document maître. Par exemple, on définit la commande `\boite` qui prend deux arguments pour faire une boîte de réponse.
- Elle précise la mise en page (en-tête, pied de page, caractéristiques de l'évaluation, etc.)

Voici les premières lignes du fichier, qui précisent notamment les paquets inclus:

.. code:: none

    \NeedsTeXFormat{LaTeX2e}
    \ProvidesClass{Gradescope}
    \LoadClass[10pt]{exam}
        \pointsinmargin
    \RequirePackage{amsmath}
    \RequirePackage[french]{babel}
    \RequirePackage[T1]{fontenc}
    \RequirePackage[utf8]{inputenc}
    \RequirePackage[margin=2cm,bottom=2.5cm]{geometry}
    \RequirePackage{etoolbox}   % Pour utiliser \AtBeginDocument
    \RequirePackage{calc}       % Pour faire des calculs de largeur de minipage
    \RequirePackage{tikz}

Vous pouvez accéder au fichier en `cliquant ici <https://github.com/soucyj/Gradescope/blob/main/Gradescope.cls>`_ .