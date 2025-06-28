#!/usr/bin/env python3
"""
Script pour créer et sauvegarder un modèle Random Forest 
entraîné sur le dataset Iris.

Ce script charge le dataset Iris, entraîne un modèle Random Forest,
évalue ses performances et sauvegarde le modèle dans le dossier models_ai.
"""

import os
import joblib
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def create_iris_random_forest_model():
    """
    Crée et entraîne un modèle Random Forest sur le dataset Iris.
    
    Returns:
        RandomForestClassifier: Le modèle entraîné
        dict: Informations sur les performances du modèle
    """
    print("🌸 Chargement du dataset Iris...")
    
    # Charger le dataset Iris
    iris = load_iris()
    X = iris.data  # Features: sepal_length, sepal_width, petal_length, petal_width
    y = iris.target  # Target: 0=Setosa, 1=Versicolor, 2=Virginica
    
    print(f"📊 Dataset chargé avec succès:")
    print(f"   - Nombre d'échantillons: {X.shape[0]}")
    print(f"   - Nombre de features: {X.shape[1]}")
    print(f"   - Classes: {iris.target_names}")
    
    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"✂️  Division des données:")
    print(f"   - Entraînement: {X_train.shape[0]} échantillons")
    print(f"   - Test: {X_test.shape[0]} échantillons")
    
    # Créer et entraîner le modèle Random Forest
    print("🌳 Entraînement du modèle Random Forest...")
    
    rf_model = RandomForestClassifier(
        n_estimators=100,          # Nombre d'arbres
        max_depth=None,            # Profondeur maximale (None = pas de limite)
        min_samples_split=2,       # Minimum d'échantillons pour diviser un nœud
        min_samples_leaf=1,        # Minimum d'échantillons dans une feuille
        random_state=42           # Pour la reproductibilité
    )
    
    rf_model.fit(X_train, y_train)
    
    # Évaluer le modèle
    print("📈 Évaluation du modèle...")
    
    # Prédictions sur l'ensemble de test
    y_pred = rf_model.predict(X_test)
    
    # Calculer l'accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"🎯 Accuracy sur l'ensemble de test: {accuracy:.4f} ({accuracy*100:.2f}%)")
    
    # Validation croisée
    cv_scores = cross_val_score(rf_model, X, y, cv=5)
    print(f"🔄 Validation croisée (5-fold):")
    print(f"   - Score moyen: {cv_scores.mean():.4f} (±{cv_scores.std()*2:.4f})")
    
    # Rapport de classification détaillé
    print("\n📋 Rapport de classification:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))
    
    # Matrice de confusion
    print("🔢 Matrice de confusion:")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    
    # Importance des features
    print("\n🏆 Importance des features:")
    feature_importance = pd.DataFrame({
        'feature': iris.feature_names,
        'importance': rf_model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    for idx, row in feature_importance.iterrows():
        print(f"   {row['feature']}: {row['importance']:.4f}")
    
    # Informations sur le modèle
    model_info = {
        'accuracy': accuracy,
        'cv_mean_score': cv_scores.mean(),
        'cv_std_score': cv_scores.std(),
        'feature_importance': feature_importance.to_dict('records'),
        'confusion_matrix': cm.tolist(),
        'classes': list(iris.target_names),
        'feature_names': list(iris.feature_names)
    }
    
    return rf_model, model_info

def save_model(model, model_info, model_path):
    """
    Sauvegarde le modèle et ses informations.
    
    Args:
        model: Le modèle entraîné
        model_info: Informations sur le modèle
        model_path: Chemin où sauvegarder le modèle
    """
    print(f"💾 Sauvegarde du modèle vers: {model_path}")
    
    # Créer le dossier s'il n'existe pas
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    
    # Sauvegarder le modèle
    joblib.dump(model, model_path)
    
    # Sauvegarder les informations du modèle
    info_path = model_path.replace('.pkl', '_info.pkl')
    joblib.dump(model_info, info_path)
    
    print(f"✅ Modèle sauvegardé avec succès!")
    print(f"   - Modèle: {model_path}")
    print(f"   - Informations: {info_path}")

def test_model(model_path):
    """
    Test rapide du modèle sauvegardé avec des exemples.
    
    Args:
        model_path: Chemin vers le modèle sauvegardé
    """
    print(f"\n🧪 Test du modèle chargé depuis: {model_path}")
    
    # Charger le modèle
    model = joblib.load(model_path)
    
    # Exemples de test (mesures typiques pour chaque classe)
    test_samples = [
        [5.1, 3.5, 1.4, 0.2],  # Setosa typique
        [7.0, 3.2, 4.7, 1.4],  # Versicolor typique
        [6.3, 3.3, 6.0, 2.5]   # Virginica typique
    ]
    
    sample_names = ['Setosa typique', 'Versicolor typique', 'Virginica typique']
    class_names = ['Setosa', 'Versicolor', 'Virginica']
    
    print("🔮 Prédictions sur des échantillons tests:")
    for i, (sample, name) in enumerate(zip(test_samples, sample_names)):
        prediction = model.predict([sample])[0]
        probability = model.predict_proba([sample])[0]
        
        print(f"   {name}:")
        print(f"      Features: {sample}")
        print(f"      Prédiction: {class_names[prediction]}")
        print(f"      Probabilités: {dict(zip(class_names, probability.round(4)))}")

def main():
    """
    Fonction principale pour créer le modèle Random Forest Iris.
    """
    print("🚀 Création du modèle Random Forest pour le dataset Iris")
    print("=" * 60)
    
    try:
        # Créer et entraîner le modèle
        model, model_info = create_iris_random_forest_model()
        
        # Définir le chemin de sauvegarde
        base_dir = os.path.dirname(os.path.abspath(__file__))
        models_dir = os.path.join(base_dir, 'models_ai')
        model_path = os.path.join(models_dir, 'random_forest_model.pkl')
        
        # Sauvegarder le modèle
        save_model(model, model_info, model_path)
        
        # Tester le modèle
        test_model(model_path)
        
        print("\n🎉 Processus terminé avec succès!")
        print(f"Le modèle est prêt à être utilisé dans votre application Django.")
        
    except Exception as e:
        print(f"❌ Erreur lors de la création du modèle: {str(e)}")
        raise

if __name__ == "__main__":
    main()
