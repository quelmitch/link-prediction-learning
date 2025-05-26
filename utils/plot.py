import matplotlib.pyplot as plt


# Degree Distribution Plot
def degree_distribution_plot(G, logx=False, logy=True):
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees, bins=50)
    plt.title("Degree Distribution")
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    if logy:
        plt.yscale("log")
    if logx:
        plt.xscale("log")
    plt.show()
