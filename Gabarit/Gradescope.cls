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
	\newcommand{\carresection[1]}
		{
			\begin{tikzpicture}
			\draw (0,0) -- (0.5,0) -- (0.5,0.5) -- (0,0.5) -- cycle;
			\draw (0.5,0.25) node[align=left, right]{#1};
			\end{tikzpicture}
		}
    \newcommand{\boite}[2]
		{
		\raisebox{-.4cm}{
				\begin{tikzpicture}
					\draw (0,0)--(#1,0) -- (#1,#2) -- (0,#2) -- cycle;		
				\end{tikzpicture}
            }
        }
    \checkboxchar{
    \raisebox{-0.2cm}{\begin{tikzpicture}
     \draw (0,0) -- (0.5,0) -- (0.5,0.5) -- (0,0.5) -- cycle;
    \end{tikzpicture}}}
\providecommand{\SigleNumero}{}
\providecommand{\NomCours}{}
\providecommand{\DateEvaluation}{}
\providecommand{\Session}{}
\providecommand{\NomEvaluation}{}
\providecommand{\Ponderation}{}
\providecommand{\SectionA}{}
\providecommand{\SectionB}{}
\providecommand{\SectionC}{}
\providecommand{\SectionD}{}
\providecommand{\Matricule}{}
\providecommand{\Coordonnateur}{}
\providecommand{\Coordonnatrice}{}
\providecommand{\Enseignant}{}
\providecommand{\Enseignante}{}
\providecommand{\Directives}{}
\providecommand{\PapierLegal}{}

\setlength\linefillheight{1cm}

	\firstpageheader{}{}{}
	\runningheader{\sc\small\ifdefempty{\SigleNumero}{}{\SigleNumero}}
	{\sc\small\ifdefempty{\NomEvaluation}{}{\NomEvaluation}\ifdefempty{\Session}{}{~-~\Session}}
	{\sc{\small \thepage~/~\numpages}}
	\runningfooter{}{}{
		\begin{tikzpicture}
		\draw (0,0) -- (1.5,0) -- (1.5,0.7) -- (0,0.7) -- cycle;
		\draw (0,0.35) node[left]{Vos initiales:~};
		\end{tikzpicture}
		}
		\noboxedpoints
		\qformat{{\textbf{Question~\thequestion}}~{(\,\totalpoints~points)}~\hfill}
		\addpoints
	\newcommand{\couverture}{
			\begin{minipage}[t]{7cm}
				\begin{flushleft}
					\hspace{-.5cm}\includegraphics[width=5cm]{logo.pdf}\\
					\hspace{-.5cm}{\sf\scriptsize \textbf{Faculté des sciences et génie}}\\[-0.2cm]
					\hspace{-.5cm}{\sf\scriptsize Département de mathématiques et statistique}\\[2cm]
				\end{flushleft}
			\end{minipage}~~~
			\begin{minipage}[t]{\textwidth-5.5cm}
				\begin{tikzpicture}
				\draw (0,0) -- (10,0) -- (10,1.5) -- (0,1.5) -- cycle;
				\draw (0,0) node[below right]{\scriptsize\text{Prénom et nom en lettres moulées (ne pas écrire à l'extérieur de l'encadré)}};
				\end{tikzpicture}\\[0.4cm]
				\begin{tikzpicture}
				\draw (0,0) -- (9,0) -- (9,1) -- (0,1) -- cycle;
				\draw (0,0) node[below right]{\scriptsize\text{NI (nombre à 9 chiffres sur votre carte étudiante)}};
				\end{tikzpicture}\\[0.4cm]
				\ifdefempty{\SectionA}{}{\carresection[\SectionA]\\}
				\ifdefempty{\SectionB}{}{\carresection[\SectionB]\\}
				\ifdefempty{\SectionC}{}{\carresection[\SectionC]\\}
				\ifdefempty{\SectionD}{}{\carresection[\SectionD]\\}
			\end{minipage}
			\vfill
			\begin{center}
				\huge\textbf{\ifdefempty{\NomEvaluation}{}{\NomEvaluation}\ifdefempty{\Ponderation}{\\}{~(\Ponderation~\%)\\}}
				\Large\ifdefempty{\NomCours}{}{\NomCours}\ifdefempty{\SigleNumero}{}{~(\SigleNumero)\\}
				\Large\ifdefempty{\DateEvaluation}{}{\DateEvaluation\\}
				\ifdefempty{\Enseignant}{}{Enseignant : \Enseignant\\}\ifdefempty{\Enseignante}{}{Enseignante : \Enseignante\\}
				\ifdefempty{\Coordonnateur}{}{Coordonnateur : \Coordonnateur\\}
				\ifdefempty{\Coordonnatrice}{}{Coordonnatrice : \Coordonnatrice\\}
			\end{center}
			\vfill
			\ifdefempty{\Directives}{}{{\noindent\textbf{Directives de l'évaluation}\Directives}}
			\vfill
			\newpage
			}
\AtBeginDocument{\couverture}
