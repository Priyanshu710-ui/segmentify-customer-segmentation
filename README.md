<div align="center">

# ✦ SEGMENTIFY

### AI-Powered Customer Segmentation Dashboard

**Upload a CSV. Discover patterns. Understand your customers. Make smarter decisions.**

[![Live Demo](https://img.shields.io/badge/🚀_LIVE_DEMO-Try_Segmentify-7C6CFF?style=for-the-badge)](https://segmentify-customer-segmentation-hdq4wvijv-jack-5127.vercel.app)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-K--Means-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Vercel](https://img.shields.io/badge/Deployed_on-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/)

### 👨‍💻 Created by **Priyanshu**

[🚀 Live Demo](https://segmentify-customer-segmentation-hdq4wvijv-jack-5127.vercel.app) · [📦 Repository](https://github.com/Priyanshu710-ui/segmentify-customer-segmentation) · [🐛 Report Bug](https://github.com/Priyanshu710-ui/segmentify-customer-segmentation/issues)

</div>

---

## 🧠 What is Segmentify?

**Segmentify** is an interactive machine-learning web application that automatically groups customers with similar characteristics using **K-Means clustering**.

```text
📄 Upload CSV
      ↓
🔍 Detect numerical features
      ↓
🧹 Handle missing values
      ↓
📏 Standardize data
      ↓
🧠 K-Means clustering
      ↓
🎯 Generate customer segments
      ↓
📊 Insights + ⬇️ Download results
```

The result is a clean dashboard with customer counts, generated clusters, readable segment names, feature averages, visual insights, and a downloadable segmented CSV.

---

# 🚀 Live Demo

<div align="center">

## 👉 [OPEN SEGMENTIFY →](https://segmentify-customer-segmentation-hdq4wvijv-jack-5127.vercel.app)

**Upload your own dataset and run the analysis directly from the browser.**

</div>

---

# ✨ Features

| Feature | What it does |
|---|---|
| 📤 **CSV Upload** | Analyze your own customer dataset. |
| 🔢 **Automatic Feature Detection** | Finds numerical columns and ignores ID-like columns. |
| 🧹 **Missing Value Handling** | Fills missing numerical values using medians. |
| 📏 **Feature Scaling** | Uses `StandardScaler` before clustering. |
| 🧠 **K-Means Clustering** | Groups similar customers automatically. |
| 🎯 **Up to 5 Segments** | Generates up to five clusters based on dataset size. |
| 🏷️ **Smart Segment Names** | Creates readable labels for income/spending datasets. |
| 📊 **Visual Insights** | Shows customer patterns and segmentation results. |
| 📋 **Segment Profiles** | Displays customer counts and feature averages. |
| ⬇️ **Export Results** | Downloads the dataset with generated segments. |
| 🌙 **Premium Dark UI** | Responsive dashboard designed for a polished live demo. |

---

# 🛠️ Tech Stack

```text
╔══════════════════════════════════════════════════╗
║                   SEGMENTIFY                     ║
╠══════════════════════════════════════════════════╣
║ Frontend       HTML • CSS • JavaScript           ║
║ Backend        Python • Flask                    ║
║ Data           Pandas • NumPy                    ║
║ ML             Scikit-learn • K-Means            ║
║ Processing     StandardScaler                     ║
║ Deployment     Vercel                            ║
╚══════════════════════════════════════════════════╝
```

---

# ⚙️ How It Works

### 1️⃣ Upload a dataset

Example:

```csv
CustomerID,Age,Annual Income (k$),Spending Score (1-100)
1,19,15,39
2,21,15,81
3,20,16,6
4,23,16,77
```

Segmentify needs at least **two numerical columns** after ID-like columns are excluded.

### 2️⃣ Prepare the data

- Removes completely empty columns
- Detects numerical features
- Excludes ID-like columns
- Handles missing values with column medians
- Standardizes the selected features

### 3️⃣ Run machine learning

```python
KMeans(
    n_clusters=min(5, len(dataset)),
    random_state=42,
    n_init=10
)
```

### 4️⃣ Generate readable groups

When suitable income and spending columns exist, Segmentify can generate labels such as:

```text
💎 High Income, High Spenders
🧊 High Income, Low Spenders
🔥 Low Income, High Spenders
🌱 Low Income, Low Spenders
```

Otherwise, it uses `Customer Group 1`, `Customer Group 2`, and so on.

---

# 📊 Dashboard Experience

```text
┌─────────────────────────────────────────────┐
│                 SEGMENTIFY                  │
├──────────────────┬──────────────────────────┤
│ Total Customers  │ Customer Segments        │
│ Model            │ Analysis Status          │
└──────────────────┴──────────────────────────┘
                    ↓
          CUSTOMER SEGMENTS
                    ↓
           DATA VISUALIZATION
                    ↓
         DOWNLOAD SEGMENTED CSV
```

---

# 📂 Project Structure

```text
segmentify-customer-segmentation/
│
├── app.py                 # Flask API + ML analysis
├── requirements.txt       # Python dependencies
├── frontend/
│   ├── index.html         # Dashboard structure
│   ├── style.css          # Dark professional UI
│   └── script.js          # Upload + API interaction
├── outputs/               # Generated results
├── data/                  # Dataset resources
├── src/                   # Additional ML modules
├── notebooks/             # Experiments
└── README.md
```

---

# 🔌 API

### `POST /api/analyze`

Send a CSV using multipart form data:

```text
file → your_dataset.csv
```

The response includes total customers, cluster count, features used, segment summaries, chart labels, and data points.

### `GET /api/download`

Downloads:

```text
customers_with_segments.csv
```

The exported dataset includes:

```text
Segment
Segment Name
```

---

# 💻 Run Locally

```bash
git clone https://github.com/Priyanshu710-ui/segmentify-customer-segmentation.git
cd segmentify-customer-segmentation
```

Create and activate a virtual environment, then:

```bash
pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# 🎯 Use Cases

- 🛍️ Retail customer analysis
- 📈 Marketing campaign targeting
- 💳 Customer behavior analysis
- 🏦 Financial customer profiling
- 🛒 E-commerce personalization
- 🎁 Loyalty program segmentation
- 📊 Business intelligence demos
- 🎓 Machine learning academic projects

---

# 🗺️ Future Roadmap

- [ ] Automatic optimal `K` selection
- [ ] DBSCAN and hierarchical clustering
- [ ] Interactive advanced charts
- [ ] Dataset preview before analysis
- [ ] Persistent analysis history
- [ ] PDF insight reports
- [ ] Database support

---

<div align="center">

## ⭐ Like the project?

**Give it a star and try the live demo.**

### 🚀 Turn customer data into decisions.

[![OPEN SEGMENTIFY](https://img.shields.io/badge/OPEN_SEGMENTIFY-→-7C6CFF?style=for-the-badge)](https://segmentify-customer-segmentation-hdq4wvijv-jack-5127.vercel.app)

---

### Made with ❤️ by **Priyanshu**

</div>
