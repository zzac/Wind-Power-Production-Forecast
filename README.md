# Wind Power Production Forecast

Ce projet est dédié à l'analyse et à la modélisation de la production d'énergie éolienne. Il utilise des données historiques de production et de capacité installée pour divers parcs éoliens afin de générer des prévisions précises.

## Présentation des Données

Le projet exploite un jeu de données principal nommé `dataset.parquet`. Ce fichier contient les mesures de production pour plusieurs sites, notamment :

* **Parcs éoliens couverts :** Belwind Phase 1, Northwind, Thorntonbank (C-Power), Rentel, et d'autres sites offshore et terrestres.
* **Variables principales :**
    * `site_name` : Nom du parc éolien.
    * `delivery_timel` : Horodatage des relevés.
    * `production` : Puissance électrique réelle générée (MW).
    * `installed_capacity` : Capacité nominale maximale du site à l'instant T.

## Objectifs

1.  **Analyse de Performance :** Comparer la production réelle par rapport à la capacité installée pour évaluer l'efficacité des sites.
2.  **Prédiction :** Entraîner des modèles de séries temporelles ou de régression pour anticiper la production en fonction des historiques.
3.  **Visualisation :** Identifier les tendances saisonnières et l'impact des variations géographiques entre les parcs.
