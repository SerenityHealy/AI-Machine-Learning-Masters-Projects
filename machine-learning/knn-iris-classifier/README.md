# K-Nearest Neighbors (KNN) Iris Classifier

An advanced KNN classifier with automatic hyperparameter tuning and flexible CSV format support for iris flower classification.

## Overview

This project implements a K-Nearest Neighbors classifier with intelligent features including automatic k-selection via grid search, data standardization, and robust CSV header detection.

## Features

- **Auto Header Detection**: Recognizes various CSV column naming conventions
- **Grid Search**: Automatically finds optimal k value (tests k=3,5,7,9,11)
- **Cross-Validation**: Uses 5-fold CV for robust evaluation
- **Data Standardization**: Implements preprocessing pipeline with StandardScaler
- **Interactive Mode**: Predict species from user input
- **Command-line Arguments**: Flexible usage with optional parameters

## Installation

```bash
# Install required packages
pip install scikit-learn pandas numpy

# Download Iris.csv dataset
# Place in the same directory as the script
```

## Usage

### Interactive Mode (with prompts)

```bash
python knn_iris_classifier.py
```

The program will prompt you for:
- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)

### Command-line Arguments

```bash
# Provide measurements directly
python knn_iris_classifier.py 5.1 3.5 1.4 0.2

# Show hold-out accuracy
python knn_iris_classifier.py --holdout
```

## Dataset Requirements

The program accepts CSV files with various header formats:
- `SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species`
- `sepal_length, sepal_width, petal_length, petal_width, species`
- `Sepal.Length, Sepal.Width, Petal.Length, Petal.Width, variety`
- No header (auto-adds standard headers)

## How It Works

1. **Data Loading**: Reads CSV and normalizes column names
2. **Preprocessing**: Standardizes features to zero mean and unit variance
3. **Model Selection**: Grid search with 5-fold CV to find optimal k
4. **Training**: Fits final model on all data with best k
5. **Prediction**: Classifies new samples using trained model

## Output Example

```
Selected k=7 via 5-fold CV (mean CV accuracy=0.973)
Predicted species: Iris-setosa
```

## Technical Details

**Algorithm**: K-Nearest Neighbors
**Distance Metric**: Euclidean distance (default)
**Preprocessing**: StandardScaler normalization
**Validation**: 5-fold cross-validation
**Grid Search Range**: k ∈ {3, 5, 7, 9, 11}

## Performance

- **Typical CV Accuracy**: 96-98%
- **Hold-out Test Accuracy**: ~95%
- **Optimal k**: Usually 5-7 for Iris dataset

## Code Structure

- `load_data()`: CSV parsing with flexible header detection
- `build_and_select_k()`: Grid search for hyperparameter tuning
- `train_final_model()`: Final model training
- `parse_inputs()`: Handle user input from args or prompts

## Learning Outcomes

- KNN algorithm implementation
- Hyperparameter optimization with grid search
- Data preprocessing and standardization
- Cross-validation techniques
- Building robust data pipelines
