# Customer Segmentation Project

Group customers into distinct segments based on purchasing behavior, using K-Means
clustering (unsupervised learning). Built as a proper VS Code project — modular
source files under `src/`, plus a runnable notebook under `notebooks/`.

## Project Structure
```
customer-segmentation/
├── .vscode/
│   ├── settings.json      # Python interpreter + Jupyter config
│   ├── extensions.json    # Recommended extensions
│   └── launch.json        # Run/debug config for main.py
├── data/
│   └── mall_customers.csv # Generated on first run (or drop in the real Kaggle CSV)
├── src/
│   ├── data_generation.py # Builds the synthetic dataset
│   ├── eda.py              # Summary stats + distribution/correlation/pairplot charts
│   ├── clustering.py       # Scaling, k-selection, K-Means, profiling
│   └── main.py             # Runs the full pipeline end to end
├── notebooks/
│   └── customer_segmentation.ipynb  # Same pipeline, in notebook form
├── outputs/                # Generated plots + result CSVs land here
├── requirements.txt
└── README.md
```

## Setup in VS Code

1. **Open the folder** in VS Code: `File > Open Folder...` → select `customer-segmentation/`.

2. **Create a virtual environment** (Terminal → New Terminal):
   ```bash
   python -m venv .venv
   ```
   ```bash
   # macOS/Linux
   source .venv/bin/activate
   ```
   ```powershell
   # Windows
   .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Select the interpreter:** `Ctrl/Cmd + Shift + P` → "Python: Select Interpreter" →
   choose `.venv`. VS Code should also pick it up automatically from `.vscode/settings.json`.

5. Install the recommended extensions if prompted (Python + Jupyter) — VS Code will
   suggest these from `.vscode/extensions.json`.

## Running it

**Option A — as a script (recommended for VS Code):**
```bash
python src/main.py
```
This runs the whole pipeline — data generation, EDA, clustering, profiling — and saves
all plots and result CSVs to `outputs/`.

Or press **F5** in VS Code (uses the pre-configured "Run Full Pipeline" launch config).

**Option B — as a notebook:**
Open `notebooks/customer_segmentation.ipynb` in VS Code and run all cells
(the Jupyter extension handles this natively — no separate Jupyter server needed).

## Using the real Kaggle dataset

By default this generates a synthetic dataset shaped like the classic "Mall Customer
Segmentation Data" (`CustomerID`, `Gender`, `Age`, `Annual Income (k$)`,
`Spending Score (1-100)`), so the project runs with zero downloads.

To use the real one instead:
1. Download it from Kaggle (search "Mall Customer Segmentation Data").
2. Save it as `data/mall_customers.csv`, matching the same column names.
3. Re-run `python src/main.py` — it detects the existing file and skips generation.

## What it demonstrates
- Exploratory Data Analysis (distributions, correlations, pairplots)
- Feature scaling (StandardScaler)
- Choosing k with the Elbow Method + Silhouette Score
- K-Means clustering
- Segment visualization with centroids
- Customer profiling — turning clusters into business-readable labels

## Resume line
"Built a K-Means customer segmentation pipeline in Python (Scikit-learn, Pandas),
identifying 5 actionable customer segments from income/spending data to inform
targeted marketing strategy."
