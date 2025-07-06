import os
import time
import networkx as nx
import pandas as pd
from grape import Graph  # type: ignore
from grape.embedders import Node2VecSkipGramEnsmallen  # type: ignore


def main():
    print("Starting embedding generation pipeline...")

    # Paths definitions
    script_dir = os.path.dirname(os.path.abspath(__file__))
    edges_path = os.path.join(script_dir, "data", "Gowalla_edges.txt")
    output_path = os.path.join(
        script_dir, "embeddings", "gowalla_node2vec_embeddings.parquet"
    )

    # Data loading
    G = nx.read_edgelist(edges_path, nodetype=int)

    grape_graph = Graph.from_pd(
        edges_df=pd.DataFrame(list(G.edges), columns=["source", "destination"]),
        directed=G.is_directed(),
        edge_src_column="source",
        edge_dst_column="destination",
    )

    # Train Embedding Model
    print("\nTraining Node2Vec model...")
    start_time = time.time()

    node2vec_model = Node2VecSkipGramEnsmallen(
        embedding_size=128,
        walk_length=80,
        iterations=10,
        return_weight=1.0,
        explore_weight=1.0,
        verbose=True,
        enable_cache=True,
    )
    embedding_result = node2vec_model.fit_transform(grape_graph)

    duration = time.time() - start_time
    print(f"\nTraining completed in {duration / 60:.2f} minutes.")

    # Save Results
    node_embeddings_list = embedding_result.get_all_node_embedding()
    central_node_embeddings_df = node_embeddings_list[0]
    central_node_embeddings_df.to_parquet(output_path)

    print(f"Saved embeddings to {output_path}...")


if __name__ == "__main__":
    main()
