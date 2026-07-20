# 🌦️ Intelligent Weather Prediction Pipeline

An end-to-end **Time Series Forecasting** project that predicts future weather conditions in **Delhi, India** using historical hourly weather observations. The project follows the complete data science lifecycle, from data collection to model deployment, combining statistical forecasting methods with modern machine learning models.

---

## 📌 Project Overview

This project forecasts multiple weather variables including:

- Temperature
- Relative Humidity
- Rainfall
- Soil Temperature
- Wind Speed
- Surface Pressure
- Mean Sea Level Pressure

The pipeline includes:

- Data Collection
- Data Cleaning & Validation
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Statistical Modeling
- Machine Learning Modeling
- Model Evaluation
- SHAP Explainability

---

# 📂 Project Structure

```text
Intelligent-Weather-Prediction-Pipeline/
│
├── data/
│   ├── raw/                          # Original weather dataset
│   ├── interim/                      # Intermediate datasets
│   └── processed/                    # Cleaned datasets ready for modeling
│
├── models/
│   └── model_summaries/              # Saved model summaries, evaluation reports, and trained models(pkl files)
│
├── notebooks/
│   ├── Data Collection & Inspection.ipynb
│   ├── Data Cleaning & Validation.ipynb
│   ├── EDA & Feature Engineering.ipynb
│   ├── ARIMA & SARIMA.ipynb
│   └── Modeling.ipynb
│
├── references/
│   ├── Data Dictionary.pdf
│   └── Project Instruction.pdf
│
├── reports/
│   ├── figures/                      # Generated plots and visualizations
│   ├── Sweetviz_Report.html          # Automated EDA report
│   └── Project_Report.pdf            # Final project report
│
├── src/
│   ├── data/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   └── logs/
│   │
│   ├── features/
│   │   └── make_features.py
│   │
│   └── models/
│       ├── train_models.py
│       ├── fine_tune_models.py
│       └── predict_models.py
│
├── setup.py                          # Project package configuration
└── README.md                         # Project documentation
```

---

# 🌍 Data Source

The dataset was collected from the **Open-Meteo Historical Weather API**.

### Dataset Information

| Attribute | Details |
|------------|----------|
| Source | Open-Meteo Historical Weather API |
| Location | Delhi, India |
| Time Period | January 2020 – December 2025 |
| Frequency | Hourly |
| Records | 52,608 observations |
| Features | 8 Weather Variables |

### Original Variables

- Temperature (2 m)
- Relative Humidity (2 m)
- Rainfall
- Soil Temperature
- Wind Speed
- Surface Pressure
- Mean Sea Level Pressure
- Is Day

---

# 🧹 Data Preprocessing

The preprocessing pipeline includes:

- Datetime conversion
- Feature renaming
- Duplicate record checking
- Missing value analysis
- Data type validation
- Chronological ordering verification
- Dataset consistency validation

The dataset contained:

- ✅ No missing values
- ✅ No duplicate records
- ✅ Correct chronological order

---

# 📊 Exploratory Data Analysis

EDA was performed to understand:

- Seasonal weather patterns
- Temperature trends
- Rainfall distribution
- Correlation among weather variables
- Time-based variations
- Weekly and monthly temperature analysis

Visualization techniques included:

- Histograms
- Boxplots
- Heatmaps
- Line plots
- Seasonal decomposition
- Correlation analysis

---

# ⚙️ Feature Engineering Approach

To improve forecasting accuracy, additional temporal and statistical features were created.

## Rolling Statistics

Rolling Mean

- Temperature
- Relative Humidity
- Rain
- Soil Temperature
- Wind Speed
- Surface Pressure
- Pressure MSL

Rolling Standard Deviation

- Temperature
- Relative Humidity
- Rain
- Soil Temperature
- Wind Speed
- Surface Pressure
- Pressure MSL

---

## Calendar Features

- Day of Year
- Day of Week
- Day of Month
- Month
- Quarter
- Weekend Indicator

---

## Cyclical Encoding

To preserve periodicity of seasonal patterns:

- Sine(Day of Year)
- Cosine(Day of Year)

These transformations allow machine learning models to understand cyclic time relationships without discontinuities.

---

# 🤖 Models Implemented

The project compares both statistical and machine learning forecasting techniques.

## Statistical Models

### ARIMA

Used for univariate time series forecasting by modeling autoregressive and moving average components.

**Why ARIMA?**

- Simple baseline model
- Effective for stationary data
- Interpretable forecasting approach

---

### SARIMA

Extends ARIMA by incorporating seasonal components.

**Why SARIMA?**

- Captures seasonal weather behavior
- Handles repeating temporal patterns
- Suitable for periodic temperature forecasting

---

### VAR (Vector AutoRegression)

Models multiple weather variables simultaneously.

**Why VAR?**

