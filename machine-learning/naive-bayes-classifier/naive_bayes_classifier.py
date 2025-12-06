import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import math


class FlowerClassificationModel:
    def __init__(self, laplace_factor=1.0):
        self.laplace_factor = laplace_factor
        self.target_labels = None
        self.sample_distribution = {}
        self.statistical_parameters = {}
        self.dataset_size = 0

    def build_data_frequency_matrix(self, features, targets):
        print("Building data frequency matrix...")
        data_frame = pd.DataFrame(features)
        data_frame['label'] = targets

        frequency_matrix = {}
        for label in self.target_labels:
            label_subset = data_frame[data_frame['label'] == label]
            frequency_matrix[label] = {
                'sample_count': len(label_subset),
                'feature_data': label_subset.drop('label', axis=1)
            }
            print(f"Label {label}: {len(label_subset)} data points")

        return frequency_matrix

    def compute_probability_parameters(self, features, targets):
        print("\nComputing probability parameters...")
        parameter_storage = {}

        for label in self.target_labels:
            label_filter = (targets == label)
            label_features = features[label_filter]

            feature_means = np.mean(label_features, axis=0)
            feature_deviations = np.std(label_features, axis=0)

            parameter_storage[label] = {
                'average_values': feature_means,
                'deviation_values': feature_deviations
            }

            print(f"Label {label} - Averages: {feature_means}")
            print(f"Label {label} - Deviations: {feature_deviations}")

        return parameter_storage

    def normal_distribution_density(self, value, avg, deviation):
        if deviation == 0:
            deviation = 1e-6

        exponential_term = math.exp(-0.5 * ((value - avg) / deviation) ** 2)
        density = (1 / (deviation * math.sqrt(2 * math.pi))) * exponential_term
        return density

    def avoid_zero_probabilities(self, probability_value):
        if probability_value == 0:
            return 1e-10
        return probability_value

    def train_classifier(self, features, targets):
        self.target_labels = np.unique(targets)
        self.dataset_size = len(targets)

        for label in self.target_labels:
            self.sample_distribution[label] = np.sum(targets == label)

        self.frequency_matrix = self.build_data_frequency_matrix(features, targets)
        self.parameter_storage = self.compute_probability_parameters(features, targets)

        print(f"\nLabel distribution:")
        for label in self.target_labels:
            distribution = self.sample_distribution[label] / self.dataset_size
            print(f"P(label={label}) = {distribution:.3f}")

    def compute_class_probabilities(self, input_sample):
        probability_scores = {}

        for label in self.target_labels:
            prior_probability = self.sample_distribution[label] / self.dataset_size

            combined_likelihood = 1.0
            for idx, feature_value in enumerate(input_sample):
                avg = self.parameter_storage[label]['average_values'][idx]
                dev = self.parameter_storage[label]['deviation_values'][idx]

                feature_density = self.normal_distribution_density(feature_value, avg, dev)
                feature_density = self.avoid_zero_probabilities(feature_density)
                combined_likelihood *= feature_density

            final_probability = prior_probability * combined_likelihood
            probability_scores[label] = final_probability

        probability_sum = sum(probability_scores.values())
        if probability_sum > 0:
            for label in probability_scores:
                probability_scores[label] /= probability_sum

        return probability_scores

    def classify_sample(self, input_sample):
        scores = self.compute_class_probabilities(input_sample)
        return max(scores, key=scores.get)

    def classify_dataset(self, feature_matrix):
        classification_results = []
        for sample in feature_matrix:
            result = self.classify_sample(sample)
            classification_results.append(result)
        return np.array(classification_results)

    def get_probability_matrix(self, feature_matrix):
        probability_matrix = []
        for sample in feature_matrix:
            scores = self.compute_class_probabilities(sample)
            score_vector = [scores[label] for label in self.target_labels]
            probability_matrix.append(score_vector)
        return np.array(probability_matrix)


def explain_smoothing_technique():
    print("\nSmoothing Technique Explanation:")
    print("Standard approach: P(feature|label) = occurrences(feature,label) / occurrences(label)")
    print("Issue: Zero occurrences result in zero probability, nullifying entire calculation")
    print("Smoothing solution: P(feature|label) = (occurrences + alpha) / (occurrences + alpha * vocabulary)")
    print("Benefit: Guarantees non-zero probabilities for robust classification")


def execute_classification_demo():
    print("Classification of Flowers Results:"
          "")

    iris_data = load_iris()
    input_features, output_labels = iris_data.data, iris_data.target

    train_features, test_features, train_labels, test_labels = train_test_split(
        input_features, output_labels, test_size=0.3, random_state=42)

    print(f"Complete dataset: {len(input_features)} specimens, {input_features.shape[1]} measurements")
    print(f"Training set: {len(train_features)} specimens")
    print(f"Testing set: {len(test_features)} specimens")

    flower_model = FlowerClassificationModel()
    flower_model.train_classifier(train_features, train_labels)

    print("\nGenerating classifications...")
    model_predictions = flower_model.classify_dataset(test_features)
    prediction_probabilities = flower_model.get_probability_matrix(test_features)

    print("\nDetailed results for initial samples:")
    for idx in range(3):
        print(f"Specimen {idx + 1}: Classified={model_predictions[idx]}, Truth={test_labels[idx]}")
        print(f"  Confidence scores: {prediction_probabilities[idx]}")

    model_accuracy = accuracy_score(test_labels, model_predictions)
    print(f"\nCustom model performance: {model_accuracy:.3f}")

    reference_model = GaussianNB()
    reference_model.fit(train_features, train_labels)
    reference_predictions = reference_model.predict(test_features)
    reference_accuracy = accuracy_score(test_labels, reference_predictions)

    print(f"Reference model performance: {reference_accuracy:.3f}")
    print(f"Performance difference: {abs(model_accuracy - reference_accuracy):.3f}")

    explain_smoothing_technique()

if __name__ == "__main__":
    execute_classification_demo()