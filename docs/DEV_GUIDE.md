# 🔧 Guide de Développement - AI Platform Django

## 📋 Avant de Commencer

### ✅ Checklist Pré-développement
- [ ] Environnement virtuel activé (`.venv`)
- [ ] Dépendances installées (`pip install -r requirements.txt`)
- [ ] Base de données migrée (`python manage.py migrate`)
- [ ] Modèles ML présents dans `models_ai/`

### 🚀 Configuration Rapide
```bash
./setup_dev.sh  # Configure tout automatiquement
```

## 🏗️ Structure du Projet

```
aiPlateform/
├── algosAi/                 # Application principale Django
│   ├── static/             # Images, PDFs, CSS, JS
│   ├── templates/          # Templates HTML
│   ├── views.py           # Logique métier
│   ├── urls.py            # Routes
│   └── models.py          # Modèles de données
├── models_ai/              # Modèles ML pré-entraînés
├── scripts/               # Scripts de création de modèles
├── aiPlateform/           # Configuration Django
├── manage.py              # Interface en ligne de commande Django
├── cleanup.sh             # Script de nettoyage
├── setup_dev.sh           # Script de configuration
└── requirements.txt       # Dépendances Python
```

## 🔄 Workflow de Développement

### 1. Avant de Coder
```bash
# Nettoyer le projet
./cleanup.sh

# Activer l'environnement virtuel
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Vérifier l'installation
python manage.py check
```

### 2. Développement
```bash
# Démarrer le serveur de développement
python manage.py runserver

# En parallèle, dans un autre terminal pour les modifications
python manage.py makemigrations  # Si changements de modèles
python manage.py migrate         # Appliquer les migrations
```

### 3. Tests
```bash
# Tester les algorithmes
python scripts/create_adaboost_models.py

# Vérifier Django
python manage.py check

# Tests unitaires (si disponibles)
python manage.py test
```

### 4. Avant de Commiter
```bash
# Nettoyer le projet
./cleanup.sh

# Vérifier l'état
git status
git diff
```

## 🧠 Ajouter un Nouvel Algorithme

### 1. Créer le Modèle ML
```python
# Dans scripts/create_nouveau_algo.py
def create_nouveau_algo_models():
    # Charger les données
    # Entraîner le modèle
    # Sauvegarder avec joblib.dump()
    pass
```

### 2. Ajouter les Vues Django
```python
# Dans algosAi/views.py
def nouveau_algo_details(request):
    return render(request, 'includes/nouveau_algo_details.html')

def nouveau_algo_iris_form(request):
    context = {
        'algorithm': 'NouveauAlgo',
        'action_url': reverse('algosAi:nouveau_algo_iris_results')
    }
    return render(request, 'includes/unified_iris_form.html', context)
```

### 3. Ajouter les Routes
```python
# Dans algosAi/urls.py
path('nouveau-algo/details/', views.nouveau_algo_details, name='nouveau_algo_details'),
path('nouveau-algo/iris/', views.nouveau_algo_iris_form, name='nouveau_algo_iris_form'),
```

### 4. Créer les Templates
- `templates/includes/nouveau_algo_details.html`
- Réutiliser `unified_iris_form.html` et `unified_iris_results.html`

### 5. Mettre à Jour la Page d'Accueil
```html
<!-- Dans templates/includes/index.html -->
<div class="algorithm-card">
    <h3>🆕 Nouveau Algorithme</h3>
    <p>Description de l'algorithme...</p>
    <a href="{% url 'algosAi:nouveau_algo_details' %}">Voir les détails</a>
</div>
```

## 🛠️ Commandes Utiles

### Django
```bash
# Gestion du serveur
python manage.py runserver              # Démarrer
python manage.py runserver 0.0.0.0:8000 # Accessible depuis le réseau

# Base de données
python manage.py makemigrations         # Créer les migrations
python manage.py migrate               # Appliquer les migrations
python manage.py dbshell               # Console base de données

# Utilitaires
python manage.py check                 # Vérifier la configuration
python manage.py collectstatic         # Collecter les fichiers statiques
python manage.py createsuperuser       # Créer un admin
```

### Git
```bash
# Workflow standard
git status                    # Voir l'état
git add .                    # Ajouter tous les fichiers
git commit -m "message"      # Commiter
git push                     # Pousser vers le dépôt

# Branches
git checkout -b nouvelle-feature  # Créer une nouvelle branche
git checkout main                # Retourner à main
git merge nouvelle-feature       # Fusionner la branche
```

### Python/ML
```bash
# Gestion des packages
pip list                     # Voir les packages installés
pip freeze > requirements.txt # Mettre à jour requirements.txt
pip install nouveau-package  # Installer un nouveau package

# Tests des modèles
python scripts/create_iris_model.py                    # Recréer Random Forest
python scripts/create_decision_tree_models.py          # Recréer Decision Tree
python scripts/create_adaboost_models.py              # Recréer AdaBoost
```

## 🐛 Débogage

### Problèmes Courants

#### 1. Erreur "ModuleNotFoundError"
```bash
# Vérifier l'environnement virtuel
which python
pip list

# Réinstaller les dépendances
pip install -r requirements.txt
```

#### 2. Erreur de Migration Django
```bash
# Supprimer et recréer les migrations
rm algosAi/migrations/0*.py
python manage.py makemigrations
python manage.py migrate
```

#### 3. Modèles ML Non Trouvés
```bash
# Recréer tous les modèles
python scripts/create_iris_model.py
python scripts/create_california_housing_model.py
python scripts/create_decision_tree_models.py
python scripts/create_adaboost_models.py
```

#### 4. Problèmes de Cache
```bash
# Nettoyer complètement
./cleanup.sh
python manage.py collectstatic --clear
```

## 📊 Monitoring et Performance

### Métriques à Surveiller
- **Temps de réponse** des prédictions
- **Précision** des modèles ML
- **Utilisation mémoire** des modèles chargés
- **Erreurs** dans les logs Django

### Optimisations Possibles
- **Cache des modèles** en mémoire
- **Optimisation des templates** Django
- **Compression** des fichiers statiques
- **Pagination** pour les gros datasets

## 🤝 Contribution

### Règles de Code
- **PEP 8** pour le style Python
- **Docstrings** pour toutes les fonctions
- **Commentaires** en français
- **Tests** pour les nouvelles fonctionnalités

### Workflow de Contribution
1. Fork du projet
2. Créer une branche feature
3. Développer et tester
4. Créer une Pull Request
5. Review et merge

---

**💡 Conseil** : Toujours tester localement avant de commiter !
