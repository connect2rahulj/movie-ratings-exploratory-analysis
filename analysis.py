"""
analysis.py
Performs exploratory data analysis on the movie ratings dataset.
Produces and saves three charts:
  1. Rating distribution (histogram)
  2. Average rating by genre (bar chart)
  3. Average rating by year (line chart)
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os
import sys


DATA_PATH = os.path.join("data", "movies.csv")


def load_data(path):
    if not os.path.exists(path):
        print(f"ERROR: Dataset not found at '{path}'.")
        print("Please run 'python generate_data.py' first.")
        sys.exit(1)
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} movies.\n")
    return df


def summary_stats(df):
    print("=== Basic Info ===")
    print(df.info())
    print("\n=== Descriptive Statistics ===")
    print(df.describe())
    print()

    print("=== Missing Values ===")
    print(df.isnull().sum())
    print()

    print("=== Movies per Genre ===")
    print(df["genre"].value_counts())
    print()


def plot_rating_distribution(df):
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.hist(df["rating"], bins=30, color="steelblue", edgecolor="white", linewidth=0.5)
    ax.set_title("Distribution of Movie Ratings", fontsize=14, fontweight="bold")
    ax.set_xlabel("Rating (out of 10)")
    ax.set_ylabel("Number of Movies")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

    mean_rating = df["rating"].mean()
    ax.axvline(mean_rating, color="tomato", linestyle="--", linewidth=1.5, label=f"Mean: {mean_rating:.2f}")
    ax.legend()

    plt.tight_layout()
    plt.savefig("rating_distribution.png", dpi=150)
    plt.close()
    print("Saved: rating_distribution.png")


def plot_avg_rating_by_genre(df):
    genre_avg = (
        df.groupby("genre")["rating"]
        .mean()
        .sort_values()
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    bars = ax.barh(genre_avg.index, genre_avg.values, color="mediumseagreen", edgecolor="white")
    ax.set_title("Average Rating by Genre", fontsize=14, fontweight="bold")
    ax.set_xlabel("Average Rating")
    ax.set_xlim(0, 10)

    # Add value labels
    for bar, val in zip(bars, genre_avg.values):
        ax.text(val + 0.1, bar.get_y() + bar.get_height() / 2,
                f"{val:.2f}", va="center", fontsize=9)

    plt.tight_layout()
    plt.savefig("avg_rating_by_genre.png", dpi=150)
    plt.close()
    print("Saved: avg_rating_by_genre.png")


def plot_avg_rating_by_year(df):
    year_avg = (
        df.groupby("year")["rating"]
        .mean()
        .reset_index()
        .sort_values("year")
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(year_avg["year"], year_avg["rating"], marker="o", markersize=4,
            color="darkorange", linewidth=1.8, label="Avg Rating")

    # Rolling average for trend line
    year_avg["rolling_avg"] = year_avg["rating"].rolling(window=3, center=True).mean()
    ax.plot(year_avg["year"], year_avg["rolling_avg"], color="steelblue",
            linewidth=2, linestyle="--", label="3-Year Rolling Avg")

    ax.set_title("Average Movie Rating by Release Year", fontsize=14, fontweight="bold")
    ax.set_xlabel("Release Year")
    ax.set_ylabel("Average Rating")
    ax.set_ylim(4, 9)
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig("avg_rating_by_year.png", dpi=150)
    plt.close()
    print("Saved: avg_rating_by_year.png")


def main():
    df = load_data(DATA_PATH)
    summary_stats(df)
    plot_rating_distribution(df)
    plot_avg_rating_by_genre(df)
    plot_avg_rating_by_year(df)
    print("\nAnalysis complete. Check the PNG files for visualizations.")


if __name__ == "__main__":
    main()