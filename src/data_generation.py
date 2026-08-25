"""
data_generation.py

Generates a synthetic customer dataset shaped like the classic
"Mall Customer Segmentation" dataset (CustomerID, Gender, Age,
Annual Income (k$), Spending Score (1-100)).

If you have the real Kaggle CSV, skip this module and load it directly
with pandas.read_csv() instead — everything downstream expects the same
column names, so no other code needs to change.
"""

import numpy as np
import pandas as pd


def generate_customer_data(n_per_segment: int = 40, random_state: int = 42) -> pd.DataFrame:
    """Generate a synthetic customer dataset with 5 realistic underlying segments.

    Returns
    -------
    pd.DataFrame with columns:
        CustomerID, Gender, Age, Annual Income (k$), Spending Score (1-100)
    """
    rng = np.random.default_rng(random_state)

    segments = [
        {"n": n_per_segment, "age": (18, 35), "income": (15, 40), "spend": (60, 95)},   # Young, low income, high spenders
        {"n": n_per_segment, "age": (25, 45), "income": (60, 100), "spend": (55, 90)},  # High income, high spenders
        {"n": n_per_segment, "age": (30, 55), "income": (60, 100), "spend": (5, 40)},   # High income, low spenders
        {"n": n_per_segment, "age": (35, 65), "income": (15, 45), "spend": (5, 40)},    # Low income, low spenders
        {"n": n_per_segment, "age": (25, 50), "income": (40, 60), "spend": (40, 60)},   # Average across the board
    ]

    rows = []
    cid = 1
    for seg in segments:
        for _ in range(seg["n"]):
            age = rng.integers(*seg["age"])
            income = rng.integers(*seg["income"])
            spend = rng.integers(*seg["spend"])
            gender = rng.choice(["Male", "Female"])
            rows.append([cid, gender, age, income, spend])
            cid += 1

    df = pd.DataFrame(
        rows,
        columns=["CustomerID", "Gender", "Age", "Annual Income (k$)", "Spending Score (1-100)"],
    )
    df = df.sample(frac=1, random_state=random_state).reset_index(drop=True)
    return df


if __name__ == "__main__":
    df = generate_customer_data()
    out_path = "data/mall_customers.csv"
    df.to_csv(out_path, index=False)
    print(f"Generated {len(df)} rows -> {out_path}")