- Captures relationships among weather variables
- Uses multivariate dependencies
- Suitable for interconnected meteorological variables

---

## Machine Learning Models

### XGBoost Regressor

Gradient boosting algorithm.

**Why XGBoost?**

- High predictive accuracy
- Handles complex nonlinear patterns
- Excellent performance on tabular data
- Built-in regularization
- Efficient training

XGBoost achieved the best overall forecasting performance in this project.

---

# 📈 Model Evaluation

Models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)
- R² Score

These metrics provide a comprehensive comparison of forecasting accuracy.

---

# 🔍 Model Explainability

SHAP (SHapley Additive exPlanations) was used to interpret the machine learning model.

SHAP analysis provides:

- Global feature importance
- Individual prediction explanations
- Feature contribution visualization

This improves transparency and interpretability of the forecasting model.

---

# 🚫 Preventing Data Leakage

Several measures were taken to ensure reliable model evaluation.

### Time-Based Train-Test Split

Instead of randomly shuffling observations, the dataset was split chronologically.

- Training Data → Historical observations
- Testing Data → Future observations

This mimics real-world forecasting where future data is unavailable during training.

---

### Feature Engineering Using Past Information Only

Rolling statistics were computed using only historical observations.

No future values were included while creating features.

---

### No Target Leakage

The target variable was excluded from predictor variables during training.

No future weather observations were used as model inputs.

---

### Chronological Validation

All preprocessing and forecasting steps preserved temporal ordering to prevent information leakage across time.

---

# 🚀 Installation

```bash
git clone [https://github.com/yourusername/Intelligent-Weather-Prediction-Pipeline.git](https://github.com/KishoreAIML/Time-Series-Forcasting-Project-Intelligent-Weather-Prediction-Pipeline.git)

cd Intelligent-Weather-Prediction-Pipeline

pip install -r requirements.txt
```

---

# ▶️ Usage

Run notebooks in the following order:

1. Data Collection & Inspection
2. Data Cleaning & Validation
3. EDA & Feature Engineering
4. ARIMA & SARIMA
5. Modeling

---

# 📌 Key Highlights

- End-to-End Forecasting Pipeline
- Automated Data Validation
- Feature Engineering
- Statistical Forecasting
- Machine Learning Forecasting
- SHAP Explainability
- Modular Python Package Structure
- Reproducible Workflow

---

# 🔮 Future Improvements

- LSTM Forecasting
- GRU Networks
- Transformer-based Time Series Models
- Hyperparameter Optimization using Optuna
- MLflow Experiment Tracking
- Docker Deployment
- Real-time Weather Forecast API
- Streamlit Dashboard

---

# 📚 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Statsmodels
- SHAP
- Sweetviz
- Missingno

---

# 👨‍💻 Author

**Kishore Tirumani**

Data Science Intern

Khizex Software Solutions

---

## ⭐ If you found this project useful, consider giving it a star.

---

---

# 🏠 Project 2 — Lahore Real Estate Price Prediction Pipeline

## 📌 Project Overview

The **Lahore Real Estate Price Prediction Pipeline** is an end-to-end Machine Learning project that predicts residential property prices in **Lahore, Pakistan** using structured real estate listing data. The project follows a complete data science workflow—from data preprocessing to model deployment—while emphasizing feature engineering, hyperparameter optimization, model explainability, and prediction uncertainty.

The pipeline includes:

- Data Collection & Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Feature Encoding
- Model Training
- Hyperparameter Optimization
- Cross Validation
- Model Evaluation
- Prediction Interval Estimation
- SHAP Explainability
- Permutation Feature Importance

---

## 📂 Project Structure

```text
Lahore_Real_Estate_Price_Prediction_Pipeline/
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── models/
│   ├── trained_models/
│   ├── encoders/
│   ├── prediction_intervals/
│   └── trial_logs/
│
├── notebooks/
│   ├── Data Cleaning & Validation.ipynb
│   ├── Exploratory Data Analysis.ipynb
│   ├── Feature Engineering.ipynb
│   ├── Modeling.ipynb
│   └── Model Explainability.ipynb
│
├── references/
│
├── reports/
│   ├── figures/
│   ├── trial_logs/
│   └── model_reports/
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── visualization/
│   └── utils/
│
├── config.yaml
├── setup.py
└── README.md
```

---

# 🏘️ Dataset Information

| Attribute | Details |
|------------|----------|
| Domain | Real Estate |
| Location | Lahore, Pakistan |
| Problem Type | Regression |
| Target Variable | Property Price (PKR) |
| Final Dataset | 17,729 Residential Properties |

### Features

- Property Type
- Property Purpose
- Location
- Area
- Bedrooms
- Bathrooms
- Kitchens
- Store Rooms
- Servant Quarters
- Furnished Status
- Gym
- Study Room
- Drawing Room
- Dining Room
- Lawn & Garden
- Swimming Pool
- Electricity Backup
- Lounge / Sitting Room

