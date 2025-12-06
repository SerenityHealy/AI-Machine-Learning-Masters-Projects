# AI & Machine Learning Master's Projects

A comprehensive collection of Python projects from my Master's program in AI and Machine Learning, featuring machine learning algorithms, computer vision, data structures, applications, and games.

## 📚 About

This repository showcases Python programming projects completed throughout my Master's program. The projects span multiple areas including machine learning, computer vision, data structures & algorithms, practical applications, game development, and object-oriented programming fundamentals.

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

### Algorithms & AI

#### 7. Elevator Rescue Problem
AI search problem solver using greedy best-first search.
- **Location:** `algorithms/elevator-rescue/`
- **Features:**
  - Greedy search algorithm implementation
  - Interactive motor configuration
  - Heuristic-based pathfinding
  - Dynamic action generation
- **Technologies:** simpleai

### Applications

#### 8. ATM Machine Simulator
Interactive banking system with authentication and transactions.
- **Location:** `applications/atm-machine/`
- **Features:**
  - PIN authentication with attempt limits
  - Withdrawal and deposit operations
  - Balance tracking and validation
  - Error handling and input validation
- **Technologies:** Python

#### 9. Shopping List Application
Comprehensive grocery management system with price comparison.
- **Location:** `applications/shopping-list/`
- **Features:**
  - List creation and management
  - Saved lists with custom names
  - Price comparison across 5 major stores
  - Multi-screen navigation
- **Technologies:** Python

#### 10. Pothole Tracking System
Municipal pothole management and repair tracking system.
- **Location:** `applications/pothole-tracker/`
- **Features:**
  - Multi-actor system (Citizen, System, Repair Crew)
  - Use case documentation
  - Interactive menu interface
  - Workflow demonstration
- **Technologies:** Python

### Data Structures & Algorithms

#### 11. Linear Search Implementation
Grocery search tool demonstrating linear search algorithm.
- **Location:** `data-structures-algorithms/linear-search/`
- **Features:**
  - Linear search from scratch
  - Case-insensitive matching
  - Interactive search interface
  - 54-item grocery database
- **Technologies:** Python

#### 12. Hash Table Implementation
Custom hash table for social media recommendations.
- **Location:** `data-structures-algorithms/hash-table/`
- **Features:**
  - Hash table built from scratch
  - Collision handling via chaining
  - CRUD operations (Insert, Get, Delete)
  - User recommendation storage
- **Technologies:** Python

#### 13. Algorithm Exercises
Collection of algorithm implementation exercises.
- **Location:** `data-structures-algorithms/algorithm-exercises/`
- **Features:**
  - Multiple algorithm modules
  - Problem-solving exercises
  - Code optimization techniques
- **Technologies:** Python

### Games

#### 14. High-Low Card Game
Interactive card guessing game with score tracking.
- **Location:** `games/high-low-card-game/`
- **Features:**
  - 52-card deck simulation
  - Random shuffling
  - Score tracking
  - Face card display
- **Technologies:** Python

### Foundations

#### 15. Object-Oriented Programming Demonstrations
Educational programs showcasing OOP concepts.
- **Location:** `foundations/oop-demonstrations/`
- **Features:**
  - Class and object demonstrations
  - Software engineer traits program
  - Encapsulation examples
  - Method and attribute usage
- **Technologies:** Python

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

## 📊 Repository Statistics

- **Total Projects**: 22 programs across 15 categories
- **Programming Language**: Python 3
- **Lines of Code**: 2,300+
- **Documentation**: Comprehensive README for each project
- **Categories**: 6 main areas (ML, CV, Data Structures, Applications, Games, Foundations)

## 🎓 Course Information

These projects were developed as part of Master's program coursework in:
- **CSC525** - Principles of Machine Learning
- Computer Vision fundamentals
- Data Structures & Algorithms
- Software Engineering
- Application Development
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
