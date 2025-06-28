from django.urls import path
from . import views

app_name = 'algosAi'

urlpatterns = [
    path('', views.index, name='index'),
    path('rf_details/', views.rf_details, name='rf_details'),
    path('rf_iris/', views.rf_iris, name='rf_iris'),
    path('rf_regression/', views.rf_regression, name='rf_regression'),

    path('rf_iris_test/', views.rf_iris_exemple_tester, name='rf_iris_exemple_tester'),
    path('rf_iris_prediction_results/', views.rf_iris_prediction_results, name='rf_iris_prediction_results'),
    
    path('rf_housing_test/', views.rf_housing_exemple_tester, name='rf_housing_exemple_tester'),
    path('rf_housing_prediction_results/', views.rf_housing_prediction_results, name='rf_housing_prediction_results'),
    
    # Decision Tree routes
    path('dt_details/', views.dt_details, name='dt_details'),
    path('dt_iris/', views.dt_iris, name='dt_iris'),
    path('dt_regression/', views.dt_regression, name='dt_regression'),
    
    path('dt_iris_test/', views.dt_iris_exemple_tester, name='dt_iris_exemple_tester'),
    path('dt_iris_prediction_results/', views.dt_iris_prediction_results, name='dt_iris_prediction_results'),
    
    path('dt_housing_test/', views.dt_housing_exemple_tester, name='dt_housing_exemple_tester'),
    path('dt_housing_prediction_results/', views.dt_housing_prediction_results, name='dt_housing_prediction_results'),

    # AdaBoost routes
    path('adaboost_details/', views.adaboost_details, name='adaboost_details'),
    path('adaboost_iris/', views.adaboost_iris, name='adaboost_iris'),
    path('adaboost_regression/', views.adaboost_regression, name='adaboost_regression'),
    
    path('adaboost_iris_test/', views.adaboost_iris_exemple_tester, name='adaboost_iris_exemple_tester'),
    path('adaboost_iris_prediction_results/', views.adaboost_iris_prediction_results, name='adaboost_iris_prediction_results'),
    
    path('adaboost_housing_test/', views.adaboost_housing_exemple_tester, name='adaboost_housing_exemple_tester'),
    path('adaboost_housing_prediction_results/', views.adaboost_housing_prediction_results, name='adaboost_housing_prediction_results'),
]