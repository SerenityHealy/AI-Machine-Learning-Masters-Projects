# Naive Bayes Classifier

A custom implementation of a Gaussian Naive Bayes classifier for iris flower species classification.

## Overview

This project implements a Naive Bayes classifier from scratch, demonstrating the underlying mathematics and probability theory behind the algorithm. The implementation is validated against scikit-learn's GaussianNB classifier.

## Features

- **Custom Implementation**: Built from scratch using NumPy for educational purposes
- **Gaussian Distribution**: Uses normal distribution for continuous features
- **Laplace Smoothing**: Implements smoothing to handle zero probabilities
- **Comparison**: Validates against scikit-learn's implementation
- **Detailed Metrics**: Provides accuracy scores and probability distributions

## How It Works

The classifier:
1. Calculates prior probabilities for each class
2. Computes mean and standard deviation for each feature per class
3. Uses Gaussian probability density function for likelihood calculation
4. Applies Bayes' theorem to compute posterior probabilities
5. Predicts the class with highest probability

## Installation

```bash
# Install required packages
pip install numpy pandas scikit-learn
```

## Usage

```bash
# Run the classifier
python naive_bayes_classifier.py
```

The program will:
- Load the Iris dataset
- Split into training (70%) and testing (30%) sets
- Train the custom classifier
- Compare against scikit-learn's implementation
- Display detailed results and accuracy metrics

## Dataset

Uses the famous Iris dataset with 4 features:
- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

Classifies into 3 species:
- Setosa
- Versicolor
- Virginica

## Output

The program displays:
- Data frequency matrix for each class
- Probability parameters (mean and std dev)
- Prior probabilities for each class
- Sample predictions with confidence scores
- Accuracy comparison between custom and scikit-learn models

## Technical Details

**Algorithm**: Gaussian Naive Bayes
**Language**: Python 3
**Key Libraries**: NumPy, Pandas, scikit-learn
**Dataset Size**: 150 samples
**Features**: 4 continuous numerical features
**Classes**: 3 species

## Learning Outcomes

- Understanding Bayes' theorem application
- Implementing probability density functions
- Handling numerical stability with smoothing
- Model validation and comparison
