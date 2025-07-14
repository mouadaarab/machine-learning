from django.shortcuts import render
from django.urls import reverse
import os
import joblib

# Create your views here.
def index(request):
    """
    Render the index page.
    """
    return render(request, 'includes/index.html')

def rf_details(request):
    """
    Render the random forest details page.
    """
    return render(request, 'includes/rf_details.html')

def rf_iris(request):
    """
    Render the random forest classification example page.
    """
    return render(request, 'includes/rf_iris.html')

def rf_iris_exemple_tester(request):
    """
    Render the random forest iris example tester page using unified template.
    """
    context = {
        'algorithm': 'Random Forest',
        'algorithm_info': 'Utilise 100 arbres de décision pour une classification robuste et précise.',
        'action_url': reverse('algosAi:rf_iris_prediction_results')
    }
    return render(request, 'includes/unified_iris_form.html', context)

def rf_iris_prediction_results(request):
    if request.method == 'POST':
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        rf_loaded = load_models('random_forest_model.pkl')
        prediction = rf_loaded.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        predicted_class = prediction[0]

        # Map the predicted class to the corresponding iris species
        iris_species = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
        img_url = {
            'Setosa': 'images/setosa.jpeg',
            'Versicolor': 'images/versicolor.JPG',
            'Virginica': 'images/virginica.jpg'
        }

        predicted_species = iris_species[predicted_class]
        predicted_img = img_url[predicted_species]

        inputData = {
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width
        }

        data = {
            'predicted_species': predicted_species,
            'predicted_img': predicted_img,
            'input_data': inputData,
            'algorithm': 'Random Forest',
            'form_url': reverse('algosAi:rf_iris_exemple_tester'),
            'details_url': reverse('algosAi:rf_iris')
        }

        # Render the unified results template with the prediction
        return render(request, 'includes/unified_iris_results.html', data)

    # If the request method is not POST, render the form again
    return render(request, 'includes/unified_iris_form.html', {
        'algorithm': 'Random Forest',
        'algorithm_info': 'Utilise 100 arbres de décision pour une classification robuste et précise.',
        'action_url': reverse('algosAi:rf_iris_prediction_results')
    })

def rf_regression(request):
    """
    Render the random forest regression example page.
    """
    return render(request, 'includes/rf_regression.html')

def rf_housing_exemple_tester(request):
    """
    Render the California housing form page using unified template.
    """
    context = {
        'algorithm': 'Random Forest',
        'algorithm_info': 'Le revenu médian est le facteur le plus important (59.7% d\'importance) parmi 100 arbres.',
        'action_url': reverse('algosAi:rf_housing_prediction_results')
    }
    return render(request, 'includes/unified_housing_form.html', context)

def rf_housing_prediction_results(request):
    if request.method == 'POST':
        med_inc = float(request.POST.get('med_inc'))
        house_age = float(request.POST.get('house_age'))
        ave_rooms = float(request.POST.get('ave_rooms'))
        ave_bedrms = float(request.POST.get('ave_bedrms'))
        population = float(request.POST.get('population'))
        ave_occup = float(request.POST.get('ave_occup'))
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))

        rf_loaded = load_models('california_housing_rf_model.pkl')
        prediction = rf_loaded.predict([[med_inc, house_age, ave_rooms, ave_bedrms, 
                                       population, ave_occup, latitude, longitude]])

        predicted_price = round(prediction[0] * 100000, 2)  # Convert to dollars

        inputData = {
            'med_inc': med_inc,
            'house_age': house_age,
            'ave_rooms': ave_rooms,
            'ave_bedrms': ave_bedrms,
            'population': population,
            'ave_occup': ave_occup,
            'latitude': latitude,
            'longitude': longitude
        }

        data = {
            'predicted_price': predicted_price,
            'input_data': inputData,
            'algorithm': 'Random Forest',
            'form_url': reverse('algosAi:rf_housing_exemple_tester'),
            'details_url': reverse('algosAi:rf_regression')
        }

        # Render the unified results template with the prediction
        return render(request, 'includes/unified_housing_results.html', data)

    # If the request method is not POST, render the form again
    return render(request, 'includes/unified_housing_form.html', {
        'algorithm': 'Random Forest',
        'algorithm_info': 'Le revenu médian est le facteur le plus important (59.7% d\'importance) parmi 100 arbres.',
        'action_url': reverse('algosAi:rf_housing_prediction_results')
    })

# Decision Tree Views
def dt_details(request):
    """
    Render the decision tree details page.
    """
    return render(request, 'includes/dt_details.html')

def dt_iris(request):
    """
    Render the decision tree classification example page.
    """
    return render(request, 'includes/dt_iris.html')

def dt_regression(request):
    """
    Render the decision tree regression example page.
    """
    return render(request, 'includes/dt_regression.html')

def dt_iris_exemple_tester(request):
    """
    Render the decision tree iris example tester page using unified template.
    """
    context = {
        'algorithm': 'Decision Tree',
        'algorithm_info': 'D\'après le modèle, seules les dimensions des pétales sont vraiment importantes pour la classification !',
        'action_url': reverse('algosAi:dt_iris_prediction_results')
    }
    return render(request, 'includes/unified_iris_form.html', context)

def dt_iris_prediction_results(request):
    if request.method == 'POST':
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        dt_loaded = load_models('decision_tree_iris_model.pkl')
        prediction = dt_loaded.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        predicted_class = prediction[0]

        # Map the predicted class to the corresponding iris species
        iris_species = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
        img_url = {
            'Setosa': 'images/setosa.jpeg',
            'Versicolor': 'images/versicolor.JPG',
            'Virginica': 'images/virginica.jpg'
        }

        predicted_species = iris_species[predicted_class]
        predicted_img = img_url[predicted_species]

        inputData = {
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width
        }

        data = {
            'predicted_species': predicted_species,
            'predicted_img': predicted_img,
            'input_data': inputData,
            'algorithm': 'Decision Tree',
            'form_url': reverse('algosAi:dt_iris_exemple_tester'),
            'details_url': reverse('algosAi:dt_iris')
        }

        # Render the unified results template with the prediction
        return render(request, 'includes/unified_iris_results.html', data)

    # If the request method is not POST, render the form again
    return render(request, 'includes/unified_iris_form.html', {
        'algorithm': 'Decision Tree',
        'algorithm_info': 'D\'après le modèle, seules les dimensions des pétales sont vraiment importantes pour la classification !',
        'action_url': reverse('algosAi:dt_iris_prediction_results')
    })

def dt_housing_exemple_tester(request):
    """
    Render the decision tree California housing form page using unified template.
    """
    context = {
        'algorithm': 'Decision Tree',
        'algorithm_info': 'Le revenu médian (MedInc) est le facteur le plus important (61.8% d\'importance) !',
        'action_url': reverse('algosAi:dt_housing_prediction_results')
    }
    return render(request, 'includes/unified_housing_form.html', context)

def dt_housing_prediction_results(request):
    if request.method == 'POST':
        med_inc = float(request.POST.get('med_inc'))
        house_age = float(request.POST.get('house_age'))
        ave_rooms = float(request.POST.get('ave_rooms'))
        ave_bedrms = float(request.POST.get('ave_bedrms'))
        population = float(request.POST.get('population'))
        ave_occup = float(request.POST.get('ave_occup'))
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))

        dt_loaded = load_models('decision_tree_housing_model.pkl')
        prediction = dt_loaded.predict([[med_inc, house_age, ave_rooms, ave_bedrms, 
                                       population, ave_occup, latitude, longitude]])

        predicted_price = round(prediction[0] * 100000, 2)  # Convert to dollars

        inputData = {
            'med_inc': med_inc,
            'house_age': house_age,
            'ave_rooms': ave_rooms,
            'ave_bedrms': ave_bedrms,
            'population': population,
            'ave_occup': ave_occup,
            'latitude': latitude,
            'longitude': longitude
        }

        data = {
            'predicted_price': predicted_price,
            'input_data': inputData,
            'algorithm': 'Decision Tree',
            'form_url': reverse('algosAi:dt_housing_exemple_tester'),
            'details_url': reverse('algosAi:dt_regression')
        }

        # Render the unified results template with the prediction
        return render(request, 'includes/unified_housing_results.html', data)

    # If the request method is not POST, render the form again
    return render(request, 'includes/unified_housing_form.html', {
        'algorithm': 'Decision Tree',
        'algorithm_info': 'Le revenu médian (MedInc) est le facteur le plus important (61.8% d\'importance) !',
        'action_url': reverse('algosAi:dt_housing_prediction_results')
    })

