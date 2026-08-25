from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

app = Flask(__name__)
CORS(app)


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


# ==========================================
# FRONTEND FILES
# ==========================================

@app.route("/style.css")
def css():
    return send_from_directory(FRONTEND_DIR, "style.css")


@app.route("/script.js")
def js():
    return send_from_directory(FRONTEND_DIR, "script.js")


# ==========================================
# OUTPUT IMAGES
# ==========================================

@app.route("/outputs/<path:filename>")
def output_files(filename):
    return send_from_directory(OUTPUT_DIR, filename)


# ==========================================
# ANALYZE CSV
# ==========================================

@app.route("/api/analyze", methods=["POST"])
def analyze():

    if "file" not in request.files:
        return jsonify({
            "success": False,
            "error": "No CSV file uploaded"
        }), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "error": "Please select a CSV file"
        }), 400

    try:

        df = pd.read_csv(file)

        # Remove completely empty columns
        df = df.dropna(axis=1, how="all")

        # Find numerical columns
        numeric_columns = df.select_dtypes(
            include=["number"]
        ).columns.tolist()

        # Remove ID columns
        feature_columns = [
            col for col in numeric_columns
            if "id" not in col.lower()
        ]

        if len(feature_columns) < 2:
            return jsonify({
                "success": False,
                "error": "Dataset must contain at least 2 numerical columns."
            }), 400

        # Select data for clustering
        X = df[feature_columns].copy()

        # Fill missing values
        X = X.fillna(X.median())

        # Maximum 5 clusters
        n_clusters = min(5, len(df))

        # Scale the data
        scaler = StandardScaler()

        X_scaled = scaler.fit_transform(X)

        # KMeans model
        kmeans = KMeans(
            n_clusters=n_clusters,
            random_state=42,
            n_init=10
        )

        clusters = kmeans.fit_predict(X_scaled)

        # Add segment number
        df["Segment"] = clusters + 1

        # ======================================
        # CREATE SEGMENT NAMES
        # ======================================

        segment_names = {}

        income_col = next(
            (
                col for col in feature_columns
                if "income" in col.lower()
            ),
            None
        )

        spending_col = next(
            (
                col for col in feature_columns
                if "spending" in col.lower()
                or "score" in col.lower()
            ),
            None
        )

        for cluster in range(1, n_clusters + 1):

            cluster_data = df[
                df["Segment"] == cluster
            ]

            averages = cluster_data[
                feature_columns
            ].mean()

            name = f"Customer Group {cluster}"

            if income_col and spending_col:

                overall_income = df[
                    income_col
                ].mean()

                overall_spending = df[
                    spending_col
                ].mean()

                high_income = (
                    averages[income_col]
                    >= overall_income
                )

                high_spending = (
                    averages[spending_col]
                    >= overall_spending
                )

                if high_income and high_spending:
                    name = "High Income, High Spenders"

                elif high_income and not high_spending:
                    name = "High Income, Low Spenders"

                elif not high_income and high_spending:
                    name = "Low Income, High Spenders"

                else:
                    name = "Low Income, Low Spenders"

            segment_names[cluster] = name

        df["Segment Name"] = df[
            "Segment"
        ].map(segment_names)

        # ======================================
        # SEGMENT SUMMARY
        # ======================================

        segments = []

        for cluster in range(1, n_clusters + 1):

            cluster_data = df[
                df["Segment"] == cluster
            ]

            averages = {}

            for col in feature_columns:

                averages[col] = round(
                    float(
                        cluster_data[col].mean()
                    ),
                    2
                )

            segments.append({

                "segment": cluster,

                "name": segment_names[cluster],

                "customers": int(
                    len(cluster_data)
                ),

                "averages": averages

            })

        # ======================================
        # CHART DATA
        # ======================================

        x_col = feature_columns[0]
        y_col = feature_columns[1]

        points = []

        for _, row in df.iterrows():

            points.append({

                "x": float(row[x_col]),

                "y": float(row[y_col]),

                "segment": int(
                    row["Segment"]
                )

            })

        # ======================================
        # SAVE OUTPUT
        # ======================================

        os.makedirs(
            OUTPUT_DIR,
            exist_ok=True
        )

        output_file = os.path.join(
            OUTPUT_DIR,
            "customers_with_segments.csv"
        )

        df.to_csv(
            output_file,
            index=False
        )

        return jsonify({

            "success": True,

            "total_customers": int(
                len(df)
            ),

            "clusters": int(
                n_clusters
            ),

            "features_used": feature_columns,

            "chart_labels": {

                "x": x_col,

                "y": y_col

            },

            "segments": segments,

            "points": points

        })

    except Exception as e:

        return jsonify({

            "success": False,

            "error": str(e)

        }), 500


# ==========================================
# DOWNLOAD RESULT
# ==========================================

@app.route("/api/download")
def download():

    return send_from_directory(

        OUTPUT_DIR,

        "customers_with_segments.csv",

        as_attachment=True

    )


# ==========================================
# RUN SERVER
# ==========================================

if __name__ == "__main__":

    print("=" * 50)
    print("CUSTOMER SEGMENTATION APP")
    print("=" * 50)

    print("App location:", BASE_DIR)
    print("Frontend folder:", FRONTEND_DIR)
    print(
        "Index exists:",
        os.path.exists(
            os.path.join(
                FRONTEND_DIR,
                "index.html"
            )
        )
    )

    print("Output folder:", OUTPUT_DIR)
    print("=" * 50)

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )