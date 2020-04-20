Ce projet a pour but de créer un site web pour mettre en place le forum RBS de Biosciences qui a lieu chaque année. 

Presentation.html
    Présente l'évènement des RBS, aux entreprises comme aux étudiants, et la possibilité de récupérer des fichiers pdf qui comportent des informations supplémentaires sur l'évènement ou le département Biosciences.

Entreprise.html
    Cette page permet aux entreprises de s'inscrire à l'évènement en répondant à quelques questions pour aider à l'organisation de l'évènement.
    Vérification que les fichiers ajoutés par l'utilisateur sont corrects (bonne extension). 
    Les fichiers déposés par les entreprises sont déposés dans le dossier 'Entreprises_inscription' et 'Entreprises_logo'.
    Une fois le formulaire rempli, on redirige vers la page de remerciements.
    Si les fichiers sont incorrects, on redirige vers la page Entreprises.
    Vérifie que l'adresse mail n'a jamais été utilisée. Si c'est le cas, redirige vers la page "Redirection.html"

Etudiants.html
    Cette page permet aux étudiants de s'inscrire à l'évènement en répondant à quelques questions pour aider à l'organisation de l'évènement.
    Vérification que le fichier ajouté par l'utilisateur (cv) est correct (bonne extension). 
    Les fichiers déposés par les étudiants sont déposés dans le dossier 'Etudiants_CV'.
    Une fois le formulaire rempli, on redirige vers la page de remerciements (Remerciement.html).
    Si le fichier "cv" est incorrect, on redirige vers la page Etudiants.
    Vérifie que l'adresse mail n'a jamais été utilisée. Si c'est le cas, redirige vers la page "Redirection.html"

Contact.html
    Redirige l'utilisateur vers sa boîte mail et pré-rempli le destinataire vers l'adresse mail générique de RBS lorsqu'il clique sur "ICI".

donnees.json
    Contient les informations des étudiants et des entreprises qui se sont inscrits au forum. Avec présence d'un id au cas où. 

login.html
    Permet aux administrateurs de se connecter afin d'avoir accès à la page qui recense toutes les inscriptions, étudiants comme entreprises (admin.html)
    Si le login est incorrect un message d'erreur demande de réessayer.
    Si le login est correct vous êtes redirigé vers la page d'acceuil pour administrateur (profil.html) et la barre de navigation en haut change.
    Vous pouvez accèder à l'intégralité des informations de chaque inscrits en cliquant sur les noms de ces derniers (membre.html).
    Enfin vous pouvez vous déconnecter. Il est recommender de le faire avant de fermer la page internet.

    Les logins et mot de passe sont (sensible à la casse):
    baptiste.alberti@insa-lyon.fr BaptisteAlberti
    maxime.carlier@insa-lyon.fr MaximeCarlier
    guilhem.panneau@insa-lyon.fr GuilhemPanneau
    dimitri.mikec@insa-lyon.fr DimitriMikec

L'ensemble des routes est présent dans le fichier app.py
Le chargement de la base de données db.sqlite pour la gestion des login se fait par la fonction présente dans __init__.py
Les informations pour les entreprises et les étudiants sont stockées dans donnees.json
Ces informations sont chargés par le fichier data.py

Enfin pour avoir accès aux packages pour la gestion des login connectez vous à l'environnement virtuel du projet avec la commande "source PROJET/venv/bin/activate" avant de faire ./do serve.

""" Le code a été testé sur mozilla firefox."""
""" Il est conseillé de recharger le serveur en faisant './do serve' chaque fois qu'une inscription est réalisée (i.e que 'donnees.json' est modifié). Cela n'est pas un souci car en pratique chaque personne ne fait qu'une inscription à la fois."""
