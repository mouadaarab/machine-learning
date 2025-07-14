#!/bin/bash
# Script de mise en place du développement pour AI Platform Django
# Usage: ./setup_dev.sh

echo "🚀 Configuration de l'environnement de développement AI Platform..."

# Vérifier que Python 3 est installé
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

echo "✅ Python 3 détecté: $(python3 --version)"

# Créer l'environnement virtuel s'il n'existe pas
if [ ! -d ".venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv .venv
else
    echo "✅ Environnement virtuel existant détecté"
fi

# Activer l'environnement virtuel
echo "🔧 Activation de l'environnement virtuel..."
source .venv/bin/activate

# Mettre à jour pip
echo "⬆️  Mise à jour de pip..."
pip install --upgrade pip

# Installer les dépendances
echo "📚 Installation des dépendances..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "❌ Fichier requirements.txt non trouvé"
    exit 1
fi

# Créer les modèles ML s'ils n'existent pas
echo "🤖 Vérification des modèles ML..."
if [ ! -f "models_ai/random_forest_model.pkl" ]; then
    echo "📊 Création des modèles Random Forest..."
    python scripts/create_iris_model.py
    python scripts/create_california_housing_model.py
fi

if [ ! -f "models_ai/decision_tree_iris_model.pkl" ]; then
    echo "🌳 Création des modèles Decision Tree..."
    python scripts/create_decision_tree_models.py
fi

if [ ! -f "models_ai/adaboost_iris_model.pkl" ]; then
    echo "🚀 Création des modèles AdaBoost..."
    python scripts/create_adaboost_models.py
fi

# Appliquer les migrations Django
echo "🗄️  Application des migrations Django..."
python manage.py makemigrations
python manage.py migrate

# Collecter les fichiers statiques
echo "🎨 Collecte des fichiers statiques..."
python manage.py collectstatic --noinput --clear 2>/dev/null || echo "   ⚠️  Collecte des fichiers statiques ignorée (pas nécessaire en dev)"

# Vérifier l'installation
echo "🔍 Vérification de l'installation..."
python manage.py check

echo ""
echo "🎉 Configuration terminée avec succès!"
echo ""
echo "📋 Commandes utiles:"
echo "   - Démarrer le serveur: python manage.py runserver"
echo "   - Créer un superuser: python manage.py createsuperuser"
echo "   - Nettoyer le projet: ./cleanup.sh"
echo "   - Tests: python manage.py test"
echo ""
echo "🌐 Accès à l'application:"
echo "   - Interface principale: http://127.0.0.1:8000/"
echo "   - Admin Django: http://127.0.0.1:8000/admin/"
echo ""
echo "📚 Documentation disponible dans le README.md"
