import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv("customers.csv")


# ============================================================
# 2. BASIC DATASET INFORMATION
# ============================================================

print("===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns)

print("\n===== DATASET INFORMATION =====")
df.info()

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())


# ============================================================
# 3. CREATE VISUALIZATION FOLDER
# ============================================================

os.makedirs("visualizations", exist_ok=True)


# ============================================================
# 4. ANNUAL INCOME DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

sns.histplot(
    df["annual_income_k"],
    bins=20,
    kde=True,
    color="skyblue"
)

plt.title("Annual Income Distribution")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Number of Customers")
plt.tight_layout()

plt.savefig("visualizations/income_distribution.png")
plt.show()


# ============================================================
# 5. SPENDING SCORE DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

sns.histplot(
    df["spending_score"],
    bins=20,
    kde=True,
    color="salmon"
)

plt.title("Spending Score Distribution")
plt.xlabel("Spending Score")
plt.ylabel("Number of Customers")
plt.tight_layout()

plt.savefig("visualizations/spending_distribution.png")
plt.show()


# ============================================================
# 6. ANNUAL INCOME VS SPENDING SCORE
# ============================================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="annual_income_k",
    y="spending_score",
    color="purple",
    alpha=0.7
)

plt.title("Annual Income vs Spending Score")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

plt.savefig("visualizations/income_vs_spending.png")
plt.show()


print("\n===== EDA COMPLETED SUCCESSFULLY =====")
print("Visualizations saved in the 'visualizations' folder.")
