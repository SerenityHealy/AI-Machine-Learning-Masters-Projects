import numpy as np


class ShallowANN:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        """
        Initialize the 2-layer Neural Network

        Args:
            input_size: Number of input features
            hidden_size: Number of neurons in hidden layer
            output_size: Number of output neurons
            learning_rate: Learning rate for gradient descent
        """
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        self.W1 = np.random.randn(self.input_size, self.hidden_size) * np.sqrt(2.0 / self.input_size)
        self.b1 = np.zeros((1, self.hidden_size))

        self.W2 = np.random.randn(self.hidden_size, self.output_size) * np.sqrt(2.0 / self.hidden_size)
        self.b2 = np.zeros((1, self.output_size))


        self.loss_history = []

    def relu(self, x):

        return np.maximum(0, x)

    def relu_derivative(self, x):

        return (x > 0).astype(float)

    def feedforward(self, X):
        """
        Forward propagation through the network

        Args:
            X: Input data matrix

        Returns:
            output: Predicted output
        """

        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.relu(self.z1)  # ReLU activation


        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.z2  # Linear output for regression

        return self.a2

    def mean_squared_error(self, y_true, y_pred):
        """Calculate Mean Squared Error loss function"""
        return np.mean((y_true - y_pred) ** 2)

    def backpropagation(self, X, y, y_pred):
        """
        Backward propagation to update weights and biases

        Args:
            X: Input data
            y: True output
            y_pred: Predicted output
        """
        m = X.shape[0]  # Number of samples


        dZ2 = (y_pred - y) / m
        dW2 = np.dot(self.a1.T, dZ2)
        db2 = np.sum(dZ2, axis=0, keepdims=True)


        dA1 = np.dot(dZ2, self.W2.T)
        dZ1 = dA1 * self.relu_derivative(self.z1)
        dW1 = np.dot(X.T, dZ1)
        db1 = np.sum(dZ1, axis=0, keepdims=True)

        #gradient descent
        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2
        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1

    def train(self, X, y, epochs=2000):
        """
        Train the neural network

        Args:
            X: Input training data
            y: Target output data
            epochs: Number of training iterations
        """
        print(f"Training neural network for {epochs} epochs...")

        for epoch in range(epochs):

            y_pred = self.feedforward(X)

            #loss
            loss = self.mean_squared_error(y, y_pred)
            self.loss_history.append(loss)


            self.backpropagation(X, y, y_pred)


            if (epoch + 1) % 200 == 0:
                print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss:.6f}")

        print("Training completed!")

    def predict(self, X):
        """Make predictions on new data"""
        return self.feedforward(X)

    def display_loss_summary(self):
        """Display training loss information"""
        print("\nTraining Loss Summary:")

        print(f"Initial Loss: {self.loss_history[0]:.6f}")
        print(f"Final Loss: {self.loss_history[-1]:.6f}")
        print(f"Loss Reduction: {((self.loss_history[0] - self.loss_history[-1]) / self.loss_history[0] * 100):.2f}%")


def create_simple_sequence_data():
    """
    Create training data for simple arithmetic sequences
    Focus on basic patterns: [a, a+d, a+2d] -> a+3d
    """
    sequences = []
    targets = []

    for start in range(0, 20):
        for step in range(1, 6):
            seq = [start, start + step, start + 2 * step]
            next_num = start + 3 * step
            sequences.append(seq)
            targets.append([next_num])


    for start in range(-10, 0):
        for step in range(1, 4):
            seq = [start, start + step, start + 2 * step]
            next_num = start + 3 * step
            sequences.append(seq)
            targets.append([next_num])

    return np.array(sequences, dtype=np.float32), np.array(targets, dtype=np.float32)


def main():


    print("\n1. Generating arithmetic sequence data...")
    X_train, y_train = create_simple_sequence_data()

    print(f"Training data shape: {X_train.shape}")
    print(f"Target data shape: {y_train.shape}")
    print(f"Sample sequences:")
    for i in range(5):
        print(f"  {X_train[i]} -> {y_train[i][0]}")


    print("\n2. Creating neural network...")
    ann = ShallowANN(input_size=3, hidden_size=10, output_size=1, learning_rate=0.01)

    print("Network Architecture:")
    print(f"  Input Layer: {ann.input_size} neurons")
    print(f"  Hidden Layer: {ann.hidden_size} neurons (ReLU activation)")
    print(f"  Output Layer: {ann.output_size} neuron (Linear activation)")


    print("\n3. Training the network...")
    ann.train(X_train, y_train, epochs=2000)


    ann.display_loss_summary()


    print("\n4. Testing the trained network...")
    test_sequences = [
        [1, 2, 3],
        [2, 4, 6],
        [5, 10, 15],
        [0, 1, 2],
        [3, 6, 9],
        [10, 20, 30],
        [-2, 0, 2],
        [1, 3, 5],
    ]

    print("\nPrediction Results:")


    total_error = 0
    for seq in test_sequences:
        seq_array = np.array(seq, dtype=np.float32).reshape(1, -1)
        pred = ann.predict(seq_array)
        expected = seq[0] + 3 * (seq[1] - seq[0])  # Calculate expected arithmetic sequence result
        error = abs(pred[0][0] - expected)
        total_error += error

        print(f"Input: {seq} -> Predicted: {pred[0][0]:.2f}, Expected: {expected}, Error: {error:.2f}")

    avg_error = total_error / len(test_sequences)
    print(f"\nAverage Prediction Error: {avg_error:.2f}")


    print("\n5. Testing Mode")

    print("Enter 3 numbers separated by spaces (or 'quit' to exit):")

    while True:
        try:
            user_input = input("\nEnter sequence: ").strip()

            if user_input.lower() == 'quit':
                break


            numbers = list(map(float, user_input.split()))

            if len(numbers) != 3:
                print("Please enter exactly 3 numbers.")
                continue


            seq_array = np.array(numbers, dtype=np.float32).reshape(1, -1)
            pred = ann.predict(seq_array)


            if len(set(np.diff(numbers))) <= 1:
                expected = numbers[0] + 3 * (numbers[1] - numbers[0])

                print(f"Predicted next number in sequence: {expected:.2f}")
            else:
                print(f"Predicted next number: {pred[0][0]:.2f}")
                print("(Not a simple arithmetic sequence)")

        except ValueError:
            print("Please enter valid numbers.")
        except KeyboardInterrupt:
            break

    print("\nProgram completed successfully!")


if __name__ == "__main__":
    main()