# Customer Persona Segmenter – Dataset & EDA

## My Contribution

This part of the project focuses on **Dataset Preparation and Exploratory Data Analysis (EDA)** for the Customer Persona Segmentation project.

## Objective

The main objective of this work is to prepare the customer dataset and understand the data before applying machine learning.

The dataset contains customer information based on:

- Annual Income
- Spending Score

## Dataset Preparation

The customer dataset is generated using:


dataset_unsupervised.py
The generated dataset is saved as:
customers.csv
Dataset Checking
The following checks were performed on the dataset:
- Displayed the first 5 records.
- Checked the dataset shape.
- Checked column names.
- Checked dataset information.
- Checked missing values.
- Checked duplicate records.
- Generated statistical summary.

Exploratory Data Analysis
EDA was performed to understand the distribution and relationship between the customer features.
The following visualizations were created:
1. Annual Income Distribution
A histogram was created to understand how the annual income of customers is distributed.
File:
visualizations/income_distribution.png
2. Spending Score Distribution
A histogram was created to understand the distribution of customer spending scores.
File:
visualizations/spending_distribution.png
3. Annual Income vs Spending Score
A scatter plot was created to understand the relationship between annual income and spending score.
File:
visualizations/income_vs_spending.png

EDA Findings
The EDA helped us understand the following:
- Customer annual income varies across the dataset.
- Spending scores are distributed across different levels.
- Customers with similar income can have different spending scores.
- The scatter plot shows different patterns of customers based on income and spending behavior.
- The dataset is suitable for further customer segmentation analysis.
Files Added by Member 1
customers.csv
dataset_unsupervised.py
EDA.py
EDA_Findings.txt
visualizations/
├── income_distribution.png
├── spending_distribution.png
└── income_vs_spending.png
Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

My Role
Role: Dataset & EDA
Responsibilities:
- Generate customer dataset
- Check and prepare the dataset
- Perform data quality checks
- Perform Exploratory Data Analysis
- Create data visualizations
- Document EDA findings
- Provide the prepared dataset for the next stage of the project

Handoff
The prepared customers.csv dataset and EDA results are provided for the next stage of the project, where the data will be used for customer segmentation.
