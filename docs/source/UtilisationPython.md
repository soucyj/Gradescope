# Utilisation du programme Python

1. Enregistrez le fichier `gradescope.py` dans le même dossier que les fichiers CSV. [Cliquez ici](https://github.com/soucyj/Gradescope/blob/gh-pages/gradescope.py) pour accéder au contenu du programme.
2. Vous devriez voir quelque chose qui ressemble à ceci:

    ```{image} images/Github.png
    :alt: Github
    :width: 800px
    :align: center
    ```
    
    
3. Cliquez avec le bouton de droite sur le bouton **Raw**, puis enregristrez le fichier dans le même dossier que les fichiers CSV téléchargés précédemment. Conservez le même nom de fichier (`gradescope.py`).

4. Lors de la première utilisation, il faut s'assurer d'avoir le logiciel Python d'installé. Pour ce faire, rendez-vous sur li [site officiel de Python](https://www.python.org/). Cliquez sur **Dowloads** puis télécharger la version appropriée à votre système d'exploitation.

    ```{image} images/Download.png
    :alt: Download Python
    :width: 800px
    :align: center
    ```
    
    
5. Une fois le téléchargement terminé, lancez l'installation. Assurez-vous de cocher *Add Python 3.10 to PATH*.

    ```{image} images/Install.png
    :alt: Install Python
    :width: 800px
    :align: center
    ```
6. Il faut maintenant exécuter le programme `gradescope.py`. Pour les utilisateurs de Windows, utilisez l'application **Powershell** pour vous rendre dans le dossier où le programme est situé (là où les fichiers CSV devraient aussi être). Une fois que vous y êtes, exécutez-le en tappant `python gradescope.py`. **Attention!** Les seuls fichiers CSV qui doivent être dans le dossier où est exécuté le programme doivent être les fichiers CSV obtenus de monPortail (nommés 12345.csv, ou 12345 est un exemple de NRC) et le fichier CSV obtenu de Gradescope (qui contient la chaîne de caractères *scores* dans le nom).

    ```{image} images/Powershell.png
    :alt: Powershell
    :width: 800px
    :align: center
    ```

    
    ```{image} images/Commandes.png
    :alt: Commandes
    :width: 800px
    :align: center
    ```
    
    
7. Le programme devrait avoir généré un fichier intitulé `ToutesLesNotes.csv`. Dans ce fichier, vous retrouverez les notes ordonnées correctement pour être copiées/collées dans le fichier Excel provenant de monPortail. Il vous suffira par la suite de téléverser la nouveau fichier Excel vers monPortail.
