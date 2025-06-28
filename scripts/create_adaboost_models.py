#!/usr/bin/env python3
"""
Script pour créer et sauvegarder des modèles AdaBoost 
entraînés sur les datasets Iris et California Housing.

Ce script crée deux modèles AdaBoost :
1. AdaBoostClassifier pour la classification des espèces d'iris
2. AdaBoostRegressor pour la prédiction des prix immobiliers californiens
"""

import os
import joblib
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, fetch_california_housing
from sklearn.ensemble import AdaBoostClassifier, AdaBoostRegressor
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import (
    classification_report, confusion_matrix, accuracy_score,
    mean_squared_error, r2_score
)


def create_adaboost_iris_model():
    """
    Crée et sauvegarde un modèle AdaBoost pour la classification des espèces d'iris.
    
    Returns:
        AdaBoostClassifier: Le modèle entraîné
        dict: Informations sur les performances du modèle
    """
    print("\n" + "="*60)
    print("🌸 Création du modèle AdaBoost pour la classification Iris...")
    
    # Charger le dataset Iris
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names
    
    print(f"📊 Dataset chargé avec succès:")
    print(f"   - Nombre d'échantillons: {X.shape[0]}")
    print(f"   - Nombre de features: {X.shape[1]}")
    print(f"   - Classes: {target_names}")
    
    # Diviser les données
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"✂️  Division des données:")
    print(f"   - Entraînement: {X_train.shape[0]} échantillons")
    print(f"   - Test: {X_test.shape[0]} échantillons")
    
    # Créer et entraîner le modèle AdaBoost
    print("🚀 Entraînement du modèle AdaBoost...")
    
    # Estimateur de base : DecisionTree avec profondeur limitée (weak learner)
    base_estimator = DecisionTreeClassifier(max_depth=1, random_state=42)
    
    ada_classifier = AdaBoostClassifier(
        estimator=base_estimator,
        n_estimators=100,          # Nombre d'estimateurs faibles
        learning_rate=1.0,         # Taux d'apprentissage
        algorithm='SAMME',         # Algorithme SAMME
        random_state=42
    )
    
    ada_classifier.fit(X_train, y_train)
    
    # Évaluer le modèle
    print("📈 Évaluation du modèle...")
    
    # Prédictions sur l'ensemble de test
    y_pred = ada_classifier.predict(X_test)
    
    # Calculer l'accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"🎯 Accuracy sur l'ensemble de test: {accuracy:.4f} ({accuracy*100:.2f}%)")
    
    # Validation croisée
    cv_scores = cross_val_score(ada_classifier, X, y, cv=5)
    print(f"🔄 Validation croisée (5-fold):")
    print(f"   - Score moyen: {cv_scores.mean():.4f} (±{cv_scores.std()*2:.4f})")
    
    # Rapport de classification détaillé
    print("\n📋 Rapport de classification:")
    print(classification_report(y_test, y_pred, target_names=target_names))
    
    # Matrice de confusion
    print("🔢 Matrice de confusion:")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    
    # Importance des features (moyenne des importances des estimateurs)
    print("\n🏆 Importance des features:")
    feature_importance = pd.DataFrame({
        'feature': feature_names,
        'importance': ada_classifier.feature_importances_
    }).sort_values('importance', ascending=False)
    
    for idx, row in feature_importance.iterrows():
        print(f"   {row['feature']}: {row['importance']:.4f}")
    
    # Sauvegarder le modèle
    models_dir = 'models_ai'
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
    
    model_path = os.path.join(models_dir, 'adaboost_iris_model.pkl')
    joblib.dump(ada_classifier, model_path)
    
    # Informations sur le modèle
    model_info = {
        'model_type': 'AdaBoostClassifier',
        'features': list(feature_names),
        'target_names': list(target_names),
        'n_estimators': 100,
        'learning_rate': 1.0,
        'accuracy': accuracy,
        'cv_mean_score': cv_scores.mean(),
        'cv_std_score': cv_scores.std(),
        'feature_importance': feature_importance.to_dict('records'),
        'confusion_matrix': cm.tolist(),
        'algorithm': 'SAMME',
        'base_estimator': 'DecisionTreeClassifier(max_depth=1)'
    }
    
    info_path = os.path.join(models_dir, 'adaboost_iris_model_info.pkl')
    joblib.dump(model_info, info_path)
    
    print(f"\n💾 Modèle sauvegardé vers: {model_path}")
    print(f"💾 Informations sauvegardées vers: {info_path}")
    
    return ada_classifier, model_info


