import numpy as np
import os
import time
from geometric_graph import geometric_graph
from check_connectivity import is_connected
from pick_sink import pick_sink
from simulate_packets import simulate_packets
from plot_results import plot_results

def run_simulation(n=100, num_rc=10, num_lambda=10, steps=1_000_000):
    """
    Main driver function for the simulation.
    """
    # Define range for connectivity radius (rc)
    # 0.16 is roughly the connectivity threshold for 100 nodes
    rc_values = np.linspace(0.16, 0.40, num_rc)
    
    # Define range for packet generation probability (lambda)
    lambda_values = np.linspace(0.1, 1.0, num_lambda)
    
    # Ensure results directory exists
    if not os.path.exists('results'):
        os.makedirs('results')
    
    print(f"--- Starting Simulation ---")
    print(f"Nodes: {n}, Steps: {steps}")
    print(f"Configurations: {num_rc} Networks x {num_lambda} Lambdas")
    
    start_time = time.time()
    results_count = 0
    
    # --- Outer Loop: Iterate through different Network Topologies (rc) ---
    for rc_idx, rc in enumerate(rc_values):
        print(f"\n[Network {rc_idx+1}/{num_rc}] Generating Graph with rc={rc:.4f}...")
        
        # Try to generate a connected graph (max 100 attempts)
        attempts = 0
        G = None
        positions = None
        
        while attempts < 100:
            G, positions = geometric_graph(n, rc)
            if is_connected(G):
                break
            attempts += 1
        
        if G is None or not is_connected(G):
            print(f"  Warning: Could not create connected graph for rc={rc:.4f}. Skipping.")
            continue
            
        # Select Sink Node
        sink = pick_sink(G)
        sink_degree = G.degree[sink]
        print(f"  Connected! Sink ID: {sink} (Degree: {sink_degree})")
        
        # --- Inner Loop: Iterate through different Traffic Loads (lambda) ---
        for lambd in lambda_values:
            # Run the statistical simulation
            packets, total_received = simulate_packets(G, positions, sink, lambd, steps)
            
            # Define output filename
            filename = f"results/Net{rc_idx+1}_rc{rc:.3f}_lambda{lambd:.2f}.png"
            
            # Generate and save plot
            plot_results(packets, positions, sink, lambd, rc, save_path=filename)
            
            results_count += 1
            
    end_time = time.time()
    print(f"\nSimulation Completed in {end_time - start_time:.2f} seconds.")
    print(f"Generated {results_count} plots in the 'results/' folder.")

if __name__ == "__main__":
    run_simulation()