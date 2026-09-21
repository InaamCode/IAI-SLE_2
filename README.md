# SLE-2: Empirical Performance Analysis


## 1. AIM :

To experimentally compare the performance of Breadth First Search (BFS) and Depth First Search (DFS) using actual execution time and the number of nodes expanded.

---

## 2. Algorithms Used :

### BFS – Breadth First Search

BFS is an uninformed search algorithm that explores nodes level by level. It uses a queue to manage the nodes waiting to be explored.

### DFS – Depth First Search

DFS is an uninformed search algorithm that explores one path as deeply as possible before backtracking. It uses a stack to manage the nodes during the search.

---

## 3. Problem Configuration :

The same graph was used for both BFS and DFS.

- Number of Nodes: 750
- Start Node: 0
- Goal Node: 749
- Number of Runs: 3
- Algorithms: BFS and DFS

---

## 4. Profiling Method :

The performance of both algorithms was measured using Python's `timeit` module.

The following metrics were measured:

1. Execution time in milliseconds.
2. Number of nodes expanded.
3. Goal-search success.

Each algorithm was executed three times on the same graph. The average execution time was calculated from the three runs.

The number of expanded nodes was counted manually during the search.

---

## 5. Experimental Results :

| Metric | BFS | DFS |
|---|---:|---:|
| Run 1 Time (ms) | 51.55020 | 57.27980 |
| Run 2 Time (ms) | 55.59490 | 47.90890 |
| Run 3 Time (ms) | 65.84880 | 45.99680 |
| Average Time (ms) | 57.66463 | 50.39517 |
| Average Nodes Expanded | 173 | 750 |
| Goal Found | True | True |

---

## 6. Observation :

DFS required less average execution time than BFS in this experiment.

However, BFS expanded significantly fewer nodes (173 nodes) compared to DFS (750 nodes).

---

## 7. Justification and Analysis :

Based on the measured results, BFS was more spatial-efficient, expanding only 173 nodes, whereas DFS expanded all 750 nodes.

The level-by-level exploration of BFS allowed it to locate the goal path after traversing fewer nodes.

The average execution time of DFS was 50.39517 ms, while BFS took 57.66463 ms.

DFS recorded a slightly lower execution time due to simpler stack push/pop operations per iteration.

Both algorithms successfully found the goal node 749.

The comparison is based on actual measurements obtained using the `timeit` method.

Performance may change for a different graph structure or problem size.

---

## 8. Conclusion :

This profiling experiment helped in understanding the practical performance of BFS and DFS.

Execution time and nodes expanded were measured using the same graph for both algorithms.

BFS proved to be much better in terms of nodes expanded, while DFS showed a slightly lower average execution time in this experiment.

The experiment helped demonstrate the importance of empirical profiling along with theoretical analysis.

---

## 9. AI Contribution :

Gemini was used as an assistance tool during the development and documentation of this SLE.

AI assistance included:

- Preparing the BFS and DFS profiling code.
- Setting up execution-time measurement using `timeit`.
- Adding node-counting functionality.
- Organizing the experimental results.
- Assisting with the structure and wording of the SLE-2 report.

The program was executed by the student, and the actual experimental results were collected from the program execution.

---

## 10. Project Files :

- `sle2_profiling_exact.py` – Python implementation of BFS and DFS with profiling.
- `README.md` – Project description, profiling method, and experimental results.
- `AI_Contribution_Log.md` – Detailed record of AI assistance.
- `SLE2_PRN_InaamIqbalMulla.docx` – Final SLE-2 profiling report.

---

## 11. Final Result :

**BFS Average Time:** 57.66463 ms  
**DFS Average Time:** 50.39517 ms  

**BFS Average Nodes Expanded:** 173  
**DFS Average Nodes Expanded:** 750  

**BFS Goal Found:** True  
**DFS Goal Found:** True  

> For this particular graph and experimental setup, BFS expanded fewer nodes, while DFS showed a lower average execution time.