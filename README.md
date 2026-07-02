# Movie Ratings Exploratory Analysis

An exploratory data analysis (EDA) project examining a synthetic movie ratings dataset. This project uses Python, Pandas, and Matplotlib to uncover trends across genres, release years, and rating distributions.

## Project Overview

This analysis answers questions like:
- Which genres tend to receive the highest ratings?
- How have average movie ratings changed over time?
- What does the overall distribution of ratings look like?

## Project Structure

```
movie-ratings-eda/
├── README.md
├── generate_data.py       # Script to generate the synthetic dataset
├── analysis.py            # Main EDA script with charts
├── requirements.txt       # Python dependencies
└── data/
    └── movies.csv         # Generated dataset (created by generate_data.py)
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/movie-ratings-eda.git
cd movie-ratings-eda
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate the dataset

```bash
python generate_data.py
```

### 4. Run the analysis

```bash
python analysis.py
```

Charts will be saved as PNG files in the current directory.

## Sample Visualizations

The script produces three charts:

- **Rating Distribution** — Histogram of all movie ratings
- **Average Rating by Genre** — Horizontal bar chart comparing genres
- **Average Rating by Year** — Line chart showing rating trends over time

## Skills Demonstrated

- Python scripting
- Data generation and manipulation with **Pandas** and **NumPy**
- Data visualization with **Matplotlib**
- Exploratory data analysis workflow

## Requirements

- Python 3.8+
- pandas
- numpy
- matplotlib