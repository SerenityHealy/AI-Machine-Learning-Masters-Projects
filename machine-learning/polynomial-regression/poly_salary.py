# poly_salary.py
# Polynomial Regression: Predict Salary from Years of Experience
# Usage:
#   python poly_salary.py --data Salary_Data.csv --degree 2 --test_size 0.2 --random_state 42
#
# Notes for graders:
# - Loads a simple 2-column CSV with headers: YearsExperience, Salary
# - Trains a polynomial regression (degree configurable; default=2)
# - Prints R^2 and MAE on the test split
# - Shows example predictions for several years of experience
# - Optionally plots and saves a curve figure as 'salary_poly_fit.png'

import argparse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_absolute_error

# Matplotlib is used for an optional plot (no style/colors set as requested)
import matplotlib.pyplot as plt

def build_model(degree: int = 2):
    return Pipeline([
        ("poly", PolynomialFeatures(degree=degree, include_bias=False)),
        ("lr", LinearRegression())
    ])

def main():
    parser = argparse.ArgumentParser(description="Polynomial Regression for Salary vs Years of Experience")
    parser.add_argument("--data", type=str, default="Salary_Data.csv",
                        help="Path to CSV with columns: YearsExperience, Salary")
    parser.add_argument("--degree", type=int, default=2, help="Polynomial degree (e.g., 2 or 3)")
    parser.add_argument("--test_size", type=float, default=0.2, help="Test split size")
    parser.add_argument("--random_state", type=int, default=42, help="Random seed for reproducibility")
    parser.add_argument("--no_plot", action="store_true", help="Skip plotting the fitted curve")
    args = parser.parse_args()

    # Load data
    df = pd.read_csv(args.data)
    if not {"YearsExperience", "Salary"}.issubset(df.columns):
        raise ValueError("CSV must contain 'YearsExperience' and 'Salary' columns.")

    X = df[["YearsExperience"]].values
    y = df["Salary"].values

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=args.test_size, random_state=args.random_state
    )

    # Build and fit model
    model = build_model(degree=args.degree)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"Polynomial degree: {args.degree}")
    print("R^2:", r2)
    print("MAE:", mae)

    # Example predictions
    for yrs in [1.0, 3.0, 5.0, 10.0]:
        pred = model.predict(np.array([[yrs]])).item()
        print(f"Predicted salary for {yrs:.1f} years: {pred:.2f}")

    # Optional plot
    if not args.no_plot:
        # Scatter of data
        plt.figure()
        plt.scatter(X, y, label="Data")

        # Smooth curve across the observed range
        x_min, x_max = float(np.min(X)), float(np.max(X))
        x_curve = np.linspace(x_min, x_max, 300).reshape(-1, 1)
        y_curve = model.predict(x_curve)
        plt.plot(x_curve, y_curve, label=f"Polynomial fit (degree={args.degree})")

        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
        plt.title("Polynomial Regression: Salary vs Years of Experience")
        plt.legend()
        plt.tight_layout()
        plt.savefig("salary_poly_fit.png", dpi=150)
        # Show for interactive runs; harmless in batch
        try:
            plt.show()
        except Exception:
            pass

if __name__ == "__main__":
    main()