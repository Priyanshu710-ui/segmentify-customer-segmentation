"""
clustering.py

K-Means clustering pipeline: feature scaling, optimal-k search
(elbow method + silhouette score), fitting, and customer profiling.
"""

import os
from typing import Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

sns.set_style("whitegrid")


def scale_features(df: pd.DataFrame, columns: list) -> Tuple[np.ndarray, StandardScaler]:
    """Scale the given columns with StandardScaler. Returns (scaled_array, fitted_scaler)."""
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[columns])
    return scaled, scaler


def find_optimal_k(scaled_data: np.ndarray, k_range=range(2, 11), outdir: str = "outputs") -> int:
    """Run the elbow method + silhouette score across k_range, save the plot,
    and return the k with the best silhouette score."""
    inertias, sil_scores = [], []

    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = km.fit_predict(scaled_data)
        inertias.append(km.inertia_)
        sil_scores.append(silhouette_score(scaled_data, labels))

    os.makedirs(outdir, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].plot(list(k_range), inertias, marker="o", color="darkorange")
    axes[0].set_title("Elbow Method")
    axes[0].set_xlabel("Number of Clusters (k)")
    axes[0].set_ylabel("Inertia")

    axes[1].plot(list(k_range), sil_scores, marker="o", color="teal")
    axes[1].set_title("Silhouette Score by k")
    axes[1].set_xlabel("Number of Clusters (k)")
    axes[1].set_ylabel("Silhouette Score")

    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "k_selection.png"), dpi=150)
    plt.close()

    best_k = list(k_range)[int(np.argmax(sil_scores))]
    return best_k


def fit_kmeans(scaled_data: np.ndarray, k: int) -> KMeans:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(scaled_data)
    return km


def plot_segments(df: pd.DataFrame, kmeans: KMeans, scaler: StandardScaler,
                   x_col: str, y_col: str, outdir: str = "outputs") -> None:
    os.makedirs(outdir, exist_ok=True)
    k = kmeans.n_clusters
    palette = sns.color_palette("husl", k)

    plt.figure(figsize=(9, 6))
    for cluster_id in sorted(df["Cluster"].unique()):
        subset = df[df["Cluster"] == cluster_id]
        plt.scatter(subset[x_col], subset[y_col], s=60,
                    color=palette[cluster_id], label=f"Segment {cluster_id}")

    centers = scaler.inverse_transform(kmeans.cluster_centers_)
    plt.scatter(centers[:, 0], centers[:, 1], s=250, c="black", marker="X", label="Centroids")

    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"Customer Segments (K-Means, k={k})")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "segments.png"), dpi=150)
    plt.close()


def label_segment(income: float, spend: float) -> str:
    """Turn a cluster's average income/spending into a human-readable business label."""
    if income >= 55 and spend >= 55:
        return "High Income, High Spenders (Target segment)"
    if income >= 55 and spend < 55:
        return "High Income, Low Spenders (Careful/Price-sensitive)"
    if income < 55 and spend >= 55:
        return "Low Income, High Spenders (Impulsive)"
    if income < 55 and spend < 55:
        return "Low Income, Low Spenders (Budget-conscious)"
    return "Average Income, Average Spenders"


def profile_segments(df: pd.DataFrame) -> pd.DataFrame:
    """Return a per-cluster summary table with a business-readable label."""
    profile = df.groupby("Cluster")[["Age", "Annual Income (k$)", "Spending Score (1-100)"]].mean().round(1)
    profile["Count"] = df["Cluster"].value_counts().sort_index()
    profile["Segment Label"] = profile.apply(
        lambda row: label_segment(row["Annual Income (k$)"], row["Spending Score (1-100)"]), axis=1
    )
    return profile


if __name__ == "__main__":
    df = pd.read_csv("data/mall_customers.csv")

    feature_cols = ["Annual Income (k$)", "Spending Score (1-100)"]
    scaled, scaler = scale_features(df, feature_cols)

    best_k = find_optimal_k(scaled)
    print(f"Best k by silhouette score: {best_k}")

    k = 5  # override with best_k if you want it fully automatic
    kmeans = fit_kmeans(scaled, k)
    df["Cluster"] = kmeans.labels_

    print(f"Silhouette Score (k={k}): {silhouette_score(scaled, df['Cluster']):.3f}")

    plot_segments(df, kmeans, scaler, "Annual Income (k$)", "Spending Score (1-100)")

    profile = profile_segments(df)
    print("\n=== Segment Profiles ===")
    print(profile)

    df.to_csv("outputs/customers_with_segments.csv", index=False)
    profile.to_csv("outputs/segment_profiles.csv")
    print("\nResults saved to outputs/")
