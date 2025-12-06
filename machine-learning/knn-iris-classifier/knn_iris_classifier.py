# Option 1 KNN classifier with Iris Data- CSC525 Principles of Machine Learning
# By: Serenity Healy
#KNN classifier on Iris flower data using class CSV file

#instructions for running the program
#Step 1: Install dependencies in terminal= pip install scikit-learn pandas numpy
#Step 2: Place the csv Iris flower data in the same folder as the current python file
#Step 3: Run the script and enter a number for each of the four prompts to get an Iris flower that is closest to measurements
#Four floating-point inputs sepal length, sepal width, petal length and width


import argparse
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

FEATURE_ALIASES = {
    "sepal_length": {"sepal_length", "sepallength", "sepallengthcm", "sepal.length", "sepal length"},
    "sepal_width":  {"sepal_width", "sepalwidth", "sepalwidthcm", "sepal.width", "sepal width"},
    "petal_length": {"petal_length", "petallength", "petallengthcm", "petal.length", "petal length"},
    "petal_width":  {"petal_width", "petalwidth", "petalwidthcm", "petal.width", "petal width"},
}

LABEL_ALIASES = {"species", "variety", "label", "class", "target", "name"}
#normalize the names of columns so different names work
#any alias possible in case data schema drifts
def _normalize(name: str) -> str:
    return "".join(ch for ch in name.lower() if ch.isalnum())

def _resolve_columns(df: pd.DataFrame):
    norm_to_orig = {_normalize(c): c for c in df.columns}

    def find_one(candidates):
        for cand in candidates:
            if cand in norm_to_orig:
                return norm_to_orig[cand]
        return None

    sepal_length = find_one({_normalize(x) for x in FEATURE_ALIASES["sepal_length"]})
    sepal_width  = find_one({_normalize(x) for x in FEATURE_ALIASES["sepal_width"]})
    petal_length = find_one({_normalize(x) for x in FEATURE_ALIASES["petal_length"]})
    petal_width  = find_one({_normalize(x) for x in FEATURE_ALIASES["petal_width"]})
    label        = find_one({_normalize(x) for x in LABEL_ALIASES})

    missing = [n for n, v in [
        ("sepal_length", sepal_length),
        ("sepal_width",  sepal_width),
        ("petal_length", petal_length),
        ("petal_width",  petal_width),
        ("label",        label),
    ] if v is None]

    if missing:
        raise ValueError(
            "Iris.csv headers not recognized.\n"
            f"Found columns: {list(df.columns)}\n"
            f"Missing/unknown: {missing}\n"
            "Tip: rename your headers to something like "
            "[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species]."
        )

    return [sepal_length, sepal_width, petal_length, petal_width], label
# pandas names columns = sanity check assume no header row
def load_data(path: str):
    df = pd.read_csv(path)
    if list(df.columns) == list(range(len(df.columns))):
        df = pd.read_csv(path, header=None)
        df.columns = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]
    feature_cols, label_col = _resolve_columns(df)
    X = df[feature_cols].values.astype(float)
    y = df[label_col].astype(str).values
    return X, y
#the search for the best k - GridSearchCV - replaces manual guessing
#CV balances 5-fold bias/variance w/out too much compute time
def build_and_select_k(X, y):
    pipe = Pipeline([("scaler", StandardScaler()), ("knn", KNeighborsClassifier())])
    search = GridSearchCV(pipe, {"knn__n_neighbors": [3, 5, 7, 9, 11]}, cv=5, n_jobs=-1)
    search.fit(X, y)
    return search.best_estimator_, search.best_params_["knn__n_neighbors"], search.best_score_
## dimple distance model accuracy .96 on test run
#test random flower measurements
def train_final_model(X, y, k):
    pipe = Pipeline([("scaler", StandardScaler()), ("knn", KNeighborsClassifier(n_neighbors=k))])
    pipe.fit(X, y)
    return pipe
#reshape keeps single sample 2D for sklearn requirement
def parse_inputs(args):
    if len(args.floats) == 4:
        return np.array(args.floats, dtype=float)
    prompts = ["Sepal length (cm): ", "Sepal width (cm): ", "Petal length (cm): ", "Petal width (cm): "]
    vals = [float(input(p).strip()) for p in prompts]
    return np.array(vals, dtype=float)

def main():
    parser = argparse.ArgumentParser(description="KNN Iris Classifier (auto-detects Iris.csv headers)")
    parser.add_argument("floats", nargs="*", type=float,
                        help="Four floats: sepal_length sepal_width petal_length petal_width")
    parser.add_argument("--holdout", action="store_true",
                        help="Show a quick hold-out accuracy check before training final model")
    args = parser.parse_args()

    X, y = load_data("Iris.csv")

    if args.holdout:
        X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
        pipe = Pipeline([("scaler", StandardScaler()), ("knn", KNeighborsClassifier(n_neighbors=5))])
        pipe.fit(X_tr, y_tr)
        y_pred = pipe.predict(X_te)
        print(f"Hold-out accuracy with k=5: {accuracy_score(y_te, y_pred):.3f}")

    _, best_k, cv_score = build_and_select_k(X, y)
    print(f"Selected k={best_k} via 5-fold CV (mean CV accuracy={cv_score:.3f})")
    model = train_final_model(X, y, best_k)

    sample = parse_inputs(args).reshape(1, -1)
    pred = model.predict(sample)[0]
    print(f"Predicted species: {pred}")

if __name__ == "__main__":
    main()

