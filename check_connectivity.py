import networkx as nx

def is_connected(G):
    """
    Checks if the graph is fully connected.
    
    Args:
        G (networkx.Graph): The graph to check.
        
    Returns:
        bool: True if connected, False otherwise.
    """
    return nx.is_connected(G)