<div align="center">

# ✦ SEGMENTIFY

### AI-Powered Customer Segmentation Dashboard

**Upload a CSV. Let machine learning find the patterns. Turn raw customer data into actionable segments.**

[![Live Demo](https://img.shields.io/badge/🚀_LIVE_DEMO-Try_Segmentify-7C6CFF?style=for-the-badge)](https://segmentify-customer-segmentation-hdq4wvijv-jack-5127.vercel.app)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-K--Means-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Vercel](https://img.shields.io/badge/Deployed_on-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/)

<br />

[🚀 Live Demo](https://segmentify-customer-segmentation-hdq4wvijv-jack-5127.vercel.app) · [📦 Repository](https://github.com/Priyanshu710-ui/segmentify-customer-segmentation) · [🐛 Report Bug](https://github.com/Priyanshu710-ui/segmentify-customer-segmentation/issues)

</div>

---

## 🧠 What is Segmentify?

**Segmentify** is an interactive machine-learning web application that automatically groups customers with similar characteristics using **K-Means clustering**.

Instead of manually digging through rows of CSV data, a user can simply:

```text
        📄 Upload CSV
             │
             ▼
      🔍 Detect numeric data
             │
             ▼
       ⚡ Clean missing values
             │
             ▼
      📏 Standardize features
             │
             ▼
       🧠 Run K-Means ML
             │
             ▼
      🎯 Generate segments
             │
      ┌──────┼──────┐
      ▼      ▼      ▼
   Insights Charts Download
```

The result is a clean dashboard containing **customer counts, generated clusters, readable segment names, feature averages, visual data insights, and a downloadable segmented CSV**.

---

# 🚀 Live Demo

<div align="center">

### 👉 **[OPEN SEGMENTIFY →](https://segmentify-customer-segmentation-hdq4wvijv-jack-5127.vercel.app)**

Upload your own customer dataset and run the analysis directly from the browser.

</div>

---

# ✨ Why Segmentify?

| ⚡ | Feature | What it does |
|---|---|---|
| 📤 | **CSV Upload** | Analyze your own customer dataset directly from the dashboard. |
| 🔢 | **Automatic Feature Detection** | Detects numerical columns and ignores ID-like columns. |
| 🧹 | **Missing Value Handling** | Fills missing numerical values using column medians. |
| 📏 | **Feature Scaling** | Uses `StandardScaler` before clustering. |
| 🧠 | **K-Means Clustering** | Automatically groups similar customers. |
| 🎯 | **Up to 5 Segments** | Uses up to five clusters depending on dataset size. |
| 🏷️ | **Smart Segment Names** | Creates labels such as *High Income, High Spenders* when suitable columns exist. |
| 📊 | **Visual Insights** | Displays customer patterns and segmentation visuals. |
| 📋 | **Segment Profiles** | Shows customer count and average values for every generated group. |
| ⬇️ | **Export Results** | Downloads the original dataset enriched with `Segment` and `Segment Name`. |
| 🌙 | **Premium Dark UI** | Modern responsive dashboard built for a clean live demo experience. |

---

# 🛠️ Tech Stack

```text
╔══════════════════════════════════════════════════════╗
║                     SEGMENTIFY                       ║
╠══════════════════════════════════════════════════════╣
║  Frontend        HTML • CSS • JavaScript             ║
║  Backend         Python • Flask                      ║
║  Data            Pandas • NumPy                      ║
║  Machine Learning Scikit-learn • K-Means             ║
║  Preprocessing   StandardScaler                      ║
║  Deployment      Vercel                              ║
╚══════════════════════════════════════════════════════╝
```

---

# ⚙️ How the Machine Learning Works

## 1️⃣ Upload the dataset

The user uploads a CSV file containing customer information.

Example:

```csv
CustomerID,Age,Annual Income (k$),Spending Score (1-100)
1,19,15,39
2,21,15,81
3,20,16,6
4,23,16,77
```

> Segmentify needs at least **two numerical columns** after ID-like columns are excluded.

---

## 2️⃣ Detect useful features

The backend:

- removes completely empty columns
- finds numerical columns
- excludes columns whose names contain `id`
- uses the remaining numerical features for clustering

---

## 3️⃣ Handle missing values

Missing numerical values are filled using the **median** of their respective column.

```text
Age:        19, 21, NaN, 23
                    ↓
              Median Fill
                    ↓
Age:        19, 21, 21, 23
```

---

## 4️⃣ Scale the data

Different features may have completely different ranges.

For example:

```text
Age                  → 18 to 70
Annual Income        → 15 to 140
Spending Score       → 1 to 100
```

Segmentify uses **StandardScaler** so that features can contribute more fairly to the clustering process.

---

## 5️⃣ Run K-Means

The app creates up to **5 clusters**:

```python
n_clusters = min(5, len(dataset))
```

The K-Means model is configured with a fixed random state for reproducible behavior:

```python
KMeans(
    n_clusters=n_clusters,
    random_state=42,
    n_init=10
)
```

---

## 6️⃣ Turn clusters into readable groups

If the dataset contains income and spending-related columns, Segmentify compares cluster averages with the overall dataset average and can generate labels such as:

```text
💎 High Income, High Spenders
🧊 High Income, Low Spenders
🔥 Low Income, High Spenders
🌱 Low Income, Low Spenders
```

Otherwise, the application falls back to labels like:

```text
Customer Group 1
Customer Group 2
Customer Group 3
```

---

# 📊 Dashboard Experience

Once analysis is complete, the dashboard provides:

```text
┌─────────────────────────────────────────────┐
│                 SEGMENTIFY                  │
├──────────────────┬──────────────────────────┤
│ Total Customers  │ Customer Segments        │
│       200        │           5              │
├──────────────────┼──────────────────────────┤
│ Model            │ Status                   │
│     K-Means      │        Ready             │
└──────────────────┴──────────────────────────┘

                ↓ ANALYZE ↓

      ┌─────────────────────────────┐
      │     CUSTOMER SEGMENTS       │
      │  Group • Size • Averages    │
      └─────────────────────────────┘

                ↓

      📊 DATA VISUALIZATION

                ↓

      ⬇ DOWNLOAD SEGMENTED CSV
```

---

# 📂 Project Structure

```text
segmentify-customer-segmentation/
│
├── app.py                         # Flask API + ML analysis
├── requirements.txt               # Python dependencies
│
├── frontend/
│   ├── index.html                 # Dashboard structure
│   ├── style.css                  # Premium dark UI
│   └── script.js                  # Upload + API interaction
│
├── outputs/                       # Generated segmented CSV / visuals
│
├── data/                          # Dataset resources
├── src/                           # Additional ML pipeline modules
├── notebooks/                     # Notebook experimentation
│
└── README.md
```

---

# 🔌 API

## Analyze Customer Data

### `POST /api/analyze`

Send a CSV file using multipart form data:

```text
file → your_dataset.csv
```

### Successful response

```json
{
  "success": true,
  "total_customers": 200,
  "clusters": 5,
  "features_used": [
    "Age",
    "Annual Income (k$)",
    "Spending Score (1-100)"
  ],
  "chart_labels": {
    "x": "Age",
    "y": "Annual Income (k$)"
  },
  "segments": [],
  "points": []
}
```

---

## Download Results

### `GET /api/download`

Downloads:

```text
customers_with_segments.csv
```

The exported file contains the original dataset plus:

```text
Segment
Segment Name
```

---

# 💻 Run Locally

## 1. Clone the repository

```bash
git clone https://github.com/Priyanshu710-ui/segmentify-customer-segmentation.git
cd segmentify-customer-segmentation
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run Segmentify

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

# 🎯 Real-World Use Cases

Segmentify can be adapted for:

- 🛍️ **Retail customer analysis**
- 📈 **Marketing campaign targeting**
- 💳 **Customer behavior analysis**
- 🏦 **Financial customer profiling**
- 🛒 **E-commerce personalization**
- 🎁 **Loyalty program segmentation**
- 📊 **Business intelligence demonstrations**
- 🎓 **Machine learning academic projects**

---

# 🧪 Example Workflow

```text
STEP 01  ━━━  Upload customer CSV
STEP 02  ━━━  Segmentify validates numerical features
STEP 03  ━━━  Missing values are processed
STEP 04  ━━━  Features are standardized
STEP 05  ━━━  K-Means discovers customer groups
STEP 06  ━━━  Clusters receive readable labels
STEP 07  ━━━  Dashboard generates insights
STEP 08  ━━━  Download the segmented dataset
```

---

# 🧩 Requirements

The project currently uses:

```text
Flask
flask-cors
pandas
numpy
scikit-learn
```

---

# 🗺️ Future Ideas

- [ ] Automatic optimal `K` selection
- [ ] More clustering algorithms such as DBSCAN and Hierarchical Clustering
- [ ] Authentication and user workspaces
- [ ] Database support
- [ ] Persistent analysis history
- [ ] PDF insight reports
- [ ] More interactive charts
- [ ] Dataset preview before analysis
- [ ] Advanced feature selection controls

---

<div align="center">

## ⭐ If you like this project, give it a star!

**Built with Python + Machine Learning + a lot of ☕**

### 🚀 Turn customer data into decisions.

[![Open Segmentify](https://img.shields.io/badge/OPEN_SEGMENTIFY-→-7C6CFF?style=for-the-badge)](https://segmentify-customer-segmentation-hdq4wvijv-jack-5127.vercel.app)

</div>
