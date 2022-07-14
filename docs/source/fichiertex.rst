Le fichier Examen.tex
--------------------------------

Le fichier **Examen.tex** est le document maître dont la compilation avec PDFLaTeX génère le PDF de l'examen à imprimer.

- On débute par définir les attributs de l'évaluation (nom de l'évaluation, cours concerné, durée, pondération, enseignants, etc.).
- On y précise les directives.
- On écrit les questions.
- Une page supplémentaire est générée pour poursuivre les solutions.

Voici les premières lignes du fichier dans le cas d'un cour à section unique coordonné par l'enseignant:

.. code:: none

    \def\SigleNumero{MAT-1906}
    \def\NomCours{Géométrie pour l'enseignement au préscolaire/primaire}
    \def\DateEvaluation{16 juin 2022 de 12h30 à 15h20}
    \def\Session{Été 2022}
    \def\NomEvaluation{Examen 3}
    \def\Ponderation{35}
    \def\Enseignante{}            % Lorsque le cours n'est pas à section multiple, indiquez le nom de l'enseignante
    \def\Enseignant{Jérôme Soucy} % Lorsque le cours n'est pas à section multiple, indiquez le nom de l'enseignant
    \def\Coordonnatrice{}         % Ne rien mettre entre les accolades si l'enseignant ou l'enseignante coordonne le cours
    \def\Coordonnateur{}          % Ne rien mettre entre les accolades si l'enseignant ou l'enseignante coordonne le cours
    \def\SectionA{}               % Ne rien mettre entre les accolades s'il s'agit d'un cours à section unique
    \def\SectionB{}               % Mettre le nom de chacun des enseignants et enseignantes entre les accolades
    \def\SectionC{}               % Une case à cocher sera générée pour chacune des sections (dès qu'il y en a 2)
    \def\SectionD{}
    \def\PapierLegal{}            % Écrire quelque chose entre les accolades pour imprimer sur du papier de formal légal
                                  % Le formal légal n'est pas recommandé pour les cours du SSE. Parfois les surveillants
                                  % n'ont pas accès à ce format de papier.

Voici les premières lignes du fichier dans le cas d'un cour à plusieurs sections:

.. code:: none

    \def\SigleNumero{MAT-1900}
    \def\NomCours{Mathématiques de l'ingénieur 1}
    \def\DateEvaluation{5 novembre 2021 de 18h30 à 21h00}
    \def\Session{Automne 2021}
    \def\NomEvaluation{Examen 2}
    \def\EnLigne{}                  % Écrivez quelque chose entre les accolades pour qu'apparaissent une attestation sur l'honneur
    \def\Ponderation{35}
    \def\Enseignante{}              % Lorsque le cours n'est pas à section multiple, indiquez le nom de l'enseignante
    \def\Enseignant{}               % Lorsque le cours n'est pas à section multiple, indiquez le nom de l'enseignant
    \def\Coordonnatrice{}           % Ne rien mettre entre les accolades si l'enseignant ou l'enseignante coordonne le cours
    \def\Coordonnateur{Félix Kwok}  % Ne rien mettre entre les accolades si l'enseignant ou l'enseignante coordonne le cours
    \def\SectionA{Félix Kwok}       % Ne rien mettre entre les accolades s'il s'agit d'un cours à section unique
    \def\SectionB{Jérôme Soucy}     % Mettre le nom de chacun des enseignants et enseignantes entre les accolades
    \def\SectionC{Maëva Ostermann}  % Une case à cocher sera générée pour chacune des sections (dès qu'il y en a 2)
    \def\SectionD{Rachid Kandri-Rody}
    \def\PapierLegal{}              % Écrire quelque chose entre les accolades pour imprimer sur du papier de formal légal
                                    % Le formal légal n'est pas recommandé pour les cours du SSE. Parfois les surveillants
                                    % n'ont pas accès à ce format de papier.

On définit ensuite les directives de l'examen:

.. code:: none

    \def\Directives{
    \begin{enumerate}
    \item Assurez-vous que cette \'evaluation comporte \numquestions ~questions réparties sur 
          \numpages~pages. Elle sera notée sur \numpoints.
    \item Le verso des feuilles peut être utilisé comme brouillon, \textbf{mais il ne sera pas 
          corrigé}.
    \item La dernière page de l'examen peut être utilisée comme brouillon ou pour compléter 
          une solution. Par exemple, si vous souhaitez y poursuivre la solution de la 
          question 1, \textbf{indiquez dans la zone de réponse de la question 1 que la suite 
          se trouve à la dernière page}.
    \item Aucune page de cet examen (y compris la page \numpages) ne doit être débrochée.
    \item Assurez-vous d'identifier correctement votre copie en plus d'inscrire vos initiales
          au bas des pages 2 à \numpages.
    \item Veuillez déposer une carte d'identité avec photo sur le coin du bureau où vous 
          rédigez l'examen.
    \item Sauf indication contraire, vous devez justifier votre raisonnement.
    \item Une feuille de résultats choisis sera distribuée avec l'examen.
    \item Tout autre document est interdit.
    \item Une calculatrice de base est autorisée. On entend par là une calculatrice avec des 
          fonctionnalités comparables ou inférieures à la Casio FX-55 Plus.
    \item Dans tous les cas où c'est possible, vous devez écrire la valeur exacte et non une 
          valeur numérique approchée (par exemple, si $x^2=2$ et $x>0$, vous devez écrire 
          $x=\sqrt{2}$ plutôt que  $x\approx 1,414$).
    \end{enumerate}}
    
Une fois toutes ces précisions fournies, la classe `Gradescope` peut être appelée. Le paquets supplémentaires ou les commandes personnalisées définies dans une autre fichier peuvent aussi être incluses.

.. code:: none

    \documentclass{Gradescope}  % On précise la classe utilisée
    \usepackage{libertine}      % Facultatif : utilisation de la police Libertine
    \usepackage[output-decimal-marker={,}]{siunitx} % Facultatif : paquet pour gérer les unités
    %\usepackage{commandesJS}    % Commandes personnalisées dans le fichier commandesJS.sty
    
On débute ensuite le corps du document en posant une première question:

.. code:: none

    \question[4] Un rectangle a des dimensions de \SI{1.2}{\centi\meter} par 
                 \SI{333}{\milli\meter}. Trouvez son aire (exacte) en 
                 \SI{}{\centi\meter\squared}. 
                 Réponse: \boite{2cm}{1cm} \SI{}{\centi\meter\squared}

Voici comment on procède pour poser une question à choix multiple. Gradescope est plus efficace pour reconnaître des zones cochées que des lettres entourées ou encore des lettres dans une boîte.

.. code:: none

   \question[1\half] Noircissez le carré correspondant à l'isométrie que vous appréciez le plus.
    \begin{checkboxes}
        \choice $r_{O,-170^{\circ}}\circ g_{a,\overrightarrow{UV}}$
        \choice $r_{O,170^{\circ}}\circ g_{a,\overrightarrow{VU}}$
        \choice $r_{O,-170^{\circ}}\circ g_{a,\overrightarrow{VU}}$
        \choice $g_{a,-\overrightarrow{UV}}\circ r_{O,-170^{\circ}}$
        \choice $g_{a,\overrightarrow{UV}}\circ r_{O,170^{\circ}}$
        \choice $g_{a,\overrightarrow{VU}}\circ r_{O,170^{\circ}}$
    \end{checkboxes}
    
Voici un exemple de question nécessitant une démarche pour laquelle la reconnaissance d'expressions mathématiques peut être utilisée pour regrouper des réponses:

.. code:: none

   \question[3] Ceci est une question nécessitant une longue démarche. Il faut trouver un polynôme
   $p(x)$ respectant certaines conditions. Écrivez votre réponse dans l'encadré au bas de la page.
   \vfill
   Réponse: $p(x)=$ \boite{4cm}{1cm}
   
On termine ensuite le bloc de questions et on inclus la page pour la poursuite des démarches. On ferme ensuite le corps du document.

.. code:: none

   \end{questions}
   \newpage
   Vous pouvez poursuivre une solution sur cette page ou l'utiliser comme brouillon. Dans tous
   les cas, veuillez ne pas la débrocher. Si vous poursuivez une solution, indiquez dans la 
   zone de réponse de la question concernée que la suite se trouve ici.
   \end{document}

