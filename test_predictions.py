#!/usr/bin/env python3
"""
Script de test pour comparer les prédictions de prix immobiliers 
entre les différents algorithmes (Random Forest, Decision Tree, AdaBoost).
"""

import os
import sys
import joblib
import numpy as np

# Ajouter le chemin du projet Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def load_model(model_name):
    """Charger un modèle depuis le dossier models_ai."""
    models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models_ai')
    model_path = os.path.join(models_dir, model_name)
    
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        print(f"❌ Modèle {model_name} non trouvé dans {models_dir}")
        return None

def test_housing_predictions():
    """Tester les prédictions de prix immobiliers avec tous les algorithmes."""
    
    print("🏠 Test des prédictions de prix immobiliers")
    print("=" * 60)
    
    # Charger les modèles
    models = {
        'Random Forest': load_model('california_housing_rf_model.pkl'),
        'Decision Tree': load_model('decision_tree_housing_model.pkl'),
        'AdaBoost': load_model('adaboost_housing_model.pkl')
    }
    
    # Exemples de données de test (features California Housing)
    test_cases = [
        {
            'name': 'Maison moyenne de Californie',
            'features': [5.0, 28.0, 5.5, 1.0, 3000.0, 3.0, 35.0, -119.0],
            'description': 'Revenu médian: 5.0, Âge: 28 ans, 5.5 pièces, 1 chambre, Population: 3000, Occupation: 3.0, Latitude: 35.0, Longitude: -119.0'
        },
        {
            'name': 'Maison de luxe (Bay Area)',
            'features': [8.3252, 41.0, 6.98, 1.02, 322.0, 2.56, 37.88, -122.23],
            'description': 'Revenu médian: 8.32, Âge: 41 ans, 6.98 pièces, 1.02 chambres, Population: 322, Occupation: 2.56, Lat: 37.88, Long: -122.23'
        },
        {
            'name': 'Maison économique',
            'features': [2.5, 15.0, 4.0, 1.0, 5000.0, 4.0, 34.0, -118.0],
            'description': 'Revenu médian: 2.5, Âge: 15 ans, 4.0 pièces, 1.0 chambre, Population: 5000, Occupation: 4.0, Latitude: 34.0, Longitude: -118.0'
        },
        {
            'name': 'Maison très chère (San Francisco)',
            'features': [15.0, 20.0, 8.0, 1.5, 500.0, 2.0, 37.78, -122.42],
            'description': 'Revenu médian: 15.0, Âge: 20 ans, 8.0 pièces, 1.5 chambres, Population: 500, Occupation: 2.0, Lat: 37.78, Long: -122.42'
        }
    ]
    
    for test_case in test_cases:
        print(f"\n📍 {test_case['name']}")
        print(f"   {test_case['description']}")
        print("   Prédictions:")
        
        for algo_name, model in models.items():
            if model is not None:
                try:
                    # Faire la prédiction
                    prediction = model.predict([test_case['features']])
                    price_raw = prediction[0]
                    
                    # Convertir en dollars (comme dans Django)
                    price_dollars = price_raw * 100000
                    
                    print(f"      {algo_name:15}: ${price_raw:.4f} (centaines de milliers) → ${price_dollars:,.2f}")
                    
                except Exception as e:
                    print(f"      {algo_name:15}: ❌ Erreur: {e}")
            else:
                print(f"      {algo_name:15}: ❌ Modèle non disponible")
        
        print("-" * 60)

def compare_model_ranges():
    """Comparer les gammes de prédictions des différents modèles."""
    
    print("\n🔍 Analyse des gammes de prédictions")
    print("=" * 60)
    
    # Charger les modèles
    models = {
        'Random Forest': load_model('california_housing_rf_model.pkl'),
        'Decision Tree': load_model('decision_tree_housing_model.pkl'),
        'AdaBoost': load_model('adaboost_housing_model.pkl')
    }
    
    # Générer des données de test aléatoires réalistes
    np.random.seed(42)
    n_samples = 100
    
    test_data = np.random.rand(n_samples, 8)
    # Normaliser selon les ranges réalistes du dataset California Housing
    test_data[:, 0] *= 15     # MedInc: 0-15
    test_data[:, 1] *= 50     # HouseAge: 0-50
    test_data[:, 2] = test_data[:, 2] * 10 + 3   # AveRooms: 3-13
    test_data[:, 3] = test_data[:, 3] * 3 + 0.5  # AveBedrms: 0.5-3.5
    test_data[:, 4] *= 10000  # Population: 0-10000
    test_data[:, 5] = test_data[:, 5] * 10 + 1   # AveOccup: 1-11
    test_data[:, 6] = test_data[:, 6] * 10 + 32  # Latitude: 32-42
    test_data[:, 7] = test_data[:, 7] * 10 - 125 # Longitude: -125 à -115
    
    for algo_name, model in models.items():
        if model is not None:
            try:
                predictions = model.predict(test_data)
                min_pred = np.min(predictions)
                max_pred = np.max(predictions)
                mean_pred = np.mean(predictions)
                std_pred = np.std(predictions)
                
                print(f"\n{algo_name}:")
                print(f"   Min: ${min_pred:.4f} (centaines de milliers) → ${min_pred*100000:,.2f}")
                print(f"   Max: ${max_pred:.4f} (centaines de milliers) → ${max_pred*100000:,.2f}")
                print(f"   Moyenne: ${mean_pred:.4f} (centaines de milliers) → ${mean_pred*100000:,.2f}")
                print(f"   Écart-type: ${std_pred:.4f}")
                
            except Exception as e:
                print(f"{algo_name}: ❌ Erreur: {e}")

if __name__ == "__main__":
    print("🧪 Tests de comparaison des algorithmes de prédiction")
    print("=" * 80)
    
    test_housing_predictions()
    compare_model_ranges()
    
    print("\n✅ Tests terminés!")
