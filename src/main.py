"""
main.py

Runs the full customer segmentation pipeline end to end:
1. Generate (or load) the dataset
2. EDA
3. Feature scaling + optimal-k search
4. K-Means clustering
5. Segment visualization + profiling

Run from the project root with:
    python src/main.py
"""

import os
import pandas as pd
from sklearn.metrics import silhouette_score

from data_generation import generate_customer_data
from eda import summarize, plot_distributions, plot_correlation_heatmap, plot_pairplot
from clustering import scale_features, find_optimal_k, fit_kmeans, plot_segments, profile_segments


DATA_PATH = "data/mall_customers.csv"
OUTDIR = "outputs"


def load_or_generate_data() -> pd.DataFrame:
    if os.path.exists(DATA_PATH):
        print(f"Loading existing dataset from {DATA_PATH}")
        return pd.read_csv(DATA_PATH)
    print("No dataset found — generating synthetic data...")
    df = generate_customer_data()
    os.makedirs("data", exist_ok=True)
    df.to_csv(DATA_PATH, index=False)
    print(f"Saved dataset to {DATA_PATH}")
    return df


def main():
    os.makedirs(OUTDIR, exist_ok=True)

    # 1. Data
    df = load_or_generate_data()

    # 2. EDA
    print("\n--- Running EDA ---")
    summarize(df)
    plot_distributions(df, OUTDIR)
    plot_correlation_heatmap(df, OUTDIR)
    plot_pairplot(df, OUTDIR)

    # 3. Scale + find k
    print("\n--- Clustering ---")
    feature_cols = ["Annual Income (k$)", "Spending Score (1-100)"]
    scaled, scaler = scale_features(df, feature_cols)
    best_k = find_optimal_k(scaled, outdir=OUTDIR)
    print(f"Best k by silhouette score: {best_k}")

    # 4. Fit K-Means
    k = 5
    kmeans = fit_kmeans(scaled, k)
    df["Cluster"] = kmeans.labels_
    score = silhouette_score(scaled, df["Cluster"])
    print(f"Silhouette Score (k={k}): {score:.3f}")

    # 5. Visualize + profile
    plot_segments(df, kmeans, scaler, feature_cols[0], feature_cols[1], OUTDIR)
    profile = profile_segments(df)
    print("\n=== Segment Profiles ===")
    print(profile)

    df.to_csv(os.path.join(OUTDIR, "customers_with_segments.csv"), index=False)
    profile.to_csv(os.path.join(OUTDIR, "segment_profiles.csv"))

    print(f"\nAll plots and result CSVs saved to {OUTDIR}/")


if __name__ == "__main__":
    main()
