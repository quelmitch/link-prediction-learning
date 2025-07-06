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
    *   **Focus:** Advanced EDA; Hyperparameter tuning for Random Forest on a link prediction task, understanding the impact of different hyperparameters, and using techniques like Grid Search or Randomized Search with Cross-Validation.


4.  **`04_facebook_social_circles_v2`**
    *   **Dataset:** Facebook Social Circles (ego-Facebook)
    *   **Focus:** Integrating node-level features with scaled Logistic Regression; optimizing via basic hyperparameter tuning.

5. **05_gowalla**
   * **Dataset:** Gowalla
   * **Focus**: A comprehensive, real-world link prediction pipeline, introducing:
     * Temporal Dynamics: Using a time-based split to predict future links based on past data.
     * Large-Scale Data Handling: Applying efficient EDA and sampling techniques suitable for a larger graph.
     * Node Embedding: Training Node2Vec to automatically learn feature representations from the graph structure.
     * Advanced Feature Engineering: Combining topological features, engineered node attributes (from geographic check-in data), and learned embeddings.
     * Model Comparison: Evaluating and comparing baseline models with more powerful ensemble models.

*(... more notebooks will be added here ...)*

## Personal Observations
1. I realized after the hyperparameters tuning done in the notebook `03` could have been done better in a later notebook. However, even if the work done is rough and the performance gains are not large, the learning process is indeed valuable and led to a better understanding of Cross-Validation and Random Forests.
2. While being in notebook `04`, i noticed the existence of the `feature_importances_` attribute for Random Forests that would have been really useful in notebook `03`. In fact, after testing it i discovered that the features [aa, ra, pa] would have scored higher than [jc, ra, pa] that i used, because aa had more importance than jc.