---

# 🧹 Data Preprocessing

The preprocessing pipeline includes:

- Missing value analysis
- Duplicate removal
- Data type validation
- Area unit conversion to Square Feet
- Price conversion to Pakistani Rupees (PKR)
- Boolean feature normalization
- Location normalization
- Outlier detection and removal

---

# 📊 Exploratory Data Analysis

EDA was performed to understand:

- Property price distribution
- Area distribution
- Bedroom & bathroom distribution
- Property amenities
- Location analysis
- Correlation between variables
- Outlier analysis
- Feature relationships

Visualization techniques include:

- Histograms
- Count Plots
- Box Plots
- Scatter Plots
- Pair Plots
- Correlation Heatmaps

---

# ⚙️ Feature Engineering

Several domain-specific features were engineered to improve prediction performance.

### Engineered Features

- Area (Square Feet)
- Price (PKR)
- Bedroom-to-Bathroom Ratio
- Log Area Transformation
- Price Per Square Foot
- Normalized Location

### Feature Encoding

- **Target Encoding** for Location
- **One-Hot Encoding** for Property Type and Purpose

---

# 🤖 Machine Learning Models

The project compares multiple ensemble regression algorithms.

## Random Forest Regressor

- Handles nonlinear relationships
- Robust against overfitting
- Provides feature importance
- Excellent predictive performance

## LightGBM Regressor

- Fast gradient boosting framework
- Efficient for large datasets
- High predictive accuracy
- Faster training

---

# 🔧 Hyperparameter Optimization

Model performance was optimized using:

- RandomizedSearchCV
- 5-Fold Cross Validation
- Hyperparameter Search
- Trial Logging

Each hyperparameter trial records:

- RMSE (PKR)
- RMSE (%)
- Training Time
- Validation Score

---

# 📊 Model Performance

The project compares multiple ensemble learning algorithms using several regression evaluation metrics. The final model was selected based on overall prediction accuracy, generalization performance, and inference speed.

| Model | MAE (PKR) | RMSE (PKR) | MAPE (%) | R² Score | Training Time (sec) | Inference Time (sec) | Final Model |
|--------|----------:|-----------:|----------:|---------:|--------------------:|----------------------:|:-----------:|
| **Random Forest Regressor** | **502,182.12** | **2,318,305.00** | **1.126** | **0.998742** | **361.76** | **0.052** | ✅ Yes |
| LightGBM Regressor | 436,625.46 | 2,604,551.00 | 0.765 | 0.998412 | 281.28 | 0.095 | No |

---

## 📈 Model Comparison

<p align="center">
    <img src="reports/figures/model_comparison.png" width="950">
</p>

---

## 🏆 Final Model Selection

Although **LightGBM** achieved slightly lower MAE and MAPE values, the **Random Forest Regressor** demonstrated superior overall performance by achieving:

- ✅ Highest R² Score
- ✅ Lowest RMSE
- ✅ Better prediction stability
- ✅ Faster inference time
- ✅ Better generalization on unseen data

Therefore, the **Random Forest Regressor** was selected as the final production model.

---

# 📈 Model Evaluation

Models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)
- R² Score
- Cross Validation

These metrics provide a comprehensive comparison of prediction accuracy and model robustness.

---

# 🎯 Prediction Intervals

Beyond point predictions, the project estimates **Prediction Intervals** using **MAPIE (Model Agnostic Prediction Interval Estimator)**.

For every prediction, the model returns:

- Predicted Property Price
- Lower Confidence Bound
- Upper Confidence Bound

Prediction intervals provide uncertainty estimates, making the model more reliable for real-world decision making.

---

# 🔍 Model Explainability

To improve model interpretability, the project includes:

## SHAP Explainability

SHAP analysis provides:

- Global Feature Importance
- Local Prediction Explanation
- SHAP Summary Plot

## Permutation Feature Importance

Permutation Importance was used to evaluate the contribution of each feature toward prediction performance.

These techniques help explain how different property attributes influence predicted prices.

---

# 🚫 Preventing Data Leakage

Several measures were taken to ensure reliable model evaluation.

- Train/Test Split performed before encoding
- Target Encoding fitted only on training data
- Saved encoders reused during inference
- Cross Validation performed only on training data
- Test data remained completely unseen during model training

This ensures realistic evaluation and better model generalization.

---

# 🚀 Future Improvements

- XGBoost
- CatBoost
- Stacking Ensemble
- Optuna Hyperparameter Optimization
- MLflow Experiment Tracking
- Streamlit Dashboard
- FastAPI Deployment
- Docker Containerization
- Automated Retraining Pipeline

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Random Forest
- LightGBM
- SHAP
- MAPIE
- Category Encoders
- Joblib
