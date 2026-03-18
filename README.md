# Wind Power Production Forecast - Belgium Offshore

## Contexte Métier
Dans le cadre de la transition énergétique, les opérateurs éoliens offshore belges sont soumis à des obligations de prévision de production sur les marchés de l'énergie à court terme. 

Pour optimiser leurs positions sur le marché Day-Ahead, ils doivent soumettre des offres de production 24 heures à l'avance au gestionnaire de réseau Elia. Une prévision erronée génère des coûts d'équilibrage importants et dégrade la rentabilité des actifs.

Ce projet, réalisé pour un opérateur énergétique belge par Wavestone, vise à développer des modèles de prévision avancés en exploitant les données météorologiques et les historiques de production.

## Périmètre du Projet (Zone MOG)
La Belgique exploite l'une des zones de concession éolienne offshore les plus denses d'Europe. Le projet se concentre sur les parcs connectés via le Modular Offshore Grid (MOG), situés entre 20 et 50 km des côtes :

* **Capacité totale :** Environ 2,3 GW.
* **Sites concernés :** Nobelwind, Rentel, Norther, Northwester 2, Mermaid, Seastar, Belwind, Northwind et Thorntonbank.
* **Conditions :** Tous les parcs sont situés dans un rayon de 30 km, ce qui implique des conditions météorologiques très similaires pour l'ensemble du portefeuille.

## Données
Les analyses et modèles s'appuient sur le fichier `dataset.parquet` qui contient :
* `site_name` : Nom de l'installation éolienne.
* `delivery_timel` : Horodatage des données.
* `production` : Puissance réelle produite (MW).
* `installed_capacity` : Capacité installée au moment de la mesure.

## Objectifs du Projet
1.  **Analyse Exploratoire :** Étude des corrélations de production entre les différents parcs de la zone MOG.
2.  **Modélisation :** Développement d'algorithmes de machine learning pour la prévision à J+1.
3.  **Optimisation Financière :** Réduction de l'écart entre les prévisions et la production réelle pour limiter les coûts d'imbalance.
