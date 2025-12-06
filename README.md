# Python School Projects

A collection of Python projects developed during my computer science coursework, focusing on machine learning, computer vision, and algorithm implementation.

## 📚 About

This repository showcases various Python programming projects I've completed as part of my academic studies. The projects demonstrate practical applications of machine learning algorithms, computer vision techniques, and problem-solving with AI search algorithms.

## 🗂️ Project Categories

### Machine Learning

#### 1. Naive Bayes Classifier
Custom implementation of a Naive Bayes classifier for iris flower species classification.
- **Location:** `machine-learning/naive-bayes-classifier/`
- **Features:**
  - Custom Gaussian Naive Bayes implementation from scratch
  - Comparison with scikit-learn's implementation
  - Detailed probability calculations and smoothing techniques
- **Technologies:** NumPy, Pandas, scikit-learn

#### 2. K-Nearest Neighbors (KNN) Iris Classifier
KNN classifier with automatic hyperparameter tuning for iris species prediction.
- **Location:** `machine-learning/knn-iris-classifier/`
- **Features:**
  - Auto-detection of various CSV header formats
  - Grid search for optimal k selection
  - Cross-validation with standardization pipeline
  - Interactive prediction mode
- **Technologies:** scikit-learn, Pandas, NumPy

#### 3. Neural Networks
Custom shallow artificial neural network implementations.
- **Location:** `machine-learning/neural-networks/`
- **Features:**
  - 2-layer neural network built from scratch
  - ReLU activation and backpropagation
  - Arithmetic sequence prediction
  - Training visualization and loss tracking
- **Technologies:** NumPy

#### 4. Polynomial Regression
Salary prediction using polynomial regression.
- **Location:** `machine-learning/polynomial-regression/`
- **Features:**
  - Configurable polynomial degree
  - Model evaluation with R² and MAE metrics
  - Visualization of fitted curves
  - Command-line argument parsing
- **Technologies:** scikit-learn, Pandas, Matplotlib

### Computer Vision

#### 5. Image Augmentation Tool
Batch image augmentation for dataset expansion.
- **Location:** `computer-vision/image-augmentation/`
- **Features:**
  - Multiple augmentation techniques (flip, rotate, brightness, contrast)
  - Folder-wide processing with directory structure preservation
  - Configurable augmentations per image
  - JSON metadata reporting
- **Technologies:** Pillow (PIL)

#### 6. OpenCV Basics
Simple OpenCV image viewer and file operations.
- **Location:** `computer-vision/opencv-basics/`
- **Features:**
  - Image loading and display
  - Automatic file saving
  - Error handling for missing files
- **Technologies:** OpenCV, Python

### Algorithms

#### 7. Elevator Rescue Problem
AI search problem solver using greedy best-first search.
- **Location:** `algorithms/elevator-rescue/`
- **Features:**
  - Greedy search algorithm implementation
  - Interactive motor configuration
  - Heuristic-based pathfinding
  - Dynamic action generation
- **Technologies:** simpleai

## 🚀 Getting Started

### Prerequisites

```bash
# Install Python 3.8 or higher
python --version

# Install common dependencies
pip install numpy pandas scikit-learn matplotlib opencv-python pillow simpleai
```

### Running Individual Projects

Each project directory contains its own README with specific instructions. General usage:

```bash
# Navigate to a specific project
cd machine-learning/knn-iris-classifier

# Run the program
python knn_iris_classifier.py
```

## 📋 Requirements

Common dependencies across projects:
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation
- **scikit-learn** - Machine learning algorithms
- **Matplotlib** - Data visualization
- **OpenCV** - Computer vision
- **Pillow** - Image processing
- **simpleai** - AI search algorithms

## 🎓 Course Information

These projects were developed as part of coursework in:
- **CSC525** - Principles of Machine Learning
- Computer Vision fundamentals
- Algorithm design and analysis

## 📝 License

These projects are for educational purposes.

## 👤 Author

**Serenity Healy**
- GitHub: [@SerenityHealy](https://github.com/SerenityHealy)

## 🤝 Contributing

These are academic projects, but suggestions and feedback are welcome!

## ⭐ Acknowledgments

- Course instructors and teaching assistants
- Open-source libraries and their contributors
- Academic resources and documentation
