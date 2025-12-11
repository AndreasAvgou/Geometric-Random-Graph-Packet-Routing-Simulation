# Packet Routing Simulation

This project implements a comprehensive simulation of packet routing in wireless sensor networks modeled as random geometric graphs. The simulation explores how network connectivity (radius `rc`) and packet generation probability (lambda `λ`) affect packet forwarding patterns and network performance.


📂 Project Structure

## Features

- **Random Geometric Graph Generation**: Creates connected networks with variable connectivity radius
- **Connectivity Verification**: Ensures all generated networks are connected before simulation
- **Sink Node Selection**: Automatically selects the most central node (highest degree) as the sink
- **Packet Simulation**: Simulates packet generation and multihop routing using shortest paths
- **Statistical Analysis**: Tracks packet forwarding activity per node
- **Visualization**: Generates scatter plots showing relationship between node distance and packet forwarding

## Project Structure

```

├── main.py                    # Main execution script
├── geometric_graph.py         # Random geometric graph generation
├── check_connectivity.py      # Network connectivity verification
├── pick_sink.py               # Sink node selection algorithm
├── simulate_packets.py        # Packet routing simulation engine
├── plot_results.py            # Result visualization
└── README.md                  # This file
```

## Installation

### Prerequisites

- Python 3.7 or higher
- NumPy
- NetworkX
- Matplotlib

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/geometric-graph-simulation.git
cd geometric-graph-simulation
```

2. Install dependencies:
```bash
pip install numpy networkx matplotlib
```

## Usage

Run the main simulation:

```bash
python main.py
```

### Configuration

You can modify simulation parameters directly in `main.py`:

```python
run_simulation(
    n=100,           # Number of nodes
    num_rc=10,       # Number of different rc values to test
    num_lambda=10,   # Number of different lambda values to test
    steps=1000000    # Number of simulation time steps
)
```

## Parameters

- **n**: Number of nodes in the network (default: 100)
- **rc**: Connectivity radius (values from ~0.15 to √2 ≈ 1.414)
- **λ (lambda)**: Packet generation probability per time step (0 < λ ≤ 1)
- **steps**: Number of simulation time steps (default: 1,000,000)

## Output

The script creates a **results/** folder containing 100 scatter plots (PNG).

   - X-axis: Euclidean distance of each node from sink
   - Y-axis: Number of packets forwarded by that node
   - Sink node appears at distance 0 with total packets received

## File Descriptions

### geometric_graph.py
Creates random geometric graphs with nodes randomly positioned in a unit square and edges based on Euclidean distance threshold.

### check_connectivity.py
Verifies that a graph is connected using NetworkX built-in functionality.

### pick_sink.py
Selects the sink node by identifying nodes with maximum degree.

### simulate_packets.py
Core simulation engine that:
- Computes shortest paths from all nodes to sink
- Simulates packet generation and routing
- Tracks forwarding statistics

### plot_results.py
Generates scatter plots visualizing packet forwarding vs. distance from sink.

### main.py
Orchestrates the entire simulation pipeline:
- Iterates through rc and lambda values
- Creates networks and runs simulations
- Saves results and statistics

## Performance Notes

The simulation with default parameters (10 rc values × 10 lambda values × 1,000,000 steps) may take several minutes to complete depending on your system. For faster testing, reduce the `steps` parameter or number of rc/lambda values.

## License

This project is provided as-is for educational purposes.

## Contact

For questions or issues, please open an issue on GitHub.

## References

- NetworkX Documentation: https://networkx.org/
- Random Geometric Graphs: IEEE Transactions on Information Theory
- Wireless Sensor Networks: Routing Algorithms and Protocols
