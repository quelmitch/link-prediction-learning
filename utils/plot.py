import matplotlib.pyplot as plt
import networkx as nx


def degree_count_plot(G, logy=True):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees, bins=50)
    plt.title("Degree Distribution")
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    if logy:
        plt.yscale("log")
    plt.show()


def degree_distribution_plot(G):
    if not G.nodes():
        return

    degree_counts = nx.degree_histogram(G)

    degrees = []
    probabilities = []
    total_nodes = G.number_of_nodes()

    for degree, count in enumerate(degree_counts):  # type: ignore
        if degree > 0 and count > 0:
            degrees.append(degree)
            probabilities.append(count / total_nodes)

    plt.figure(figsize=(8, 6))
    plt.scatter(degrees, probabilities)

    plt.title("Degree Distribution (PMF) - Log-Log Scale")
    plt.xlabel("Degree (k)")
    plt.ylabel("P(k)")

    plt.xscale("log")
    plt.yscale("log")

    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.tight_layout()
    plt.show()
