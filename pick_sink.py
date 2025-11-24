import numpy as np

def pick_sink(G):
    """
    Selects the Sink node based on the maximum degree (most neighbors).
    
    Args:
        G (networkx.Graph): The network graph.
        
    Returns:
        int: The ID of the selected sink node.
    """
    degrees = dict(G.degree())
    max_deg = max(degrees.values())
    
    # Find all nodes that share the maximum degree (handling ties)
    candidates = [node for node in G.nodes if degrees[node] == max_deg]
    
    # Randomly select one among the best candidates
    return np.random.choice(candidates)