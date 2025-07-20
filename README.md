# 📌 SoftDesk – API REST de gestion de projets et de bugs

SoftDesk est une API web développée avec Django REST Framework, permettant de gérer des projets collaboratifs, des tickets (issues), et des commentaires liés.

---

## 🚀 Fonctionnalités

- Authentification sécurisée via JWT (SimpleJWT)
- Gestion des utilisateurs avec vérification de l'âge (RGPD)
- Création de projets, ajout de contributeurs
- Gestion des issues (tâches, bugs, features)
- Commentaires sur chaque issue
- Permissions fines sur les accès : seuls les autheur / contributeurs d'un projet peuvent y accéder, modifier ou commenter les ressources liées
- Pagination automatique sur les ressources listables
- Mise à jour automatique des dépendances via `dependabot.yml`

---

## 📦 Stack technique

- Python 3.12
- Django 5.x
- Django REST Framework
- djangorestframework-simplejwt (auth)
- SQLite (en dev)
- Postman (tests manuels)

---

## 🛡 Sécurité et RGPD

L’application respecte les principes du RGPD :
- Consentement explicite demandé pour être contacté ou partager ses données
- Vérification que l'utilisateur a au moins 15 ans
- Données personnelles modifiables ou supprimables (droit à l’oubli)

---

## 🔧 Installation

```bash
# 1. Clone du repo
git clone https://github.com/votre-utilisateur/softdesk-api.git
cd softdesk-api

# 2. Installer les dépendances avec Pipenv
pipenv install --dev

# 3. Activer l'environnement virtuel
pipenv shell

# 4. Migrer la base de données
python manage.py migrate

# 5. Créer un superutilisateur
python manage.py createsuperuser
