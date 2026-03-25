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

### 3 Données Météorologiques (IFS HRES 9km) (Dataset 3)

Ce jeu de données regroupe les prévisions issues du modèle de prévision numérique du temps (NWP) haute résolution du Centre européen pour les prévisions météorologiques à moyen terme (ECMWF). Il s'agit de données maillées sur une résolution spatiale de 9 km x 9 km, fournies à un pas de temps horaire. Dans le cadre opérationnel du marché Day-Ahead (horizon H+24), ces variables constituent les caractéristiques explicatives (*features*) fondamentales du modèle de prévision.

**1. Dynamique des Vents (Facteurs de Puissance Primaire)**
La puissance éolienne générée étant proportionnelle au cube de la vitesse du vent, ces variables sont les prédicteurs les plus critiques du modèle.
* **`wind_speed_100m` (m/s)** : Vitesse moyenne du vent extrapolée à 100 mètres d'altitude, correspondant à la hauteur de moyeu (*hub height*) standard des turbines offshore étudiées.
* **`wind_speed_10m` (m/s)** : Vitesse moyenne du vent à 10 mètres d'altitude. Couplée à la mesure à 100m, elle permet au modèle de capter le cisaillement du vent (*wind shear*) et la rugosité de surface liée à la houle océanique.
* **`wind_gusts_10m` (m/s)** : Vitesse maximale des rafales enregistrées sur les 3 heures précédentes. Cette variable agit comme un indicateur de volatilité et permet d'anticiper les baisses brutales de production liées aux mises en sécurité (arrêts automatiques) des éoliennes lors d'épisodes de vents extrêmes.

**2. Thermodynamique et Densité de l'Air**
La masse volumique de l'air influence directement l'énergie cinétique récupérable par les pales. À vitesse de vent égale, un air froid et dense génère un meilleur rendement énergétique.
* **`temperature_2m` (°C)** : Température atmosphérique à 2 mètres d'altitude.
* **`apparent_temperature` (°C)** : Température ressentie intégrant l'humidité ambiante, permettant d'affiner l'estimation de la densité de l'air.
* **`dewpoint_2m` (°C)** : Température du point de rosée. Le différentiel entre la température ambiante et le point de rosée est un indicateur clé du risque de givrage sur les pales (*blade icing*). Le givre altère sévèrement l'aérodynamisme des rotors et provoque des pertes de production drastiques.

**3. Conditions Barométriques**
* **`pressure_msl` (hPa)** : Pression atmosphérique ramenée au niveau moyen de la mer.
* **`surface_pressure` (hPa)** : Pression atmosphérique en surface. L'analyse des variations de pression permet au modèle d'identifier les systèmes frontaux et l'instabilité atmosphérique globale, qui dictent les variations macroscopiques des régimes de vent.

**4. Précipitations et Couverture Nuageuse**
* **`precipitation` (mm)** & **`snowfall` (cm)** : Cumuls horaires des précipitations. Bien que leur impact direct soit de second ordre, des précipitations intenses modifient la densité locale de l'air et impactent l'écoulement aérodynamique autour des pales.
* **`cloud_cover` (%)** : Couverture nuageuse totale. Elle sert d'indicateur de stabilité de la couche limite atmosphérique ; une forte nébulosité atténue les gradients thermiques au-dessus de l'océan, stabilisant ainsi les masses d'air.

**Alignement Temporel et Contrainte Métier :**
Pour éviter toute fuite de données (*data leakage*) et respecter le cahier des charges d'Elia, le modèle doit impérativement s'entraîner sur des prévisions météorologiques alignées avec le moment de la soumission des enchères. L'utilisation des "runs" météorologiques projetés à H+24 garantit que le modèle sera évaluable dans des conditions opérationnelles réelles.

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
