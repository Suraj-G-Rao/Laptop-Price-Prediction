# Laptop Price Prediction

This project is designed to predict laptop prices based on various specifications using machine learning models.

## Table of Contents
1. [Data Preprocessing and Exploration](#data-preprocessing-and-exploration)
2. [Model Training and Evaluation](#model-training-and-evaluation)
3. [Model Deployment](#model-deployment)
4. [Running the Application](#running-the-application)

## Data Preprocessing and Exploration

### Data Collection
- The dataset consists of laptop specifications and their corresponding prices.

### Exploratory Data Analysis (EDA)
- Performed EDA to understand data distribution and relationships between features.
- Identified key features that significantly influence laptop prices.

### Feature Engineering
- Created additional features such as pixels per inch (PPI) and binary indicators for touchscreen and IPS display.

## Model Training and Evaluation

### Data Splitting
- The data was split into training and testing sets using an 85-15 ratio.

### Model Selection
- Implemented several machine learning models including:
  - Linear Regression
  - Lasso
  - Ridge
  - K-Nearest Neighbors
  - Decision Tree
  - Support Vector Regressor (SVR)
  - Random Forest
  - AdaBoost
  - Gradient Boosting
  - XGBoost

### Pipeline Creation
- Built a pipeline with `ColumnTransformer` and `OneHotEncoder` for categorical feature handling.
- Integrated the selected machine learning models into the pipeline.

### Evaluation Metrics
- Evaluated model performance using:
  - R² Score
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
- The Gradient Boosting Regressor provided the best performance.

## Model Deployment

### Model Saving
- Serialized the trained Gradient Boosting model pipeline using `pickle` for deployment.

### Web Application Development
- Developed a Streamlit-based web application to allow users to input laptop specifications and get price predictions.

### User Interface
- Implemented dropdowns and input fields for specifications like brand, processor, RAM, GPU, and more.

## Running the Application

### Streamlit App
- The app predicts laptop prices based on user inputs and provides real-time predictions.

### Deployment
- The application can be deployed on cloud platforms or run locally for serving predictions.