def create_adaboost_housing_model():
    """
    Crée et sauvegarde un modèle AdaBoost pour la régression des prix immobiliers californiens.
    
    Returns:
        AdaBoostRegressor: Le modèle entraîné
        dict: Informations sur les performances du modèle
    """
    print("\n" + "="*60)
    print("🏠 Création du modèle AdaBoost pour la régression California Housing...")
    
    # Charger le dataset California Housing
    california_housing = fetch_california_housing()
    X = california_housing.data
    y = california_housing.target
    feature_names = california_housing.feature_names
    
    print(f"📊 Dataset chargé avec succès:")
    print(f"   - Nombre d'échantillons: {X.shape[0]}")
    print(f"   - Nombre de features: {X.shape[1]}")
    print(f"   - Features: {list(feature_names)}")
    print(f"   - Variable cible: Prix des maisons (en centaines de milliers de dollars)")
    
    # Diviser les données
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"✂️  Division des données:")
    print(f"   - Entraînement: {X_train.shape[0]} échantillons")
    print(f"   - Test: {X_test.shape[0]} échantillons")
    
    # Créer et entraîner le modèle AdaBoost
    print("🚀 Entraînement du modèle AdaBoost...")
    
    # Estimateur de base : DecisionTree avec profondeur limitée (weak learner)
    base_estimator = DecisionTreeRegressor(max_depth=4, random_state=42)
    
    ada_regressor = AdaBoostRegressor(
        estimator=base_estimator,
        n_estimators=100,          # Nombre d'estimateurs faibles
        learning_rate=1.0,         # Taux d'apprentissage
        loss='linear',             # Fonction de perte linéaire
        random_state=42
    )
    
    ada_regressor.fit(X_train, y_train)
    
    # Faire des prédictions
    y_pred = ada_regressor.predict(X_test)
    
    # Calculer les métriques
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    print(f"\n📈 Performance du modèle:")
    print(f"   - Mean Squared Error: {mse:.4f}")
    print(f"   - Root Mean Squared Error: {rmse:.4f}")
    print(f"   - R² Score: {r2:.4f}")
    
    # Importance des features
    feature_importance = pd.DataFrame({
        'feature': feature_names,
        'importance': ada_regressor.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\n🏆 Importance des features:")
    for idx, row in feature_importance.iterrows():
        print(f"   {row['feature']}: {row['importance']:.4f}")
    
    # Sauvegarder le modèle
    models_dir = 'models_ai'
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
    
    model_path = os.path.join(models_dir, 'adaboost_housing_model.pkl')
    joblib.dump(ada_regressor, model_path)
    
    # Informations sur le modèle
    model_info = {
        'model_type': 'AdaBoostRegressor',
        'features': list(feature_names),
        'n_estimators': 100,
        'learning_rate': 1.0,
        'loss': 'linear',
        'mse': mse,
        'rmse': rmse,
        'r2_score': r2,
        'feature_importance': feature_importance.to_dict('records'),
        'base_estimator': 'DecisionTreeRegressor(max_depth=4)'
    }
    
    info_path = os.path.join(models_dir, 'adaboost_housing_model_info.pkl')
    joblib.dump(model_info, info_path)
    
    print(f"\n💾 Modèle sauvegardé vers: {model_path}")
    print(f"💾 Informations sauvegardées vers: {info_path}")
    
    return ada_regressor, model_info


def test_models():
    """
    Teste les modèles AdaBoost sauvegardés avec des exemples.
    """
    print("\n" + "="*60)
    print("🧪 Test des modèles AdaBoost...")
    
    # Test du modèle Iris
    print("\n🌸 Test du modèle AdaBoost Iris:")
    iris_model = joblib.load('models_ai/adaboost_iris_model.pkl')
    
    # Exemples de test pour Iris
    test_samples = [
        [5.1, 3.5, 1.4, 0.2],  # Setosa typique
        [7.0, 3.2, 4.7, 1.4],  # Versicolor typique
        [6.3, 3.3, 6.0, 2.5]   # Virginica typique
    ]
    
    sample_names = ['Setosa typique', 'Versicolor typique', 'Virginica typique']
    class_names = ['Setosa', 'Versicolor', 'Virginica']
    
    for i, (sample, name) in enumerate(zip(test_samples, sample_names)):
        prediction = iris_model.predict([sample])[0]
        probability = iris_model.predict_proba([sample])[0]
        
        print(f"   {name}:")
        print(f"      Features: {sample}")
        print(f"      Prédiction: {class_names[prediction]}")
        print(f"      Probabilités: {dict(zip(class_names, probability.round(4)))}")
    
    # Test du modèle Housing
    print("\n🏠 Test du modèle AdaBoost Housing:")
    housing_model = joblib.load('models_ai/adaboost_housing_model.pkl')
    
    # Exemple de test pour Housing (valeurs moyennes)
    test_house = [8.3252, 41.0, 6.98, 1.02, 322.0, 2.56, 37.88, -122.23]
    prediction = housing_model.predict([test_house])[0]
    
    print(f"   Maison d'exemple:")
    print(f"      Features: {test_house}")
    print(f"      Prix prédit: ${prediction:.2f}00 (centaines de milliers)")


def main():
    """
    Fonction principale pour créer les modèles AdaBoost.
    """
    print("🚀 Création des modèles AdaBoost")
    print("=" * 60)
    
    try:
        # Créer les modèles
        iris_model, iris_info = create_adaboost_iris_model()
        housing_model, housing_info = create_adaboost_housing_model()
        
        # Tester les modèles
        test_models()
        
        print("\n" + "="*60)
        print("🎉 Modèles AdaBoost créés avec succès!")
        print(f"📈 Iris Classification - Accuracy: {iris_info['accuracy']:.2f}%")
        print(f"📈 California Housing - R² Score: {housing_info['r2_score']:.4f}")
        print("\nLes modèles sont prêts à être utilisés dans votre application Django.")
        
    except Exception as e:
        print(f"❌ Erreur lors de la création des modèles: {str(e)}")
        raise


if __name__ == "__main__":
    main()
