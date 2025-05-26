import random
from re import error
import networkx as nx

random.seed(42)

#### Easy Negative Sampling ####


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


#### Hard Negative Sampling ####


# Top N (desc by number of neighbors) non-connected node pairs that have common neighbors and are at distance=2. Randomly Sampled.
def common_neighbors_hard_negative_sampling(G, negative_samples_ratio=1):
    if not G.edges:
        raise Exception("Graph with no edges")

    positive_set_size = len(list(G.edges()))
    target_num_negatives = int(positive_set_size * negative_samples_ratio)

    nodes = list(G.nodes())

    if len(nodes) < 3:
        raise Exception("Not enough nodes")

    candidate_non_edges = {}

    # Heuristic to prevent too long runs
    max_candidates_to_find = target_num_negatives * 5
    max_attempts = max_candidates_to_find * 10

    for _ in range(max_attempts):
        if len(candidate_non_edges) >= max_candidates_to_find:
            break

        u = random.choice(nodes)
        if G.degree(u) == 0:
            continue

        w = random.choice(list(G.neighbors(u)))
        if G.degree(w) <= 1:
            continue

        potential_v_nodes = list(G.neighbors(w))
        random.shuffle(potential_v_nodes)

        for v in potential_v_nodes:
            if v != u and not G.has_edge(u, v):
                pair = tuple(sorted((u, v)))
                if pair not in candidate_non_edges:
                    cn_count = len(list(nx.common_neighbors(G, u, v)))
                    if cn_count > 0:
                        candidate_non_edges[pair] = cn_count
                break

    # Sort candidates by common neighbors (descending)
    sorted_candidates = sorted(
        candidate_non_edges.items(), key=lambda item: item[1], reverse=True
    )

    # Take the top N
    hard_negatives = set(
        pair for pair, count in sorted_candidates[:target_num_negatives]
    )

    if len(hard_negatives) < target_num_negatives / 2:
        raise Exception("Not enough hard negatives found")

    return hard_negatives
