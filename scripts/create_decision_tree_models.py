import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.datasets import load_iris, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score
import joblib
import os

def create_decision_tree_iris_model():
    """
    Create and save a Decision Tree classification model for Iris dataset.
    """
    print("Creating Decision Tree model for Iris classification...")
    
    # Load the Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names
    
    print(f"Dataset shape: {X.shape}")
    print(f"Features: {feature_names}")
    print(f"Target classes: {target_names}")
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print("\nTraining Decision Tree Classifier...")
    
    # Create and train the Decision Tree model
    dt_classifier = DecisionTreeClassifier(
        max_depth=5,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42
    )
    
    dt_classifier.fit(X_train, y_train)
    
    # Make predictions
    y_pred = dt_classifier.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nModel Performance:")
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=target_names))
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': feature_names,
        'importance': dt_classifier.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\nFeature Importance:")
    print(feature_importance)
    
    # Save the model
    models_dir = 'models_ai'
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
    
    model_path = os.path.join(models_dir, 'decision_tree_iris_model.pkl')
    joblib.dump(dt_classifier, model_path)
    
    # Save model info
    model_info = {
        'model_type': 'DecisionTreeClassifier',
        'features': list(feature_names),
        'target_names': list(target_names),
        'max_depth': 5,
        'accuracy': accuracy,
        'feature_importance': feature_importance.to_dict('records')
    }
    
    info_path = os.path.join(models_dir, 'decision_tree_iris_model_info.pkl')
    joblib.dump(model_info, info_path)
    
    print(f"\nModel saved to: {model_path}")
    print(f"Model info saved to: {info_path}")
    
    return dt_classifier, model_info

def create_decision_tree_housing_model():
    """
    Create and save a Decision Tree regression model for California housing prices.
    """
    print("\n" + "="*60)
    print("Creating Decision Tree model for California Housing regression...")
    
    # Load the California housing dataset
    california_housing = fetch_california_housing()
    X = california_housing.data
    y = california_housing.target
    feature_names = california_housing.feature_names
    
    print(f"Dataset shape: {X.shape}")
    print(f"Features: {feature_names}")
    print(f"Target variable: House value in hundreds of thousands of dollars")
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print("\nTraining Decision Tree Regressor...")
    
    # Create and train the Decision Tree model
    dt_regressor = DecisionTreeRegressor(
        max_depth=10,
        min_samples_split=10,
        min_samples_leaf=5,
        random_state=42
    )
    
    dt_regressor.fit(X_train, y_train)
    
    # Make predictions
    y_pred = dt_regressor.predict(X_test)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    print(f"\nModel Performance:")
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"Root Mean Squared Error: {rmse:.4f}")
    print(f"R² Score: {r2:.4f}")
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': feature_names,
        'importance': dt_regressor.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\nFeature Importance:")
    print(feature_importance)
    
    # Save the model
    model_path = os.path.join('models_ai', 'decision_tree_housing_model.pkl')
    joblib.dump(dt_regressor, model_path)
    
    # Save model info
    model_info = {
        'model_type': 'DecisionTreeRegressor',
        'features': list(feature_names),
        'max_depth': 10,
        'mse': mse,
        'rmse': rmse,
        'r2_score': r2,
        'feature_importance': feature_importance.to_dict('records')
    }
    
    info_path = os.path.join('models_ai', 'decision_tree_housing_model_info.pkl')
    joblib.dump(model_info, info_path)
    
    print(f"\nModel saved to: {model_path}")
    print(f"Model info saved to: {info_path}")
    
    return dt_regressor, model_info

if __name__ == "__main__":
    # Create both models
    iris_model, iris_info = create_decision_tree_iris_model()
    housing_model, housing_info = create_decision_tree_housing_model()
    
    print("\n" + "="*60)
    print("Decision Tree models created successfully!")
    print("- Iris Classification Model: Accuracy = {:.2f}%".format(iris_info['accuracy'] * 100))
    print("- Housing Regression Model: R² = {:.4f}".format(housing_info['r2_score']))
