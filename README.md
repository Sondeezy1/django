#  Django Notes App

Une application web simple de prise de notes utilisant Django.  
Chaque utilisateur peut s’inscrire, se connecter, créer ses propres notes, les consulter, et les filtrer par catégories.

---

## Fonctionnalités

-  Création de notes personnelles
-  Authentification : inscription, connexion, déconnexion
-  Chaque utilisateur ne voit que ses propres notes
-  Catégorisation des notes : Personnel, Travail, Étude, Autre
-  Interface stylisée avec CSS personnalisé
-  Interface d’administration Django

---

##  Structure du projet

```bash
WEB/
├── notes/                  # App principale
│   ├── models.py           # Modèle Note
│   ├── views.py            # Vues (note_list, note_create...)
│   ├── urls.py             # URLs locales
│   └── templates/notes/    # Templates HTML
├── WEB/                    # Répertoire du projet
│   └── settings.py         # Configuration Django
├── db.sqlite3              # Base de données SQLite
└── manage.py
