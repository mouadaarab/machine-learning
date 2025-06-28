import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

def create_california_housing_model():
    """
    Create and save a Random Forest regression model for California housing prices.
    """
    print("Loading California Housing dataset...")
    
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
    
    print("\nTraining Random Forest Regressor...")
    
    # Create and train the Random Forest model
    rf_regressor = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2
    )
    
    rf_regressor.fit(X_train, y_train)
    
    # Make predictions
    y_pred = rf_regressor.predict(X_test)
    
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
        'importance': rf_regressor.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\nFeature Importance:")
    print(feature_importance)
    
    # Save the model
    models_dir = 'models_ai'
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
    
    model_path = os.path.join(models_dir, 'california_housing_rf_model.pkl')
    joblib.dump(rf_regressor, model_path)
    
    # Save model info
    model_info = {
        'model_type': 'RandomForestRegressor',
        'features': list(feature_names),
        'n_estimators': 100,
        'max_depth': 10,
        'mse': mse,
        'rmse': rmse,
        'r2_score': r2,
        'feature_importance': feature_importance.to_dict('records')
    }
    
    info_path = os.path.join(models_dir, 'california_housing_rf_model_info.pkl')
    joblib.dump(model_info, info_path)
    
    print(f"\nModel saved to: {model_path}")
    print(f"Model info saved to: {info_path}")
    
    return rf_regressor, model_info

if __name__ == "__main__":
    model, info = create_california_housing_model()
    print("\nCalifornia Housing Random Forest model created successfully!")
