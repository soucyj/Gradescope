Gabarit LaTeX
--------------------------------

Pour optimiser l'utilisation de Gradescope, j'ai créer une classe de document LaTeX nommée tout simplement **Gradescope**. Son utilisation s'est avérée efficace jusqu'à maintenant. Elle comporte les éléments suivants, particulièrement important:

- Deux boîtes pour l'identification de la copie (une pour le nom et le prénom, une autre pour le matricule);
- Des cases à cocher pour bien identifier la section à laquelle l'étudiant est inscrit dans le cas de cours à plusieurs sections;
- Le total des points (globalement et à l'intérieur d'une question comportant des sous-questions) se cacul automatiquement (il s'agit d'une fonctionnalité héritée de la class `exam.cls`);
- Des directives importantes pour éviter quelques problèmes (ne pas écrire de solutions au verso, ne pas débrocher les copies, etc.);
- Une boîte au bas de chaque page pour que l'étudiant y inscrive ses initiales;
- Une page à la fin pour poursuivre la solution d'une question si l'étudiant manque d'espace.

Voici un exemple de résultat : `Examen.pdf <Examen.pdf>`_

Pour télécharger les fichiers nécessaires à la compilation (`Gradescope.cls`, `Examen.tex` et `logo.png`), téléchargez le fichier suivant : `Gabarit.zip <Gabarit.zip>`__