# AdaBoost Views
def adaboost_details(request):
    """
    Render the AdaBoost details page.
    """
    return render(request, 'includes/adaboost_details.html')

def adaboost_iris(request):
    """
    Render the AdaBoost iris classification example page.
    """
    return render(request, 'includes/adaboost_iris.html')

def adaboost_iris_exemple_tester(request):
    """
    Render the AdaBoost iris example tester page using unified template.
    """
    context = {
        'algorithm': 'AdaBoost',
        'algorithm_info': 'Combine 200 arbres de décision faibles qui s\'adaptent aux échantillons difficiles.',
        'action_url': reverse('algosAi:adaboost_iris_prediction_results')
    }
    return render(request, 'includes/unified_iris_form.html', context)

def adaboost_iris_prediction_results(request):
    if request.method == 'POST':
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        adaboost_loaded = load_models('adaboost_iris_model.pkl')
        prediction = adaboost_loaded.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        predicted_class = prediction[0]

        # Map the predicted class to the corresponding iris species
        iris_species = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
        img_url = {
            'Setosa': 'images/setosa.jpeg',
            'Versicolor': 'images/versicolor.JPG',
            'Virginica': 'images/virginica.jpg'
        }

        predicted_species = iris_species[predicted_class]
        predicted_img = img_url[predicted_species]

        inputData = {
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width
        }

        return render(request, 'includes/unified_iris_results.html', {
            'algorithm': 'AdaBoost',
            'algorithm_description': 'AdaBoost (Adaptive Boosting) combine plusieurs arbres de décision faibles pour créer un classificateur robuste qui s\'améliore progressivement.',
            'predicted_species': predicted_species,
            'predicted_img': predicted_img,
            'inputData': inputData,
            'algorithm_info': 'L\'algorithme se concentre sur les échantillons difficiles à chaque itération.'
        })

def adaboost_regression(request):
    """
    Render the AdaBoost California Housing regression example page.
    """
    return render(request, 'includes/adaboost_regression.html')

def adaboost_housing_exemple_tester(request):
    """
    Render the AdaBoost housing example tester page using unified template.
    """
    context = {
        'algorithm': 'AdaBoost',
        'algorithm_info': 'Combine des arbres de régression faibles qui s\'adaptent aux erreurs de prédiction.',
        'action_url': reverse('algosAi:adaboost_housing_prediction_results')
    }
    return render(request, 'includes/unified_housing_form.html', context)

def adaboost_housing_prediction_results(request):
    if request.method == 'POST':
        med_inc = float(request.POST.get('med_inc'))
        house_age = float(request.POST.get('house_age'))
        ave_rooms = float(request.POST.get('ave_rooms'))
        ave_bedrms = float(request.POST.get('ave_bedrms'))
        population = float(request.POST.get('population'))
        ave_occup = float(request.POST.get('ave_occup'))
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))

        adaboost_loaded = load_models('adaboost_housing_model.pkl')
        prediction = adaboost_loaded.predict([[med_inc, house_age, ave_rooms, ave_bedrms, 
                                             population, ave_occup, latitude, longitude]])

        predicted_price = round(prediction[0] * 100000, 2)  # Convert to dollars

        inputData = {
            'med_inc': med_inc,
            'house_age': house_age,
            'ave_rooms': ave_rooms,
            'ave_bedrms': ave_bedrms,
            'population': population,
            'ave_occup': ave_occup,
            'latitude': latitude,
            'longitude': longitude
        }

        return render(request, 'includes/unified_housing_results.html', {
            'algorithm': 'AdaBoost',
            'algorithm_description': 'AdaBoost (Adaptive Boosting) combine des arbres de régression faibles qui s\'améliorent progressivement en se concentrant sur les prédictions difficiles.',
            'predicted_price': predicted_price,
            'input_data': inputData,
            'algorithm_info': 'R² Score: 0.513 - Performances améliorées avec 200 estimateurs.'
        })

def load_models(name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_dir, 'models_ai')
    model_path = os.path.join(models_dir, name)

    ml_model = None
    ml_model = joblib.load(model_path)
    return ml_model