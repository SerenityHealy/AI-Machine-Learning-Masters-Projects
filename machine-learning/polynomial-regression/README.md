# Polynomial Regression - Salary Prediction

A polynomial regression model for predicting salary based on years of experience with configurable degree and comprehensive evaluation metrics.

## Overview

This project implements polynomial regression to model the non-linear relationship between years of experience and salary. It includes model evaluation, visualization, and flexible command-line configuration.

## Features

- **Configurable Polynomial Degree**: Test different polynomial degrees (2, 3, etc.)
- **Model Evaluation**: R² score and Mean Absolute Error (MAE)
- **Visualization**: Scatter plot with fitted polynomial curve
- **Command-line Interface**: Flexible parameter configuration
- **Example Predictions**: Shows predictions for various experience levels
- **Data Splitting**: Train/test split for unbiased evaluation

## Installation

```bash
# Install required packages
pip install pandas numpy scikit-learn matplotlib
```

## Dataset

Requires a CSV file with two columns:
- `YearsExperience`: Years of professional experience
- `Salary`: Annual salary

Example `Salary_Data.csv`:
```csv
YearsExperience,Salary
1.1,39343
1.3,46205
1.5,37731
2.0,43525
...
```

## Usage

### Basic Usage

```bash
# Run with default parameters (degree=2, test_size=0.2)
python poly_salary.py --data Salary_Data.csv
```

### Advanced Configuration

```bash
# Use degree-3 polynomial
python poly_salary.py --data Salary_Data.csv --degree 3

# Custom test size and random seed
python poly_salary.py --data Salary_Data.csv --degree 2 --test_size 0.3 --random_state 42

# Skip plotting
python poly_salary.py --data Salary_Data.csv --no_plot
```

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--data` | `Salary_Data.csv` | Path to CSV file |
| `--degree` | `2` | Polynomial degree |
| `--test_size` | `0.2` | Test split proportion |
| `--random_state` | `42` | Random seed for reproducibility |
| `--no_plot` | `False` | Skip visualization |

## Output

### Console Output
```
Polynomial degree: 2
R^2: 0.9569
MAE: 4380.25
Predicted salary for 1.0 years: 38496.50
Predicted salary for 3.0 years: 54789.23
Predicted salary for 5.0 years: 79234.67
Predicted salary for 10.0 years: 121567.89
```

### Visualization
Generates `salary_poly_fit.png`:
- Scatter plot of actual data points
- Smooth polynomial curve fit
- Labeled axes and legend

## How It Works

1. **Load Data**: Reads CSV and validates required columns
2. **Feature Engineering**: Creates polynomial features up to specified degree
3. **Train/Test Split**: Splits data for unbiased evaluation
4. **Pipeline**: StandardScaler → PolynomialFeatures → LinearRegression
5. **Evaluation**: Computes R² and MAE on test set
6. **Prediction**: Shows examples and generates visualization

## Model Details

**Algorithm**: Polynomial Regression
- Transforms features: x → [x, x², x³, ...]
- Fits linear model on polynomial features
- Degree controls model complexity

**Pipeline Steps**:
1. PolynomialFeatures: Generates polynomial and interaction features
2. LinearRegression: Fits linear model to transformed features

## Evaluation Metrics

### R² (Coefficient of Determination)
- Measures proportion of variance explained
- Range: 0 to 1 (higher is better)
- Typical value: 0.95+ for salary data

### MAE (Mean Absolute Error)
- Average absolute prediction error
- Same units as target (dollars)
- Lower is better

## Choosing Polynomial Degree

- **Degree 1**: Linear regression (may underfit)
- **Degree 2**: Captures quadratic relationships (common choice)
- **Degree 3+**: More complex curves (risk of overfitting)

Test different degrees and compare R² and MAE on the test set.

## Technical Details

**Language**: Python 3
**Key Libraries**:
- pandas: Data loading
- numpy: Numerical operations
- scikit-learn: ML pipeline and regression
- matplotlib: Visualization

## Learning Outcomes

- Polynomial feature engineering
- Non-linear regression modeling
- Model evaluation with R² and MAE
- Train/test split methodology
- scikit-learn pipelines
- Command-line argument parsing
- Data visualization with matplotlib
