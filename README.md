# Link Prediction Learning Journey

This repository documents my learning process for performing link prediction using classical machine learning techniques. The current focus is on **binary classification** to predict the existence of an edge between two nodes in a graph.

## Project Goal

The primary goal of this project is to systematically learn and apply various techniques involved in building a link prediction system. This includes:

*   Understanding different graph datasets and their inherent structures.
*   Mastering the use of topological features and knowing when each is most effective.
*   Implementing robust data preprocessing, including train/validation/test splitting and effective negative sampling strategies.
*   Comparing and contrasting different machine learning models for the link prediction task.
*   Evaluating model performance using appropriate metrics and deriving meaningful insights.

## Approach: Iterative Notebooks

This project is structured as a series of Jupyter notebooks, each building upon the knowledge and codebase of the previous one.
Each notebook:
*   Aims to cover a new aspect of link prediction, gradually increasing the complexity of features, models, or evaluation methods.
*   Has a primary learning objective.
*   Introduces a new dataset from [SNAP (Stanford Network Analysis Platform)](https://snap.stanford.edu/data/).

Utility functions for common tasks are progressively refactored into a `utils` directory for better organization and reuse across notebooks.

## Notebooks

1.  **`01_facebook_social_circles`**
    *   **Dataset:** Facebook Social Circles (ego-Facebook)
    *   **Focus:** Introduction to link prediction basics. Explores the critical impact of negative sampling strategies (random vs. common-neighbor based) on model performance using a simple common-neighbor feature.

2.  **`02_scientific_authors_collaboration`**
    *   **Dataset:** Scientific Authors Collaboration (CA-HepTh)
    *   **Focus:** Comparative analysis of various topological features (Common Neighbors, Jaccard, Adamic-Adar, Preferential Attachment, Resource Allocation). Comparison of AUC-ROC and AUC-PR as evaluation metrics, especially with different negative sampling techniques.

3.  **`03_dense_email_network`**
    *   **Dataset:** Email Network (email-Eu-core)
    *   **Focus:** Making a good EDA for topological features and comparing the performance of different binary classification models (e.g., Logistic Regression, SVM, Gradient Boosting) using a robust set of topological features and hard negative sampling.

*(... more notebooks will be added here ...)*
