"""
eda.py

Exploratory data analysis helpers: summary stats and standard plots,
saved to the outputs/ folder.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


def summarize(df: pd.DataFrame) -> None:
    """Print basic info, missing values, and descriptive stats."""
    print("=== Shape ===")
    print(df.shape)
    print("\n=== Info ===")
    df.info()
    print("\n=== Missing values ===")
    print(df.isnull().sum())
    print("\n=== Describe ===")
    print(df.describe())


def plot_distributions(df: pd.DataFrame, outdir: str = "outputs") -> None:
    """Save histogram distributions for Age, Income, Spending Score."""
    os.makedirs(outdir, exist_ok=True)
    fig, axes = plt.subplots(1, 3, figsize=(16, 4))
    sns.histplot(df["Age"], kde=True, ax=axes[0], color="steelblue")
    axes[0].set_title("Age Distribution")

    sns.histplot(df["Annual Income (k$)"], kde=True, ax=axes[1], color="seagreen")
    axes[1].set_title("Annual Income Distribution")

    sns.histplot(df["Spending Score (1-100)"], kde=True, ax=axes[2], color="indianred")
    axes[2].set_title("Spending Score Distribution")

    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "distributions.png"), dpi=150)
    plt.close()


def plot_correlation_heatmap(df: pd.DataFrame, outdir: str = "outputs") -> None:
    os.makedirs(outdir, exist_ok=True)
    plt.figure(figsize=(6, 5))
    cols = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
    sns.heatmap(df[cols].corr(), annot=True, cmap="coolwarm", center=0)
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "correlation_heatmap.png"), dpi=150)
    plt.close()


def plot_pairplot(df: pd.DataFrame, outdir: str = "outputs") -> None:
    os.makedirs(outdir, exist_ok=True)
    g = sns.pairplot(
        df,
        vars=["Age", "Annual Income (k$)", "Spending Score (1-100)"],
        hue="Gender",
        palette="husl",
    )
    g.fig.suptitle("Pairwise Relationships", y=1.02)
    g.savefig(os.path.join(outdir, "pairplot.png"), dpi=150)
    plt.close()


if __name__ == "__main__":
    df = pd.read_csv("data/mall_customers.csv")
    summarize(df)
    plot_distributions(df)
    plot_correlation_heatmap(df)
    plot_pairplot(df)
    print("\nEDA plots saved to outputs/")
