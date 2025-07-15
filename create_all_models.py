#!/usr/bin/env python3
"""
Script principal pour créer tous les modèles de Machine Learning.

Ce script exécute tous les scripts de création de modèles :
- Random Forest
- Decision Tree  
- AdaBoost
- XGBoost
- SVM

Usage:
    python create_all_models.py
"""

import os
import sys
import subprocess
import time

def run_script(script_name):
    """
    Exécute un script et gère les erreurs.
    
    Args:
        script_name: Nom du script à exécuter
        
    Returns:
        bool: True si succès, False sinon
    """
    print(f"\n{'='*60}")
    print(f"🚀 Exécution de {script_name}...")
    print(f"{'='*60}")
    
    try:
        # Exécuter le script
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=False, 
                              check=True)
        
        print(f"✅ {script_name} terminé avec succès!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'exécution de {script_name}: {e}")
        return False
    except Exception as e:
        print(f"❌ Erreur inattendue avec {script_name}: {e}")
        return False

def main():
    """
    Fonction principale qui exécute tous les scripts de création de modèles.
    """
    print("🧠 CRÉATION DE TOUS LES MODÈLES DE MACHINE LEARNING")
    print("="*60)
    
    # Vérifier que nous sommes dans le bon répertoire
    scripts_dir = 'scripts'
    if not os.path.exists(scripts_dir):
        print("❌ Le dossier 'scripts' n'existe pas. Exécutez ce script depuis le dossier racine du projet.")
        return
    
    # Liste des scripts à exécuter
    scripts = [
        'scripts/create_random_forest_models.py',
        'scripts/create_decision_tree_models.py',
        'scripts/create_adaboost_models.py',
        'scripts/create_xgboost_models.py',
        'scripts/create_svm_models.py'
    ]
    
    # Statistiques
    start_time = time.time()
    success_count = 0
    total_scripts = len(scripts)
    
    # Exécuter chaque script
    for script in scripts:
        if os.path.exists(script):
            if run_script(script):
                success_count += 1
                time.sleep(2)  # Petite pause entre les scripts
            else:
                print(f"⚠️  Continuer avec les autres scripts...")
        else:
            print(f"❌ Script non trouvé: {script}")
    
    # Résumé final
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"\n{'='*60}")
    print("📊 RÉSUMÉ FINAL")
    print(f"{'='*60}")
    print(f"✅ Scripts réussis: {success_count}/{total_scripts}")
    print(f"⏱️  Temps total: {duration:.1f} secondes")
    
    if success_count == total_scripts:
        print("🎉 TOUS LES MODÈLES ONT ÉTÉ CRÉÉS AVEC SUCCÈS!")
        print("\n📁 Modèles disponibles dans models_ai/:")
        
        # Lister les modèles créés
        models_dir = 'models_ai'
        if os.path.exists(models_dir):
            models = os.listdir(models_dir)
            models.sort()
            
            # Grouper par algorithme
            algorithms = {}
            for model in models:
                if model.endswith('.pkl'):
                    algo = model.split('_')[0]
                    if algo not in algorithms:
                        algorithms[algo] = []
                    algorithms[algo].append(model)
            
            for algo, files in algorithms.items():
                print(f"\n🔹 {algo.upper()}:")
                for file in files:
                    print(f"   - {file}")
        
        print(f"\n🌐 Vous pouvez maintenant tester l'application Django:")
        print(f"   python manage.py runserver")
        
    else:
        print(f"⚠️  Certains modèles n'ont pas pu être créés.")
        print(f"Vérifiez les logs ci-dessus pour plus de détails.")

if __name__ == "__main__":
    main()
