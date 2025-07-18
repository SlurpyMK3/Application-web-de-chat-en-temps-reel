
# 💬 Hello_chat – Application web de chat en temps réel

[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://www.docker.com/)


**Hello_Chat** est une application de chat en ligne construite avec **Django**, **Channels**, **Redis** et **WebSockets**.  
Elle permet à plusieurs utilisateurs de communiquer en temps réel dans des salons de discussion.

---

## 🚀 Fonctionnalités

- Authentification utilisateur (inscription, connexion, déconnexion)
- Chat en temps réel avec WebSockets via Django Channels
- Création et gestion de salons de discussion dynamiques
- Interface moderne avec TailwindCSS et Flowbite
- Gestion des messages et des utilisateurs connectés
- Déploiement facile via Docker et Docker Compose

---

## 🐳 Installation avec Docker

### 1. Cloner le dépôt

```bash
git clone https://github.com/SlurpyMK3/Application-web-de-chat-en-temps-reel.git
cd Application-web-de-chat-en-temps-reel
```

### 2. Construire et lancer les conteneurs

```bash
docker-compose up --build
```

### 3. Accéder à l’application

Ouvre ton navigateur et va sur :  
[http://localhost:8000/](http://localhost:8000/)

---

## ⚙️ Configuration

Variables d’environnement dans `docker-compose.yml` :

```yaml
DATABASE_URL=postgres://postgres:667442@db:5432/postgres
REDIS_URL=redis://redis:6379/0
```

Ces variables configurent la connexion à la base de données PostgreSQL et à Redis.

---

## 📁 Structure du projet

- `mysite/` : Projet Django principal (`settings.py`, `urls.py`, `asgi.py`, etc.)
- `chat/` : Application Django pour la gestion du chat (`models.py`, `views.py`, `consumers.py`, etc.)
- `templates/` : Templates HTML (Django Template Engine)
- `static/` : Fichiers statiques (CSS, JS, images)
- `entrypoint.sh` : Script de démarrage pour appliquer les migrations et collectstatic
- `Dockerfile` : Construction de l’image Docker de l’application
- `docker-compose.yml` : Orchestration des services Docker (`web`, `db`, `redis`)

---

## 🛠️ Commandes utiles

Créer un superutilisateur Django :

```bash
docker-compose exec web python manage.py createsuperuser
```

Appliquer les migrations manuellement :

```bash
docker-compose exec web python manage.py migrate
```

Accéder au shell Django :

```bash
docker-compose exec web python manage.py shell
```

---

## 📦 Technologies utilisées

- Python 3.11  
- Django 5.x  
- Django Channels (ASGI et WebSockets)  
- Redis (gestion des channels)  
- PostgreSQL (base de données)  
- TailwindCSS + Flowbite (UI moderne)  
- Docker & Docker Compose

---
