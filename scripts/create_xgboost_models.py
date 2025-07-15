#!/usr/bin/env python3
"""
Script pour créer et sauvegarder des modèles XGBoost 
entraînés sur les datasets Iris et California Housing.

Ce script crée deux modèles XGBoost :
1. XGBClassifier pour la classification des espèces d'iris
2. XGBRegressor pour la prédiction des prix immobiliers californiens
"""

import os
import joblib
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, fetch_california_housing
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import (
    classification_report, confusion_matrix, accuracy_score,
    mean_squared_error, r2_score
)

try:
    import xgboost as xgb
    from xgboost import XGBClassifier, XGBRegressor
except ImportError:
    print("❌ XGBoost n'est pas installé. Installation en cours...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'xgboost'])
    import xgboost as xgb
    from xgboost import XGBClassifier, XGBRegressor


def create_xgboost_iris_model():
    """
    Crée et sauvegarde un modèle XGBoost pour la classification des espèces d'iris.
    
    Returns:
        XGBClassifier: Le modèle entraîné
        dict: Informations sur les performances du modèle
    """
    print("\n" + "="*60)
    print("🌸 Création du modèle XGBoost pour la classification Iris...")
    
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
    
    # Créer et entraîner le modèle XGBoost
    print("🚀 Entraînement du modèle XGBoost Classifier...")
    
    xgb_classifier = XGBClassifier(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        eval_metric='mlogloss'
    )
    
    xgb_classifier.fit(X_train, y_train)
    
    # Évaluer le modèle
    print("📈 Évaluation du modèle...")
    
    # Prédictions sur l'ensemble de test
    y_pred = xgb_classifier.predict(X_test)
    
    # Calculer l'accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"🎯 Accuracy sur l'ensemble de test: {accuracy:.4f} ({accuracy*100:.2f}%)")
    
    # Validation croisée
    cv_scores = cross_val_score(xgb_classifier, X, y, cv=5)
    print(f"🔄 Validation croisée (5-fold):")
    print(f"   - Score moyen: {cv_scores.mean():.4f} (±{cv_scores.std()*2:.4f})")
    
    # Rapport de classification détaillé
    print("\n📋 Rapport de classification:")
    print(classification_report(y_test, y_pred, target_names=target_names))
    
    # Matrice de confusion
    print("🔢 Matrice de confusion:")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    
    # Importance des features
    print("\n🏆 Importance des features:")
    feature_importance = pd.DataFrame({
        'feature': feature_names,
        'importance': xgb_classifier.feature_importances_
    }).sort_values('importance', ascending=False)
    
    for idx, row in feature_importance.iterrows():
        print(f"   {row['feature']}: {row['importance']:.4f}")
    
    # Sauvegarder le modèle
    models_dir = 'models_ai'
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
    
    model_path = os.path.join(models_dir, 'xgboost_iris_model.pkl')
    joblib.dump(xgb_classifier, model_path)
    
    # Informations sur le modèle
    model_info = {
        'model_type': 'XGBClassifier',
        'features': list(feature_names),
        'target_names': list(target_names),
        'n_estimators': 100,
        'max_depth': 6,
        'learning_rate': 0.1,
        'accuracy': accuracy,
        'cv_mean_score': cv_scores.mean(),
        'cv_std_score': cv_scores.std(),
        'feature_importance': feature_importance.to_dict('records'),
        'confusion_matrix': cm.tolist()
    }
    
    info_path = os.path.join(models_dir, 'xgboost_iris_model_info.pkl')
    joblib.dump(model_info, info_path)
    
    print(f"\n💾 Modèle sauvegardé:")
    print(f"   - Modèle: {model_path}")
    print(f"   - Informations: {info_path}")
    
    return xgb_classifier, model_info


def create_xgboost_housing_model():
    """
    Crée et sauvegarde un modèle XGBoost pour la prédiction des prix immobiliers californiens.
    
    Returns:
        XGBRegressor: Le modèle entraîné
        dict: Informations sur les performances du modèle
    """
    print("\n" + "="*60)
    print("🏠 Création du modèle XGBoost pour la régression California Housing...")
    
    # Charger le dataset California Housing
    california_housing = fetch_california_housing()
    X = california_housing.data
    y = california_housing.target
    feature_names = california_housing.feature_names
    
    print(f"📊 Dataset chargé avec succès:")
    print(f"   - Nombre d'échantillons: {X.shape[0]}")
    print(f"   - Nombre de features: {X.shape[1]}")
    print(f"   - Features: {feature_names}")
    print(f"   - Target: Prix des maisons (en centaines de milliers de dollars)")
    
    # Diviser les données
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"✂️  Division des données:")
    print(f"   - Entraînement: {X_train.shape[0]} échantillons")
    print(f"   - Test: {X_test.shape[0]} échantillons")
    
    # Créer et entraîner le modèle XGBoost
    print("🚀 Entraînement du modèle XGBoost Regressor...")
    
    xgb_regressor = XGBRegressor(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        eval_metric='rmse'
    )
    
    xgb_regressor.fit(X_train, y_train)
    
    # Évaluer le modèle
    print("📈 Évaluation du modèle...")
    
    # Prédictions sur l'ensemble de test
    y_pred = xgb_regressor.predict(X_test)
    
    # Calculer les métriques
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    print(f"📊 Performance du modèle:")
    print(f"   - Mean Squared Error: {mse:.4f}")
    print(f"   - Root Mean Squared Error: {rmse:.4f}")
    print(f"   - R² Score: {r2:.4f}")
    
    # Validation croisée pour la régression
    cv_scores = cross_val_score(xgb_regressor, X, y, cv=5, scoring='r2')
    print(f"🔄 Validation croisée R² (5-fold):")
    print(f"   - Score moyen: {cv_scores.mean():.4f} (±{cv_scores.std()*2:.4f})")
    
    # Importance des features
    print("\n🏆 Importance des features:")
    feature_importance = pd.DataFrame({
        'feature': feature_names,
        'importance': xgb_regressor.feature_importances_
    }).sort_values('importance', ascending=False)
    
    for idx, row in feature_importance.iterrows():
        print(f"   {row['feature']}: {row['importance']:.4f}")
    
    # Sauvegarder le modèle
    models_dir = 'models_ai'
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
    
    model_path = os.path.join(models_dir, 'xgboost_housing_model.pkl')
    joblib.dump(xgb_regressor, model_path)
    
    # Informations sur le modèle
    model_info = {
        'model_type': 'XGBRegressor',
        'features': list(feature_names),
        'n_estimators': 100,
        'max_depth': 6,
        'learning_rate': 0.1,
        'mse': mse,
        'rmse': rmse,
        'r2_score': r2,
        'cv_mean_score': cv_scores.mean(),
        'cv_std_score': cv_scores.std(),
        'feature_importance': feature_importance.to_dict('records')
    }
    
    info_path = os.path.join(models_dir, 'xgboost_housing_model_info.pkl')
    joblib.dump(model_info, info_path)
    
    print(f"\n💾 Modèle sauvegardé:")
    print(f"   - Modèle: {model_path}")
    print(f"   - Informations: {info_path}")
    
    return xgb_regressor, model_info


