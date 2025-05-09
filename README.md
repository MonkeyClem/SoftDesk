## Récupération du projet : 

Pour lancer ce projet, veuillez vous rendre dans le dossier qui servira la racine, et lancer la commande suivante : 
```bash
git clone https://github.com/MonkeyClem/openDesk.git
cd openDesk
```

## Installer l’environnement :

```bash
pip install pipenv        # si pipenv n’est pas encore installé
pipenv install            # installe tout depuis le Pipfile
pipenv shell              # active l’environnement virtuel
```

Appliquer les migrations :

```bash
python manage.py migrate
```

## (Optionnel) Créer un superuser :
```bash
python manage.py createsuperuser
```

## Lancer le serveur :
```bash
python manage.py runserver
```