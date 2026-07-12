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