def test_iris_model():
    """
    Test rapide du modèle Iris avec des exemples.
    """
    print(f"\n🧪 Test du modèle XGBoost Iris...")
    
    model_path = os.path.join('models_ai', 'xgboost_iris_model.pkl')
    
    if not os.path.exists(model_path):
        print(f"❌ Modèle non trouvé: {model_path}")
        return
    
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


def test_housing_model():
    """
    Test rapide du modèle California Housing avec des exemples.
    """
    print(f"\n🧪 Test du modèle XGBoost California Housing...")
    
    model_path = os.path.join('models_ai', 'xgboost_housing_model.pkl')
    
    if not os.path.exists(model_path):
        print(f"❌ Modèle non trouvé: {model_path}")
        return
    
    # Charger le modèle
    model = joblib.load(model_path)
    
    # Exemples de test (valeurs moyennes typiques)
    test_samples = [
        [8.3252, 41.0, 6.984127, 1.023810, 322.0, 2.555556, 37.88, -122.23],  # San Francisco typique
        [5.6431, 25.0, 4.192308, 1.022222, 1392.0, 3.877778, 36.06, -119.01], # Central Valley typique
        [3.2596, 33.0, 3.257576, 1.017241, 2599.0, 4.466667, 34.03, -118.38]  # Los Angeles typique
    ]
    
    sample_names = ['San Francisco', 'Central Valley', 'Los Angeles']
    feature_names = [
        'MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 
        'Population', 'AveOccup', 'Latitude', 'Longitude'
    ]
    
    print("🔮 Prédictions sur des échantillons tests:")
    for i, (sample, name) in enumerate(zip(test_samples, sample_names)):
        prediction = model.predict([sample])[0]
        
        print(f"   {name}:")
        print(f"      Prédiction: ${prediction*100:.0f}k")
        print(f"      Features: {dict(zip(feature_names, sample))}")


def main():
    """
    Fonction principale pour créer les modèles XGBoost.
    """
    print("🚀 Création des modèles XGBoost")
    print("=" * 60)
    
    try:
        # Créer le modèle Iris
        iris_model, iris_info = create_xgboost_iris_model()
        
        # Créer le modèle California Housing
        housing_model, housing_info = create_xgboost_housing_model()
        
        # Tester les modèles
        test_iris_model()
        test_housing_model()
        
        print("\n🎉 Tous les modèles XGBoost ont été créés avec succès!")
        print("Les modèles sont prêts à être utilisés dans votre application Django.")
        
        return {
            'iris': {'model': iris_model, 'info': iris_info},
            'housing': {'model': housing_model, 'info': housing_info}
        }
        
    except Exception as e:
        print(f"❌ Erreur lors de la création des modèles: {str(e)}")
        raise


if __name__ == "__main__":
    models = main()
