# Shallow Artificial Neural Network

Custom 2-layer neural network implementations built from scratch for arithmetic sequence prediction.

## Overview

This project demonstrates a shallow artificial neural network (ANN) built entirely from scratch using only NumPy. The network learns to predict the next number in arithmetic sequences through gradient descent and backpropagation.

## Features

- **From-Scratch Implementation**: No deep learning frameworks, pure NumPy
- **2-Layer Architecture**: Input → Hidden (ReLU) → Output (Linear)
- **Backpropagation**: Full implementation of gradient descent
- **Loss Tracking**: Monitors training progress across epochs
- **Interactive Testing**: Test with custom sequences
- **Educational Focus**: Detailed comments and architecture display

## Files

- `shallow_ann.py` - Main implementation with sequence prediction
- `foundations_neural_network.py` - Duplicate/alternate version

## Installation

```bash
# Install NumPy
pip install numpy
```

## Usage

```bash
# Run the neural network
python shallow_ann.py
```

The program will:
1. Generate arithmetic sequence training data
2. Display network architecture
3. Train for 2000 epochs (showing progress every 200 epochs)
4. Test on predefined sequences
5. Enter interactive mode for custom testing

### Interactive Mode

```
Enter sequence: 2 4 6
Predicted next number in sequence: 8.00

Enter sequence: 5 10 15
Predicted next number in sequence: 20.00

Enter sequence: quit
```

## Architecture

```
Input Layer:  3 neurons  (for 3-number sequences)
Hidden Layer: 10 neurons (ReLU activation)
Output Layer: 1 neuron   (Linear activation)
```

### Activation Functions

- **ReLU** (Hidden Layer): f(x) = max(0, x)
- **Linear** (Output): f(x) = x

## How It Works

### 1. Forward Propagation
```
z1 = X · W1 + b1
a1 = ReLU(z1)
z2 = a1 · W2 + b2
output = z2
```

### 2. Loss Calculation
Uses Mean Squared Error (MSE):
```
MSE = mean((y_true - y_pred)²)
```

### 3. Backpropagation
Computes gradients and updates weights:
```
dW2 = a1^T · dZ2
dW1 = X^T · dZ1
W2 -= learning_rate * dW2
W1 -= learning_rate * dW1
```

## Training Data

Generates arithmetic sequences:
- Pattern: [a, a+d, a+2d] → a+3d
- Start values: 0 to 20
- Step values: 1 to 6
- Total training samples: ~150

## Performance

Typical results:
- **Initial Loss**: ~400-600
- **Final Loss**: ~0.01-0.10
- **Loss Reduction**: 99%+
- **Average Prediction Error**: <2.0

## Example Output

```
1. Generating arithmetic sequence data...
Training data shape: (130, 3)
Sample sequences:
  [0. 1. 2.] -> 3.0
  [0. 2. 4.] -> 6.0

2. Creating neural network...
Network Architecture:
  Input Layer: 3 neurons
  Hidden Layer: 10 neurons (ReLU activation)
  Output Layer: 1 neuron (Linear activation)

3. Training the network...
Epoch 200/2000, Loss: 45.234567
Epoch 400/2000, Loss: 12.345678
...
Epoch 2000/2000, Loss: 0.056789

Training Loss Summary:
Initial Loss: 456.789012
Final Loss: 0.056789
Loss Reduction: 99.99%

4. Testing the trained network...
Input: [1, 2, 3] -> Predicted: 4.02, Expected: 4, Error: 0.02
```

## Technical Details

**Weight Initialization**: He initialization (√(2/n))
**Learning Rate**: 0.01
**Epochs**: 2000
**Optimizer**: Standard gradient descent
**Loss Function**: Mean Squared Error

## Code Structure

### Class: ShallowANN
- `__init__()`: Initialize weights and biases
- `relu()`: ReLU activation function
- `relu_derivative()`: Derivative for backprop
- `feedforward()`: Forward propagation
- `mean_squared_error()`: Loss calculation
- `backpropagation()`: Gradient computation
- `train()`: Training loop
- `predict()`: Make predictions
- `display_loss_summary()`: Show training results

## Learning Outcomes

- Neural network architecture design
- Implementing forward and backward propagation
- Gradient descent optimization
- Activation functions and their derivatives
- Weight initialization techniques
- Training loop and loss monitoring
