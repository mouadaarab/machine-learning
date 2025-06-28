# 🧠 Scripts de Création des Modèles ML

Ce dossier contient les scripts pour créer et entraîner les modèles de Machine Learning utilisés dans l'application.

## 📁 Fichiers

### 🌸 Classification Iris
- **`create_iris_model.py`** : Crée le modèle Random Forest pour classifier les espèces d'iris
- **Performance** : ~97% de précision sur le test set

### 🏠 Régression California Housing  
- **`create_california_housing_model.py`** : Crée le modèle Random Forest pour prédire les prix immobiliers
- **Performance** : R² = 0.775 sur le test set

### 🌳 Decision Tree (Les Deux)
- **`create_decision_tree_models.py`** : Crée les modèles Decision Tree pour classification et régression
- **Performances** :
  - Iris : 100% de précision (parfait sur ce dataset simple)
  - California Housing : R² = 0.689

### 🚀 AdaBoost (Les Deux)
- **`create_adaboost_models.py`** : Crée les modèles AdaBoost pour classification et régression
- **Performances** :
  - Iris : 96.7% de précision (excellent avec boosting adaptatif)
  - California Housing : R² = 0.513

### 📚 Documentation
- **`MODEL_README.md`** : Documentation détaillée des modèles (si existant)

## 🚀 Utilisation

### Exécuter un Script
```bash
# Depuis le dossier racine du projet
cd aiPlateform

# Modèles Random Forest
python scripts/create_iris_model.py
python scripts/create_california_housing_model.py

# Modèles Decision Tree
python scripts/create_decision_tree_models.py

# Modèles AdaBoost
python scripts/create_adaboost_models.py
```

### Que Font les Scripts ?
1. **Chargement des données** : Datasets depuis scikit-learn
2. **Préparation** : Split train/test, preprocessing si nécessaire
3. **Entraînement** : Configuration et fit des modèles
4. **Évaluation** : Calcul des métriques de performance
5. **Sauvegarde** : Sérialisation avec joblib dans `models_ai/`

## 📊 Modèles Générés

Chaque script génère :
- **Modèle principal** : `.pkl` avec le modèle entraîné
- **Informations** : `_info.pkl` avec métadonnées et performance

### Structure des Informations
```python
model_info = {
    'model_type': 'RandomForestClassifier',
    'features': ['feature1', 'feature2', ...],
    'accuracy': 0.97,  # ou r2_score pour régression
    'feature_importance': [...]
}
```

## 🔧 Personnalisation

### Modifier les Hyperparamètres
Éditez les scripts pour ajuster :
- **n_estimators** : Nombre d'arbres (Random Forest)
- **max_depth** : Profondeur maximale
- **min_samples_split** : Échantillons minimum pour split
- **random_state** : Pour la reproductibilité

### Ajouter un Nouveau Modèle
1. Créez `create_votre_modele.py`
2. Suivez la structure des scripts existants
3. Sauvegardez dans `../models_ai/`
4. Mettez à jour les vues Django pour charger le nouveau modèle

## ⚠️ Notes Importantes

- **Dépendances** : Assurez-vous que scikit-learn, numpy, pandas et joblib sont installés
- **Emplacement** : Les modèles sont sauvés dans `../models_ai/` (relatif aux scripts)
- **Reproductibilité** : `random_state=42` pour des résultats cohérents
- **Performance** : Les métriques peuvent varier légèrement selon l'environnement

## 🔄 Régénération

Les modèles sont inclus dans le dépôt, mais vous pouvez les régénérer :
- Après modification des hyperparamètres
- Pour tester différentes configurations
- Pour mise à jour avec nouvelles versions de scikit-learn

---

*Ces scripts créent la base ML de l'application web interactive !*
