#!/bin/bash
# Script de nettoyage du projet AI Platform Django
# Usage: ./cleanup.sh

echo "🧹 Nettoyage du projet AI Platform..."

# Supprimer les fichiers de cache Python
echo "📂 Suppression des fichiers de cache Python..."
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
find . -name "*.pyc" -delete 2>/dev/null || true
find . -name "*.pyo" -delete 2>/dev/null || true

# Supprimer les fichiers système
echo "🗑️  Suppression des fichiers système..."
find . -name ".DS_Store" -delete 2>/dev/null || true
find . -name "Thumbs.db" -delete 2>/dev/null || true
find . -name "desktop.ini" -delete 2>/dev/null || true

# Supprimer les fichiers temporaires
echo "🗂️  Suppression des fichiers temporaires..."
find . -name "*~" -delete 2>/dev/null || true
find . -name "*.tmp" -delete 2>/dev/null || true
find . -name "*.temp" -delete 2>/dev/null || true

# Supprimer les bases de données temporaires
echo "🗄️  Suppression des bases de données temporaires..."
rm -f ssdb.sqlite3 2>/dev/null || true
rm -f *_temp.db 2>/dev/null || true

# Supprimer les dossiers de test
echo "🧪 Suppression des dossiers de test temporaires..."
rm -rf tests/ 2>/dev/null || true

# Supprimer les logs
echo "📜 Suppression des logs..."
find . -name "*.log" -delete 2>/dev/null || true

# Nettoyer les environnements virtuels temporaires
echo "🔧 Vérification des environnements virtuels..."
if [ -d ".venv_temp" ]; then
    rm -rf .venv_temp
    echo "   ✅ Environnement virtuel temporaire supprimé"
fi

# Nettoyer les fichiers de migration orphelins (optionnel)
echo "🗃️  Nettoyage des migrations..."
find . -path "*/migrations/__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

echo ""
echo "✅ Nettoyage terminé!"
echo ""
echo "📊 Statistiques du projet:"
echo "   - Fichiers Python: $(find . -name "*.py" | wc -l | tr -d ' ')"
echo "   - Templates HTML: $(find . -name "*.html" | wc -l | tr -d ' ')"
echo "   - Modèles ML: $(find models_ai/ -name "*.pkl" 2>/dev/null | wc -l | tr -d ' ')"
echo "   - Scripts: $(find scripts/ -name "*.py" 2>/dev/null | wc -l | tr -d ' ')"
echo ""
echo "🚀 Le projet est maintenant propre et prêt à être utilisé!"
