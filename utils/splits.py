import networkx as nx
import numpy as np
import random

random.seed(42)


def create_train_test_split(
    G, build_feature_dataset, negative_sampling_fun, test_ratio=0.2
):
    # Split Positive Edges
    edges = list(G.edges())
    random.shuffle(edges)
    split_idx = int((1 - test_ratio) * len(edges))
    train_edges = edges[:split_idx]
    test_edges = edges[split_idx:]

    # Create training graph
    G_train = nx.Graph()
    G_train.add_nodes_from(G.nodes())
    G_train.add_edges_from(train_edges)

    # Split Negative Edges
    negative_edges = negative_sampling_fun()
    negative_edges = list(negative_edges)
    random.shuffle(negative_edges)
    neg_train_edges = negative_edges[:split_idx]
    neg_test_edges = negative_edges[split_idx:]

    # Combined Positive + Negative (Train)
    X_train_pos = build_feature_dataset(train_edges, G_train)
    X_train_neg = build_feature_dataset(neg_train_edges, G_train)
    X_train = X_train_pos + X_train_neg
    y_train = np.concatenate([np.ones(len(X_train_pos)), np.zeros(len(X_train_neg))])

    # Combined Positive + Negative (Test)
    X_test_pos = build_feature_dataset(test_edges, G_train)
    X_test_neg = build_feature_dataset(neg_test_edges, G_train)
    X_test = X_test_pos + X_test_neg
    y_test = np.concatenate([np.ones(len(X_test_pos)), np.zeros(len(X_test_neg))])

    return X_train, X_test, y_train, y_test
