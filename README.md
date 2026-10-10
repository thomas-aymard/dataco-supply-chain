# 📦 Supply Chain Analytics & Late Delivery Prediction

## 📝 Contexte du Projet
Ce projet de Data Science de bout en bout simule l'environnement de données d'une entreprise de logistique et de e-commerce. L'objectif est de transformer des données brutes (fichiers plats) en une base de données relationnelle exploitable, puis de développer un modèle d'apprentissage automatique capable d'anticiper les retards de livraison.

## 🛠️ Architecture Technique & Outils
* **ETL (Extract, Transform, Load) :** Script Python automatisé (`pandas`) pour nettoyer et normaliser un dataset de +180 000 lignes.
* **Base de données :** Modélisation relationnelle et création d'une base de données `SQLite` (requêtes SQL, jointures).
* **Machine Learning :** Utilisation de `Scikit-Learn` (Random Forest Classifier) dans un environnement `Jupyter Notebook`.

## 🚀 Réalisations et Résultats
1. **Pipeline de Données :** Découpage du dataset brut en tables relationnelles (`Customers`, `Orders`, etc.) pour optimiser l'intégrité et le requêtage.
2. **Feature Engineering :** Préparation des données catégorielles et création de la vue analytique métier.
3. **Modélisation Prédictive :** Entraînement d'un modèle Random Forest pour identifier les risques de retards de livraison (`Late_Delivery_Risk`).

**Performance du Modèle :**
* Le modèle atteint une **précision globale (Accuracy) de ~69%**.
* Le KPI critique (Precision sur la détection des retards) s'élève à **84%**. Cela signifie que lorsque le modèle prédit qu'une commande sera en retard, la prédiction est correcte dans 84% des cas, offrant une fiabilité d'action forte pour les équipes logistiques.

## 📂 Structure du Répertoire
* `/data/` : Dossiers de stockage des données brutes (ignoré via .gitignore) et de la base de données SQL générée.
* `/sql/` : Scripts de création (DDL) du schéma relationnel.
* `/scripts/` : Scripts Python d'automatisation du pipeline ETL.
* `/notebooks/` : Notebooks Jupyter d'analyse exploratoire et d'entraînement du modèle Machine Learning.