# Modèle Random Forest pour la Classification des Iris

Ce fichier contient la documentation pour le modèle Random Forest créé pour classifier les espèces d'iris dans le projet Django.

## 📁 Fichiers générés

- `random_forest_model.pkl` : Le modèle Random Forest entraîné
- `random_forest_model_info.pkl` : Informations détaillées sur les performances du modèle
- `create_iris_model.py` : Script de création du modèle

## 🌸 À propos du Dataset Iris

Le dataset Iris est un jeu de données classique en machine learning contenant :
- **150 échantillons** de fleurs d'iris
- **4 features** : longueur et largeur des sépales et pétales (en cm)
- **3 classes** : Setosa, Versicolor, Virginica

### Features utilisées :
1. `sepal_length` : Longueur du sépale (cm)
2. `sepal_width` : Largeur du sépale (cm)  
3. `petal_length` : Longueur du pétale (cm)
4. `petal_width` : Largeur du pétale (cm)

## 🌳 Performances du Modèle

- **Accuracy sur test** : ~90%
- **Validation croisée** : ~96.7% (±4.2%)
- **Features les plus importantes** :
  1. Largeur du pétale : ~43.7%
  2. Longueur du pétale : ~43.2%
  3. Longueur du sépale : ~11.6%
  4. Largeur du sépale : ~1.5%

## 🚀 Utilisation

### Dans l'application Django

Le modèle est automatiquement chargé par la fonction `load_models()` dans `views.py` :

```python
# Charger le modèle
rf_model = load_models('random_forest_model.pkl')

# Faire une prédiction
prediction = rf_model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
```

### Exemples de prédiction

```python
# Exemple Setosa (typique)
features = [5.1, 3.5, 1.4, 0.2]
prediction = rf_model.predict([features])  # Résultat : 0 (Setosa)

# Exemple Versicolor (typique)  
features = [7.0, 3.2, 4.7, 1.4]
prediction = rf_model.predict([features])  # Résultat : 1 (Versicolor)

# Exemple Virginica (typique)
features = [6.3, 3.3, 6.0, 2.5] 
prediction = rf_model.predict([features])  # Résultat : 2 (Virginica)
```

## 🔄 Régénérer le modèle

Pour créer un nouveau modèle avec des paramètres différents :

```bash
# Activer l'environnement virtuel
source .venv/bin/activate

# Exécuter le script
python create_iris_model.py
```

## 📊 Mapping des Classes

```python
iris_species = {
    0: 'Setosa',
    1: 'Versicolor', 
    2: 'Virginica'
}
```

## 🛠️ Dépendances

Les packages Python requis sont listés dans `requirements_ml.txt` :
- numpy>=1.21.0
- pandas>=1.3.0
- scikit-learn>=1.0.0
- joblib>=1.0.0

## 📈 Architecture du Modèle

**Random Forest Classifier** avec les paramètres :
- `n_estimators=100` : 100 arbres de décision
- `max_depth=None` : Pas de limite de profondeur
- `min_samples_split=2` : Minimum 2 échantillons pour diviser
- `min_samples_leaf=1` : Minimum 1 échantillon par feuille
- `random_state=42` : Pour la reproductibilité

## 🎯 Interprétation des Résultats

- **Classe 0 (Setosa)** : Généralement facile à classifier (100% de précision)
- **Classe 1 (Versicolor)** : Parfois confondue avec Virginica
- **Classe 2 (Virginica)** : Parfois confondue avec Versicolor

Les dimensions des pétales sont les caractéristiques les plus discriminantes pour la classification.
