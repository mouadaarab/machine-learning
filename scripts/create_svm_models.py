#!/usr/bin/env python3
"""
Script pour créer et sauvegarder des modèles SVM 
entraînés sur les datasets Iris et California Housing.

Ce script crée deux modèles SVM :
1. SVC pour la classification des espèces d'iris
2. SVR pour la prédiction des prix immobiliers californiens
"""

import os
import joblib
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, fetch_california_housing
from sklearn.svm import SVC, SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import (
    classification_report, confusion_matrix, accuracy_score,
    mean_squared_error, r2_score
)


def create_svm_iris_model():
    """
    Crée et sauvegarde un modèle SVM pour la classification des espèces d'iris.
    
    Returns:
        tuple: (SVC model, StandardScaler, dict) Le modèle entraîné, le scaler et les infos
    """
    print("\n" + "="*60)
    print("🌸 Création du modèle SVM pour la classification Iris...")
    
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
    
    # Normalisation des données (important pour SVM)
    print("🔧 Normalisation des données...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Créer et entraîner le modèle SVM
    print("🎯 Entraînement du modèle SVM Classifier...")
    
    svm_classifier = SVC(
        kernel='rbf',
        C=1.0,
        gamma='scale',
        probability=True,  # Pour avoir les probabilités
        random_state=42
    )
    
    svm_classifier.fit(X_train_scaled, y_train)
    
    # Évaluer le modèle
    print("📈 Évaluation du modèle...")
    
    # Prédictions sur l'ensemble de test
    y_pred = svm_classifier.predict(X_test_scaled)
    
    # Calculer l'accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"🎯 Accuracy sur l'ensemble de test: {accuracy:.4f} ({accuracy*100:.2f}%)")
    
    # Validation croisée (avec normalisation)
    X_scaled = scaler.fit_transform(X)
    cv_scores = cross_val_score(svm_classifier, X_scaled, y, cv=5)
    print(f"🔄 Validation croisée (5-fold):")
    print(f"   - Score moyen: {cv_scores.mean():.4f} (±{cv_scores.std()*2:.4f})")
    
    # Rapport de classification détaillé
    print("\n📋 Rapport de classification:")
    print(classification_report(y_test, y_pred, target_names=target_names))
    
    # Matrice de confusion
    print("🔢 Matrice de confusion:")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    
    # Informations sur le modèle SVM
    print(f"\n🏆 Informations du modèle SVM:")
    print(f"   - Kernel: {svm_classifier.kernel}")
    print(f"   - C (régularisation): {svm_classifier.C}")
    print(f"   - Gamma: {svm_classifier.gamma}")
    print(f"   - Nombre de vecteurs de support: {svm_classifier.n_support_}")
    
    # Sauvegarder le modèle et le scaler
    models_dir = 'models_ai'
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
    
    model_path = os.path.join(models_dir, 'svm_iris_model.pkl')
    scaler_path = os.path.join(models_dir, 'svm_iris_scaler.pkl')
    
    joblib.dump(svm_classifier, model_path)
    joblib.dump(scaler, scaler_path)
    
    # Informations sur le modèle
    model_info = {
        'model_type': 'SVC',
        'features': list(feature_names),
        'target_names': list(target_names),
        'kernel': svm_classifier.kernel,
        'C': svm_classifier.C,
        'gamma': svm_classifier.gamma,
        'accuracy': accuracy,
        'cv_mean_score': cv_scores.mean(),
        'cv_std_score': cv_scores.std(),
        'n_support_vectors': svm_classifier.n_support_.tolist(),
        'confusion_matrix': cm.tolist(),
        'scaler_path': scaler_path
    }
    
    info_path = os.path.join(models_dir, 'svm_iris_model_info.pkl')
    joblib.dump(model_info, info_path)
    
    print(f"\n💾 Modèle sauvegardé:")
    print(f"   - Modèle: {model_path}")
    print(f"   - Scaler: {scaler_path}")
    print(f"   - Informations: {info_path}")
    
    return svm_classifier, scaler, model_info


def create_svm_housing_model():
    """
    Crée et sauvegarde un modèle SVM pour la prédiction des prix immobiliers californiens.
    
    Returns:
        tuple: (SVR model, StandardScaler, dict) Le modèle entraîné, le scaler et les infos
    """
    print("\n" + "="*60)
    print("🏠 Création du modèle SVM pour la régression California Housing...")
    
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
    
    # Normalisation des données (crucial pour SVM)
    print("🔧 Normalisation des données...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Créer et entraîner le modèle SVM
    print("🎯 Entraînement du modèle SVM Regressor...")
    
    svm_regressor = SVR(
        kernel='rbf',
        C=1.0,
        gamma='scale',
        epsilon=0.1
    )
    
    svm_regressor.fit(X_train_scaled, y_train)
    
    # Évaluer le modèle
    print("📈 Évaluation du modèle...")
    
    # Prédictions sur l'ensemble de test
    y_pred = svm_regressor.predict(X_test_scaled)
    
    # Calculer les métriques
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    print(f"📊 Performance du modèle:")
    print(f"   - Mean Squared Error: {mse:.4f}")
    print(f"   - Root Mean Squared Error: {rmse:.4f}")
    print(f"   - R² Score: {r2:.4f}")
    
    # Validation croisée pour la régression (avec normalisation)
    X_scaled = scaler.fit_transform(X)
    cv_scores = cross_val_score(svm_regressor, X_scaled, y, cv=5, scoring='r2')
    print(f"🔄 Validation croisée R² (5-fold):")
    print(f"   - Score moyen: {cv_scores.mean():.4f} (±{cv_scores.std()*2:.4f})")
    
    # Informations sur le modèle SVM
    print(f"\n🏆 Informations du modèle SVM:")
    print(f"   - Kernel: {svm_regressor.kernel}")
    print(f"   - C (régularisation): {svm_regressor.C}")
    print(f"   - Gamma: {svm_regressor.gamma}")
    print(f"   - Epsilon: {svm_regressor.epsilon}")
    print(f"   - Nombre de vecteurs de support: {len(svm_regressor.support_)}")
    
    # Sauvegarder le modèle et le scaler
    models_dir = 'models_ai'
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
    
    model_path = os.path.join(models_dir, 'svm_housing_model.pkl')
    scaler_path = os.path.join(models_dir, 'svm_housing_scaler.pkl')
    
    joblib.dump(svm_regressor, model_path)
    joblib.dump(scaler, scaler_path)
    
    # Informations sur le modèle
    model_info = {
        'model_type': 'SVR',
        'features': list(feature_names),
        'kernel': svm_regressor.kernel,
        'C': svm_regressor.C,
        'gamma': svm_regressor.gamma,
        'epsilon': svm_regressor.epsilon,
        'mse': mse,
        'rmse': rmse,
        'r2_score': r2,
        'cv_mean_score': cv_scores.mean(),
        'cv_std_score': cv_scores.std(),
        'n_support_vectors': len(svm_regressor.support_),
        'scaler_path': scaler_path
    }
    
    info_path = os.path.join(models_dir, 'svm_housing_model_info.pkl')
    joblib.dump(model_info, info_path)
    
    print(f"\n💾 Modèle sauvegardé:")
    print(f"   - Modèle: {model_path}")
    print(f"   - Scaler: {scaler_path}")
    print(f"   - Informations: {info_path}")
    
    return svm_regressor, scaler, model_info


def test_iris_model():
    """
    Test rapide du modèle Iris avec des exemples.
    """
    print(f"\n🧪 Test du modèle SVM Iris...")
    
    model_path = os.path.join('models_ai', 'svm_iris_model.pkl')
    scaler_path = os.path.join('models_ai', 'svm_iris_scaler.pkl')
    
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        print(f"❌ Modèle ou scaler non trouvé: {model_path}, {scaler_path}")
        return
    
    # Charger le modèle et le scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    
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
        # Normaliser l'échantillon
        sample_scaled = scaler.transform([sample])
        prediction = model.predict(sample_scaled)[0]
        probability = model.predict_proba(sample_scaled)[0]
        
        print(f"   {name}:")
        print(f"      Features: {sample}")
        print(f"      Prédiction: {class_names[prediction]}")
        print(f"      Probabilités: {dict(zip(class_names, probability.round(4)))}")


def test_housing_model():
    """
    Test rapide du modèle California Housing avec des exemples.
    """
    print(f"\n🧪 Test du modèle SVM California Housing...")
    
    model_path = os.path.join('models_ai', 'svm_housing_model.pkl')
    scaler_path = os.path.join('models_ai', 'svm_housing_scaler.pkl')
    
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        print(f"❌ Modèle ou scaler non trouvé: {model_path}, {scaler_path}")
        return
    
    # Charger le modèle et le scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    
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
        # Normaliser l'échantillon
        sample_scaled = scaler.transform([sample])
        prediction = model.predict(sample_scaled)[0]
        
        print(f"   {name}:")
        print(f"      Prédiction: ${prediction*100:.0f}k")
        print(f"      Features: {dict(zip(feature_names, sample))}")


def main():
    """
    Fonction principale pour créer les modèles SVM.
    """
    print("🚀 Création des modèles SVM")
    print("=" * 60)
    
    try:
        # Créer le modèle Iris
        iris_model, iris_scaler, iris_info = create_svm_iris_model()
        
        # Créer le modèle California Housing
        housing_model, housing_scaler, housing_info = create_svm_housing_model()
        
        # Tester les modèles
        test_iris_model()
        test_housing_model()
        
        print("\n🎉 Tous les modèles SVM ont été créés avec succès!")
        print("Les modèles sont prêts à être utilisés dans votre application Django.")
        
        return {
            'iris': {'model': iris_model, 'scaler': iris_scaler, 'info': iris_info},
            'housing': {'model': housing_model, 'scaler': housing_scaler, 'info': housing_info}
        }
        
    except Exception as e:
        print(f"❌ Erreur lors de la création des modèles: {str(e)}")
        raise


if __name__ == "__main__":
    models = main()
