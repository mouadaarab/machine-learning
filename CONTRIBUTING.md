# 🤝 Guide de Contribution

Merci de votre intérêt pour contribuer à AI Platform Django ! Ce guide vous aidera à contribuer efficacement au projet.

## 📋 Types de Contributions

Nous accueillons différents types de contributions :

- 🐛 **Correction de bugs**
- ✨ **Nouvelles fonctionnalités**
- 📚 **Amélioration de la documentation**
- 🎨 **Améliorations UI/UX**
- 🧠 **Nouveaux algorithmes ML**
- 🧪 **Tests unitaires**
- ⚡ **Optimisations de performance**

## 🚀 Comment Contribuer

### 1. Préparation
1. **Forkez** le dépôt sur GitHub
2. **Clonez** votre fork localement :
   ```bash
   git clone https://github.com/votre-username/ai-platform-django.git
   cd ai-platform-django/aiPlateform
   ```
3. **Configurez** le remote upstream :
   ```bash
   git remote add upstream https://github.com/original-repo/ai-platform-django.git
   ```

### 2. Environnement de Développement
1. **Créez** un environnement virtuel :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur macOS/Linux
   # ou
   venv\\Scripts\\activate   # Sur Windows
   ```
2. **Installez** les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. **Lancez** les tests pour vérifier que tout fonctionne :
   ```bash
   python manage.py check
   python manage.py runserver
   ```

### 3. Développement
1. **Créez** une branche pour votre fonctionnalité :
   ```bash
   git checkout -b feature/nom-de-votre-fonctionnalite
   ```
2. **Développez** votre fonctionnalité
3. **Testez** vos modifications
4. **Committez** avec des messages clairs :
   ```bash
   git commit -m "feat: ajout de l'algorithme SVM pour classification"
   ```

### 4. Soumission
1. **Pushez** votre branche :
   ```bash
   git push origin feature/nom-de-votre-fonctionnalite
   ```
2. **Créez** une Pull Request sur GitHub
3. **Décrivez** clairement vos changements

## 📝 Standards de Code

### Python / Django
- Suivez **PEP 8** pour le style de code
- Utilisez des **docstrings** pour documenter les fonctions
- **Noms explicites** pour les variables et fonctions
- **Commentaires** pour la logique complexe

### HTML / CSS
- **Indentation** de 2 espaces
- **Classes CSS** en kebab-case
- **Structure sémantique** HTML5
- **Responsive design** avec Bootstrap

### JavaScript
- **Indentation** de 2 espaces
- **Noms de variables** en camelCase
- **Commentaires** pour les fonctions complexes

## 🧠 Ajouter un Nouvel Algorithme

Pour ajouter un nouvel algorithme de ML :

### 1. Script de Création du Modèle
Créez `scripts/create_votre_algorithme.py` :
```python
def create_votre_algorithme_model():
    # Chargement des données
    # Entraînement du modèle
    # Sauvegarde avec joblib
    pass
```

### 2. Routes
Ajoutez dans `algosAi/urls.py` :
```python
path('votre_algo_details/', views.votre_algo_details, name='votre_algo_details'),
path('votre_algo_iris/', views.votre_algo_iris, name='votre_algo_iris'),
# etc.
```

### 3. Vues
Utilisez les templates unifiés dans `algosAi/views.py` :
```python
def votre_algo_iris_tester(request):
    context = {
        'algorithm': 'Votre Algorithme',
        'algorithm_info': 'Description spécifique...',
        'action_url': reverse('algosAi:votre_algo_iris_results')
    }
    return render(request, 'includes/unified_iris_form.html', context)
```

### 4. Page de Détails
Créez `templates/includes/votre_algo_details.html`

### 5. Mise à Jour de l'Index
Ajoutez la carte de votre algorithme dans `templates/includes/index.html`

## 🧪 Tests

### Tests Manuels
- Testez toutes les fonctionnalités modifiées
- Vérifiez la responsivité sur différentes tailles d'écran
- Testez avec différents navigateurs

### Tests Automatisés (Future)
- Tests unitaires avec `pytest`
- Tests d'intégration Django
- Tests de performance

## 📚 Documentation

### README
- Mettez à jour le README si nécessaire
- Ajoutez des captures d'écran pour les nouvelles fonctionnalités

### Commentaires Code
- Documentez les fonctions complexes
- Expliquez la logique métier
- Ajoutez des TODO pour les améliorations futures

## 🐛 Rapporter des Bugs

### Issues GitHub
Créez une issue avec :
- **Titre clair** décrivant le problème
- **Description détaillée** avec étapes de reproduction
- **Environnement** (OS, Python, navigateur)
- **Captures d'écran** si pertinent

### Template d'Issue
```
## Description
Brève description du bug

## Reproduction
1. Allez sur la page X
2. Cliquez sur Y
3. Observez Z

## Comportement Attendu
Ce qui devrait se passer

## Comportement Actuel
Ce qui se passe réellement

## Environnement
- OS: [e.g. macOS 12.0]
- Python: [e.g. 3.9]
- Django: [e.g. 5.0]
- Navigateur: [e.g. Chrome 96]
```

## ✨ Suggestions d'Améliorations

### Ideas Bienvenues
- **Nouveaux algorithmes** (SVM, Neural Networks, etc.)
- **Visualisations** de données et résultats
- **Interface utilisateur** améliorée
- **API REST** pour accès programmatique
- **Tests automatisés**

### Processus de Suggestion
1. **Vérifiez** les issues existantes
2. **Créez** une nouvelle issue avec le label "enhancement"
3. **Décrivez** clairement la valeur ajoutée
4. **Proposez** une implémentation si possible

## 📞 Communication

### Channels
- **GitHub Issues** : Pour bugs et suggestions
- **GitHub Discussions** : Pour questions générales
- **Pull Requests** : Pour revue de code

### Guidelines
- Soyez **respectueux** et constructif
- **Recherchez** avant de poser une question
- **Documentez** vos contributions
- **Testez** avant de soumettre

## 🏆 Reconnaissance

Les contributeurs seront ajoutés au README principal. Merci pour votre contribution !

## 📄 Code de Conduite

En participant à ce projet, vous acceptez de maintenir un environnement respectueux et inclusif pour tous.

---

*Merci de contribuer à rendre l'apprentissage du Machine Learning plus accessible !*
