Présentation
Ce projet est une API RESTful permettant de gérer des utilisateurs (nom et email) à travers des opérations CRUD (Create, Read, Update, Delete). L’objectif principal est de construire une architecture professionnelle, conteneurisée avec Docker, connectée à une base de données PostgreSQL, et testable via Postman.

Ce projet s’inscrit dans une logique d’apprentissage concret des outils et bonnes pratiques utilisés en entreprise dans un environnement Python back-end.

Cahier des charges simplifié
Objectif : développer une API REST maintenable, testable, et facilement déployable, dans un environnement isolé.

Rôle du développeur : mettre en place le back-end, la base de données, l’environnement Docker, les tests avec Postman et une documentation claire


Stack technique
Python 3

Django 5

Django REST Framework

PostgreSQL (via Docker)

Docker / Docker Compose

Postman

TablePlus

Fonctionnalités de l’API
Création d’un utilisateur

Récupération de la liste des utilisateurs

Récupération des détails d’un utilisateur

Modification d’un utilisateur

Suppression d’un utilisateur

Docker et Docker Compose

Instructions
bash

git clone https://github.com/ton_pseudo/api_py.git
cd api_py
docker compose build
docker compose up

Tests avec Postman
Les endpoints disponibles permettent :

GET /api/users/ : Liste des utilisateurs

POST /api/users/ : Création d’un utilisateur

GET /api/users/<id>/ : Détail d’un utilisateur

PUT /api/users/<id>/ : Mise à jour

DELETE /api/users/<id>/ : Suppression



