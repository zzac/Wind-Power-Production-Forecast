# Prédiction de la production d'énergie éolienne en mer

## Contexte du projet
Dans le cadre de la transition énergétique, les opérateurs de parcs éoliens offshore belges sont soumis à des obligations de prévision de production sur les marchés de l'énergie à court terme. Pour optimiser leurs positions sur le marché "Day-Ahead", ils doivent soumettre des offres de production 24 heures à l'avance au gestionnaire de réseau Elia. Une mauvaise prévision génère des coûts d'équilibrage importants et dégrade la rentabilité des actifs.

Ce projet vise à développer des modèles avancés de prévision de la production d'énergie éolienne en mer, en exploitant les données de prévisions météorologiques et les relevés historiques de production d'un portefeuille de parcs éoliens.

## Périmètre d'étude
L'étude porte sur 10 parcs éoliens actifs en mer du Nord, situés à 20-50 km des côtes belges (Nobelwind, Rentel, Norther, Northwester 2, Mermaid, Seastar, Belwind, Northwind et Thorntonbank). Ces parcs représentent une capacité installée totale d'environ 2,3 GW.

## Description des données
Le projet s'appuie sur trois jeux de données principaux :

### 1. Production (Dataset 1)
* **Données** : Production éolienne offshore horaire.
* **Période** : Du 31/12/2022 au 18/02/2026.
* **Colonnes** : Nom du site, horodatage (UTC), production mesurée (MW), et capacité installée (MW).

### 2. Localisation (Dataset 2)
* **Données** : Coordonnées géographiques des 10 sites.
* **Colonnes** : Nom du site, latitude (°N), longitude (°E).

### 3. Météo (Dataset 3)
* **Source** : API Open-Meteo (Modèle ECMWF IFS HRES).
* **Données** : Prévisions horaires incluant la vitesse du vent (10m et 100m), la direction du vent, les rafales, la température, la pression atmosphérique, et la couverture nuageuse.

## Structure du projet
* `dataset_1.parquet` : Historique de production.
* `dataset_2.parquet` : Coordonnées des parcs.
* `dataset_3.parquet` : Données météorologiques historiques et prévisions.
* `consignes.pdf` : Cahier des charges et contexte métier.

## Installation et Utilisation
1. Assurez-vous de disposer d'un environnement Python avec les bibliothèques `pandas` et `pyarrow` pour la lecture des fichiers Parquet.
2. Chargez les données via la commande :
   ```python
   import pandas as pd
   df_prod = pd.read_parquet('dataset_1.parquet')
