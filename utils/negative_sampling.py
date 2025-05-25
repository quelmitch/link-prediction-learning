import random
import networkx as nx

random.seed(42)


# Random Negative Sampling
def random_negative_sampling(G, negative_samples_ratio=1):
    positive_set = set(tuple(sorted(link)) for link in list(G.edges))

    negative_candidates = set()
    negative_set_size = int(len(positive_set) * negative_samples_ratio)

    node_list = list(G.nodes())

    while len(negative_candidates) < negative_set_size:
        u, v = random.sample(node_list, 2)
        pair = tuple(sorted((u, v)))

        if not G.has_edge(u, v) and pair not in negative_candidates:
            negative_candidates.add(pair)

    return negative_candidates


# Common-Neighbors Negative Sampling
# A simpler implementation that takes just the top k node pairs with most common neighbors without a link between them.
def top_common_neighbors_negative_sampling(G, negative_samples_ratio=1):
    positive_set = set(tuple(sorted(link)) for link in list(G.edges))

    non_edges_with_scores = []
    nodes = list(G.nodes())

    for i, u in enumerate(nodes):
        for v_idx in range(i + 1, len(nodes)):
            v = nodes[v_idx]
            pair = tuple(sorted((u, v)))

            if not G.has_edge(u, v):
                common_ns_count = len(list(nx.common_neighbors(G, u, v)))
                non_edges_with_scores.append((pair, common_ns_count))

    # Sort by common neighbors (descending) and take top-K
    non_edges_with_scores.sort(key=lambda x: x[1], reverse=True)
    negative_set_size = int(len(positive_set) * negative_samples_ratio)

    top_pairs = non_edges_with_scores[:negative_set_size]
    return set(pair for pair, _ in top_pairs)
