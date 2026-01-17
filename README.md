# 🚀 SQL Reliability & QA Toolkit (22M+ Transactions)

Ce projet simule un environnement bancaire (type Fintech) à haute charge pour tester la fiabilité des systèmes, l'intégrité des données et les performances SQL.

## 📊 Le Challenge technique
L'objectif était de passer d'un simple script de base à un environnement de production réaliste pour pratiquer le monitoring SRE et l'automatisation QA.

- **Volume de données :** 22 294 503 transactions.
- **Poids de la base :** 2.8 GB.
- **Moteur :** InnoDB (MySQL).



---

## 🛠️ Contenu du Toolkit

### 1. Data Generation (`/data_gen`)
Script Python utilisant `Faker` et des **insertions par lots (batching)** de 5000 lignes pour optimiser les I/O disque et éviter la saturation du buffer pool.
> *Usage : Automatisation de jeux de données massifs pour tests de charge.*

### 2. Emergency SQL Toolkit (`/sql_scripts`)
Une collection de requêtes critiques pour le diagnostic en production :
- **Performance :** Identification des verrous (Locks) et des requêtes lentes.
- **Intégrité :** Audit automatique pour détecter les écarts entre les soldes et l'historique des transactions (Data Drift).

### 3. Monitoring & Health Check (`/monitoring`)
Scripts automatisés pour vérifier la disponibilité de la base de données et alerter en cas d'indisponibilité.

---

## 📈 Résultats & Apprentissages (SRE Mindset)

### Incident Simulation #1 : Le "Slow Count"
- **Problème :** Un simple `SELECT COUNT(*)` prenait **9.09 secondes**.
- **Diagnostic :** Full Table Scan sur un volume de 2.8 Go sans indexation optimisée.
- **Solution :** Mise en place d'index composites et optimisation de la configuration `innodb_buffer_pool_size`.
- **Résultat :** Temps de réponse réduit à **< 0.01s**.

### Incident Simulation #2 : Data Integrity
- **Scénario :** Simulation d'un crash durant un transfert.
- **Outil :** Le script `audit_integrity.sql` a permis de détecter immédiatement les comptes dont le solde ne correspondait plus à la somme des transactions.

---

## ⚙️ Installation Rapide

1. **DB Setup :** `mysql -u root -p < sql_scripts/setup_db.sql`
2. **Install Deps :** `pip install -r requirements.txt`
3. **Generate Data :** `python data_gen/generator.py`

---

## 👨‍💻 Pourquoi ce projet ?
Initialement orienté Data, j'ai développé ce toolkit pour démontrer que la maîtrise fine du SQL et de la gestion des données est le pilier central de la **fiabilité (SRE)** et de l'**automatisation des tests (QA)**