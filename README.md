# 🤖 AI Platform Django - Machine Learning Web Application

Une plateforme web interactive pour explorer et tester différents algorithmes de Machine Learning avec Django.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0+-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table des Matières

- [🎯 Aperçu](#-aperçu)
- [✨ Fonctionnalités](#-fonctionnalités)
- [🛠️ Technologies Utilisées](#️-technologies-utilisées)
- [📦 Installation](#-installation)
- [🚀 Utilisation](#-utilisation)
- [🧠 Algorithmes Implémentés](#-algorithmes-implémentés)
- [📁 Structure du Projet](#-structure-du-projet)
- [🤝 Contribution](#-contribution)
- [📄 Licence](#-licence)

## 🎯 Aperçu

AI Platform Django est une application web éducative qui permet aux utilisateurs d'explorer et de tester différents algorithmes de Machine Learning de manière interactive. L'application propose des exemples concrets de classification et de régression avec des interfaces utilisateur intuitives.

### 🌟 Pourquoi cette plateforme ?

- **Apprentissage interactif** : Testez les algorithmes avec des paramètres personnalisables
- **Comparaison visuelle** : Comparez les performances entre différents algorithmes
- **Interface intuitive** : Pas besoin de connaissances en programmation
- **Exemples réels** : Datasets classiques (Iris, California Housing)

## ✨ Fonctionnalités

### 🔬 Algorithmes de Machine Learning
- **Random Forest** : Classification et Régression
- **Decision Tree** : Classification et Régression avec règles interprétables
- **AdaBoost** : Classification et Régression avec boosting adaptatif

### 📊 Exemples Interactifs
- **Classification Iris** : Prédiction d'espèces de fleurs
- **Régression California Housing** : Prédiction de prix immobiliers

### 🎛️ Interface Utilisateur
- **Formulaires interactifs** avec sliders pour ajuster les paramètres
- **Visualisation des résultats** avec images et analyses contextuelles
- **Explications des algorithmes** avec avantages/inconvénients
- **Logique de décision transparente** (surtout pour Decision Tree)

### 🔄 Architecture Unifiée
- **Templates réutilisables** pour tous les algorithmes
- **Code modulaire** et facilement extensible
- **Interface cohérente** entre tous les modèles

## 🛠️ Technologies Utilisées

### Backend
- **Django 5.2+** : Framework web Python
- **Python 3.8+** : Langage de programmation

### Machine Learning
- **scikit-learn** : Bibliothèque de Machine Learning
- **NumPy** : Calculs numériques
- **Pandas** : Manipulation de données
- **Joblib** : Sérialisation des modèles

### Frontend
- **HTML5 & CSS3** : Structure et style
- **Bootstrap 5** : Framework CSS responsive
- **JavaScript** : Interactivité côté client

## 📦 Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de packages Python)

### 1. Cloner le Dépôt
```bash
git clone https://github.com/mouadaarab/machine-learning.git
cd ai-platform-django/aiPlateform
```

### 2. Créer un Environnement Virtuel
```bash
python -m venv venv

# Sur Windows
venv\\Scripts\\activate

# Sur macOS/Linux
source venv/bin/activate
```

### 3. Installer les Dépendances
```bash
pip install -r requirements.txt
```

### 4. Créer les Modèles ML (Optionnel)
Les modèles pré-entraînés sont inclus, mais vous pouvez les recréer :
```bash
# Modèles Random Forest
python scripts/create_iris_model.py
python scripts/create_california_housing_model.py

# Modèles Decision Tree
python scripts/create_decision_tree_models.py

# Modèles AdaBoost
python scripts/create_adaboost_models.py
```

### 5. Configurer Django
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

### 6. Lancer le Serveur
```bash
python manage.py runserver
```

L'application sera accessible à : `http://127.0.0.1:8000`

## 🚀 Utilisation

### 🏠 Page d'Accueil
- Naviguez entre les différents algorithmes
- Accédez aux détails de chaque algorithme
- Choisissez entre classification et régression

### 🌸 Classification Iris
1. Cliquez sur "Exemple de Classification" pour Random Forest ou Decision Tree
2. Ajustez les dimensions des sépales et pétales avec les sliders
3. Cliquez sur "Prédire" pour voir l'espèce prédite
4. Observez la logique de décision (surtout pour Decision Tree)

### 🏠 Régression California Housing
1. Cliquez sur "Exemple de Régression"
2. Ajustez les paramètres du logement (revenu, âge, localisation, etc.)
3. Obtenez une prédiction de prix avec analyse contextuelle
4. Comparez les résultats entre algorithmes

### 📚 Pages de Détails
- Apprenez le fonctionnement de chaque algorithme
- Découvrez les avantages et inconvénients
- Comprenez les paramètres importants

## 🧠 Algorithmes Implémentés

### 🌳 Random Forest
**Avantages :**
- Très précis et robuste
- Réduit le surapprentissage
- Gère bien les données manquantes

**Inconvénients :**
- Moins interprétable
- Plus complexe computationnellement

**Performances :**
- Iris : ~97% de précision
- California Housing : R² = 0.77

### 🌲 Decision Tree
**Avantages :**
- Complètement interprétable
- Règles de décision claires
- Rapide à entraîner et prédire

**Inconvénients :**
- Tendance au surapprentissage
- Moins stable (sensible aux données)

**Performances :**
- Iris : 100% de précision sur le test
- California Housing : R² = 0.69

### 🚀 AdaBoost (Adaptive Boosting)
**Avantages :**
- Améliore les "weak learners" 
- Réduit le biais efficacement
- S'adapte aux échantillons difficiles

**Inconvénients :**
- Sensible au bruit et aux outliers
- Plus lent (entraînement séquentiel)
- Risque de surapprentissage sur des données bruitées

**Performances :**
- Iris : 93.3% de précision
- California Housing : R² = 0.386

## 📁 Structure du Projet

```
aiPlateform/
├── 📄 manage.py                 # Script principal Django
├── 📄 requirements.txt          # Dépendances Python
├── 📄 .gitignore               # Fichiers ignorés par Git
├── 📄 README.md                # Ce fichier
├── 📁 aiPlateform/             # Configuration Django
│   ├── 📄 settings.py
│   ├── 📄 urls.py
│   └── 📄 wsgi.py
├── 📁 algosAi/                 # Application principale
│   ├── 📄 models.py
│   ├── 📄 views.py             # Logique métier
│   ├── 📄 urls.py              # Routes
│   ├── 📁 templates/           # Templates HTML
│   │   └── 📁 includes/
│   │       ├── 📄 index.html
│   │       ├── 📄 unified_iris_form.html
│   │       ├── 📄 unified_iris_results.html
│   │       ├── 📄 unified_housing_form.html
│   │       ├── 📄 unified_housing_results.html
│   │       ├── 📄 rf_details.html
│   │       ├── 📄 dt_details.html
│   │       ├── 📄 rf_iris.html
│   │       ├── 📄 dt_iris.html
│   │       ├── 📄 rf_regression.html
│   │       └── 📄 dt_regression.html
│   └── 📁 static/              # Fichiers statiques
│       ├── 📁 images/          # Images des fleurs et algorithmes
│       └── 📁 pdfs/            # Documentation PDF
├── 📁 models_ai/               # Modèles ML sauvegardés
│   ├── 📄 random_forest_model.pkl
│   ├── 📄 random_forest_model_info.pkl
│   ├── 📄 california_housing_rf_model.pkl
│   ├── 📄 california_housing_rf_model_info.pkl
│   ├── 📄 decision_tree_iris_model.pkl
│   ├── 📄 decision_tree_iris_model_info.pkl
│   ├── 📄 decision_tree_housing_model.pkl
│   ├── 📄 decision_tree_housing_model_info.pkl
│   ├── 📄 adaboost_iris_model.pkl
│   ├── 📄 adaboost_iris_model_info.pkl
│   ├── 📄 adaboost_housing_model.pkl
│   └── � adaboost_housing_model_info.pkl
└── �📁 scripts/                 # Scripts de création des modèles
    ├── 📄 create_iris_model.py
    ├── 📄 create_california_housing_model.py
    ├── 📄 create_decision_tree_models.py
    ├── 📄 create_adaboost_models.py
    └── 📄 MODEL_README.md
```

## 🎨 Captures d'Écran

### Page d'Accueil
Interface principale avec sélection des algorithmes

### Formulaires Interactifs
Sliders pour ajuster les paramètres en temps réel

### Résultats de Prédiction
Affichage des résultats avec analyse contextuelle

### Logique de Décision
Explication step-by-step pour Decision Tree

## 🔧 Développement

### Ajouter un Nouvel Algorithme
1. Créer le script de modèle dans `scripts/`
2. Ajouter les routes dans `algosAi/urls.py`
3. Créer les vues dans `algosAi/views.py`
4. Ajouter la carte d'algorithme dans `templates/includes/index.html`
5. Les templates unifiés s'adapteront automatiquement !

### Architecture Extensible
- **Templates unifiés** : Réutilisables pour tous les algorithmes
- **Système de contexte** : Informations spécifiques par algorithme
- **Modularité** : Facile d'ajouter de nouvelles fonctionnalités

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment contribuer :

1. **Fork** le projet
2. Créez une **branche feature** (`git checkout -b feature/AmazingFeature`)
3. **Committez** vos changements (`git commit -m 'Add some AmazingFeature'`)
4. **Push** vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une **Pull Request**

### Types de Contributions
- 🐛 Correction de bugs
- ✨ Nouvelles fonctionnalités
- 📚 Amélioration de la documentation
- 🎨 Améliorations UI/UX
- 🧠 Nouveaux algorithmes ML

## 📈 Roadmap

### Version Future
- [ ] **Support de plus d'algorithmes** (SVM, Neural Networks, etc.)
- [ ] **Visualisations graphiques** des données et résultats
- [ ] **Upload de datasets personnalisés**
- [ ] **API REST** pour accès programmatique
- [ ] **Authentification utilisateur**
- [ ] **Historique des prédictions**
- [ ] **Comparaison side-by-side** des algorithmes
- [ ] **Export des résultats** (PDF, CSV)

## 🐛 Problèmes Connus

- Les migrations Django peuvent nécessiter d'être appliquées
- Les modèles ML sont pré-entraînés pour la démonstration
- Interface optimisée pour desktop (responsive en cours)

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👥 Auteurs

- **Votre Nom** - *Développement initial* - [@mouadaarab](https://github.com/mouadaarab)

## 🙏 Remerciements

- **scikit-learn** pour les algorithmes de Machine Learning
- **Django** pour le framework web robuste
- **Bootstrap** pour l'interface utilisateur responsive
- **UCI ML Repository** pour les datasets

---

⭐ N'oubliez pas de donner une étoile si ce projet vous a été utile !

## 📞 Contact

Pour toute question ou suggestion :
- 📧 Email : mouadaarab@gmail.com

---

*Développé avec ❤️ pour l'apprentissage du Machine Learning*
