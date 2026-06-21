# Automated Marketing ROI Engine

An end-to-end machine learning-driven marketing automation platform that predicts customer value segments, executes targeted campaign actions, and provides real-time analytics for measuring campaign effectiveness and marketing ROI.

## Overview

Modern marketing teams often struggle to identify which customers deserve retention efforts, upsell campaigns, or re-engagement strategies. This project automates that decision-making process by combining machine learning, workflow automation, secure data storage, and business intelligence into a single pipeline.

The system analyzes customer behavioral and transactional data, predicts customer value segments using an XGBoost classification model, automatically triggers segment-specific marketing actions, stores execution logs in MySQL, and visualizes results through a live Streamlit dashboard.

---

## Key Results

* Achieved **94.2% targeting accuracy** using an optimized XGBoost classification model.
* Improved projected marketing ROI by **1.4×** through automated customer segmentation and campaign routing.
* Automated customer lifecycle management using data-driven marketing workflows.
* Integrated machine learning, database persistence, and real-time analytics into a unified system.

---

## Technology Stack

| Category             | Technologies          |
| -------------------- | --------------------- |
| Programming Language | Python                |
| Machine Learning     | XGBoost, Scikit-Learn |
| Data Processing      | Pandas, NumPy         |
| Database             | MySQL                 |
| Dashboard            | Streamlit             |
| Security             | Python-Dotenv         |
| Model Persistence    | Joblib                |

---

## System Architecture

Customer Behavioral Data
→ Feature Engineering
→ XGBoost Classification
→ Customer Segment Prediction
→ Automated Campaign Routing
→ MySQL Logging Layer
→ Streamlit Analytics Dashboard

---

## Machine Learning Pipeline

The prediction engine evaluates customer profiles using a 12-feature behavioral analytics framework:

* Recency
* Frequency
* Monetary Value
* Average Order Value
* Session Count
* Average Session Duration
* Pages Viewed
* Click Activity
* Campaign Response
* Wishlist Additions
* Cart Abandonment Rate
* Product Returns

These features are transformed into a structured input matrix and processed by an XGBoost classifier to determine the most appropriate customer value segment.

---

## Automated Campaign Routing Engine

After customer classification, the automation layer executes personalized marketing actions based on predicted customer value.

Example workflows include:

* Retention incentives for high-value customers
* Premium feature upsell campaigns
* Product engagement and newsletter workflows
* Cart recovery campaigns
* Churn prevention and win-back offers

This simulates how modern marketing automation platforms personalize customer engagement at scale.

---

## Database & Security

The system uses MySQL as the central persistence layer for storing:

* Customer information
* Predicted customer segments
* Executed marketing actions
* Campaign activity logs

Database credentials are securely managed using environment variables through `.env` files, preventing sensitive information from being exposed in source code.

---

## Analytics Dashboard

A Streamlit-powered dashboard provides real-time visibility into system activity, including:

* Customer segment distributions
* Campaign execution tracking
* Marketing workflow monitoring
* Operational metrics and reporting

The dashboard enables users to monitor marketing performance and evaluate the effectiveness of automated segmentation strategies.

---

## Future Improvements

* Deploy routing workflows using AWS Lambda
* Implement real-time event streaming
* Add automated model retraining pipelines
* Integrate campaign A/B testing
* Introduce MLOps monitoring and model drift detection


