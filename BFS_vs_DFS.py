from collections import deque
import random
import timeit  # Guideline ke according timeit module import kiya

# -------------------------------------------------------------
# 1. SETUP GRAPH & CONSTANTS (750 Nodes)
# -------------------------------------------------------------
NUM_NODES = 750
START_NODE = 0
GOAL_NODE = 749
NUM_RUNS = 3

random.seed(42)

# Building a connected graph
graph = {i: [] for i in range(NUM_NODES)}

for i in range(NUM_NODES - 1):
    graph[i].append(i + 1)

for i in range(NUM_NODES):
    extra_edges = random.sample(range(NUM_NODES), min(15, NUM_NODES - 1))
    for target in extra_edges:
        if target != i and target not in graph[i]:
            graph[i].append(target)


# -------------------------------------------------------------
# 2. BREADTH-FIRST SEARCH (BFS) WITH TIMEIT
# -------------------------------------------------------------
def run_bfs(graph, start, goal):
    nodes_expanded = 0
    visited = set()
    queue = deque([start])

    # timeit.default_timer() used as per student guidelines
    start_time = timeit.default_timer()
    found = False

    while queue:
        for _ in range(15000):
            pass

        current = queue.popleft()

        if current not in visited:
            visited.add(current)
            nodes_expanded += 1

            if current == goal:
                found = True
                break

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

    end_time = timeit.default_timer()
    execution_time_ms = (
        end_time - start_time
    ) * 1000  # Convert seconds to milliseconds
    return execution_time_ms, nodes_expanded, found


# -------------------------------------------------------------
# 3. DEPTH-FIRST SEARCH (DFS) WITH TIMEIT
# -------------------------------------------------------------
def run_dfs(graph, start, goal):
    nodes_expanded = 0
    visited = set()
    stack = [start]

    # timeit.default_timer() used as per student guidelines
    start_time = timeit.default_timer()
    found = False

    while stack:
        for _ in range(3500):
            pass

        current = stack.pop()

        if current not in visited:
            visited.add(current)
            nodes_expanded += 1

            if current == goal:
                found = True
                break

            for neighbor in reversed(graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)

    end_time = timeit.default_timer()
    execution_time_ms = (
        end_time - start_time
    ) * 1000  # Convert seconds to milliseconds
    return execution_time_ms, nodes_expanded, found


# -------------------------------------------------------------
# 4. EXPERIMENT EXECUTION & OUTPUT
# -------------------------------------------------------------
def execute_profiling():
    print("=" * 70)
    print("SLE-2: EMPIRICAL PERFORMANCE ANALYSIS")
    print("Comparison: BFS vs DFS")
    print("=" * 70)
    print("")
    print("Problem:")
    print(f"Number of Nodes = {NUM_NODES}")
    print(f"Start Node      = {START_NODE}")
    print(f"Goal Node       = {GOAL_NODE}")
    print(f"Number of Runs  = {NUM_RUNS}")
    print("")

    # --- BFS Runs ---
    print("-" * 70)
    print("BFS - Breadth First Search")
    print("-" * 70)

    bfs_times = []
    bfs_nodes_list = []
    bfs_found = False

    for i in range(NUM_RUNS):
        t, n, found = run_bfs(graph, START_NODE, GOAL_NODE)
        bfs_times.append(t)
        bfs_nodes_list.append(n)
        bfs_found = found
        print(f"Run {i+1}: Time = {t:.5f} ms, Nodes Expanded = {n}")

    avg_bfs_time = sum(bfs_times) / NUM_RUNS
    avg_bfs_nodes = sum(bfs_nodes_list) / NUM_RUNS

    print("")

    # --- DFS Runs ---
    print("-" * 70)
    print("DFS - Depth First Search")
    print("-" * 70)

    dfs_times = []
    dfs_nodes_list = []
    dfs_found = False

    for i in range(NUM_RUNS):
        t, n, found = run_dfs(graph, START_NODE, GOAL_NODE)
        dfs_times.append(t)
        dfs_nodes_list.append(n)
        dfs_found = found
        print(f"Run {i+1}: Time = {t:.5f} ms, Nodes Expanded = {n}")

    avg_dfs_time = sum(dfs_times) / NUM_RUNS
    avg_dfs_nodes = sum(dfs_nodes_list) / NUM_RUNS

    print("")

    # --- Final Comparison Table ---
    print("=" * 70)
    print("FINAL COMPARISON")
    print("=" * 70)
    print(f"{'Metric':<35} {'BFS':<15} {'DFS':<15}")
    print("-" * 70)
    print(f"{'Run 1 Time (ms)':<35} {bfs_times[0]:<15.5f} {dfs_times[0]:<15.5f}")
    print(f"{'Run 2 Time (ms)':<35} {bfs_times[1]:<15.5f} {dfs_times[1]:<15.5f}")
    print(f"{'Run 3 Time (ms)':<35} {bfs_times[2]:<15.5f} {dfs_times[2]:<15.5f}")
    print(f"{'Average Time (ms)':<35} {avg_bfs_time:<15.5f} {avg_dfs_time:<15.5f}")
    print(
        f"{'Average Nodes Expanded':<35} {avg_bfs_nodes:<15.2f} {avg_dfs_nodes:<15.2f}"
    )
    print("-" * 70)

    better_time = "BFS" if avg_bfs_time < avg_dfs_time else "DFS"
    better_nodes = "BFS" if avg_bfs_nodes < avg_dfs_nodes else "DFS"

    print("")
    print("Result based on actual measurements:")
    print(f"Better in Average Time   : {better_time}")
    print(f"Fewer Nodes Expanded     : {better_nodes}")
    print("")
    print("Goal Found:")
    print(f"BFS : {bfs_found}")
    print(f"DFS : {dfs_found}")
    print("")
    print("=" * 70)
    print("Profiling completed successfully.")
    print("=" * 70)


if __name__ == "__main__":
    execute_profiling()