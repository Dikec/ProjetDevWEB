Ce projet a pour but de créer un site web pour mettre en place le forum RBS de Biosciences qui a lieu chaque année. 

Presentation.html
    Présente les RBS

Entreprise.html
    Vérification que les fichiers ajoutés par l'utilisateur sont corrects (bonne extension). 
    Les fichiers déposés par les entreprises sont déposés dans le dossier 'Entreprises_inscription' et 'Entreprises_logo'.
    Une fois le formulaire rempli, on redirige vers la page de remerciements.
    Si les fichiers sont incorrects, on redirige vers la page Entreprises.
    Vérifie que l'adresse mail n'a jamais été utilisée. Si c'est le cas, redirige vers la page "Redirection.html"

Etudiants.html
    Vérification que le fichier ajouté par l'utilisateur (cv) est correct (bonne extension). 
    Les fichiers déposés par les étudiants sont déposés dans le dossier 'Etudiants_CV'.
    Une fois le formulaire rempli, on redirige vers la page de remerciements (Remerciement.html).
    Si le fichier "cv" est incorrect, on redirige vers la page Etudiants.
    Vérifie que l'adresse mail n'a jamais été utilisée. Si c'est le cas, redirige vers la page "Redirection.html"

Contact.html
    Redirige l'utilisateur vers sa boîte mail et pré-rempli le destinataire vers l'adresse mail générique de RBS lorsqu'il clique sur "ICI".

donnees.json
    Contient les informations des étudiants et des entreprises qui se sont inscrits au forum. Avec présence d'un id au cas où. 

""" Le code a été testé sur mozilla firefox."""
""" Il est conseillé de recharger le serveur en faisant './do serve' chaque fois qu'une inscription est réalisée (i.e que 'donnees.json' est modifié). Cela n'est pas un souci car en pratique chaque personne ne fait qu'une inscription à la fois."""
