# Page Replacement Algorithm Simulator

A Python simulator for **FIFO**, **LRU** and **Optimal** page replacement (Operating Systems lab project).

**Author:** Shashwat Shandilya | **Roll No.:** BTE25DTA100011

## Features
- User-entered reference string and number of frames, with input validation
- Step-by-step trace table (step, page, frame contents, Hit/Fault, replaced page)
- Page faults, hits, hit ratio and fault ratio for each algorithm
- Final comparison table of all three algorithms
- Belady's anomaly experiment

## How to run
**Jupyter / Colab:** open `BTE25DTA100011_Shashwat_PageReplacement.ipynb`, run all cells, and enter the input when prompted.
**Terminal:** `python page_replacement.py`

## Algorithms
| Algorithm | Victim selection rule |
|---|---|
| FIFO | Page that has been in memory the longest |
| LRU | Page not used for the longest time |
| Optimal | Page used farthest in the future (benchmark only) |

## Sample run
```
Enter page reference string: 1 2 3 1 4 2 5
Enter number of frames: 3
FIFO    -> Faults: 5  Hits: 2  Hit Ratio: 28.57%
LRU     -> Faults: 6  Hits: 1  Hit Ratio: 14.29%
Optimal -> Faults: 5  Hits: 2  Hit Ratio: 28.57%
```

## Results summary
**Part B** (7,0,1,2,0,3,0,4,2,3,0,3,2 with 3 frames)

| Algorithm | Faults | Hits | Hit Ratio |
|---|---|---|---|
| FIFO | 10 | 3 | 23.08% |
| LRU | 9 | 4 | 30.77% |
| Optimal | 7 | 6 | 46.15% |

**Belady's anomaly** (1 2 3 4 1 2 5 1 2 3 4 5)

| Algorithm | Faults (3 frames) | Faults (4 frames) |
|---|---|---|
| FIFO | 9 | 10 |
| LRU | 10 | 8 |
| Optimal | 7 | 6 |

FIFO produces more faults with more frames, which is Belady's anomaly. LRU and Optimal are stack algorithms and never show this behaviour.

## Screenshots

### Code
![Title](Screenshot%202026-10-24%20170857.png)
![FIFO](Screenshot%202026-10-24%20170918.png)
![LRU](Screenshot%202026-10-24%20171011.png)
![Optimal](Screenshot%202026-10-24%20171032.png)
![Input validation code](Screenshot%202026-10-24%20171051.png)
![Output helpers](Screenshot%202026-10-24%20171113.png)

### Sample run (1 2 3 1 4 2 5, 3 frames)
![FIFO sample run](Screenshot%202026-10-24%20171139.png)
![LRU, Optimal and comparison](Screenshot%202026-10-24%20171206.png)

### Part B
![Test cell](Screenshot%202026-10-24%20171400.png)
![FIFO and LRU trace](Screenshot%202026-10-24%20171451.png)
![Optimal trace and comparison](Screenshot%202026-10-24%20171513.png)

### Experiment 1: Belady's anomaly
![Belady's anomaly](Screenshot%202026-10-24%20171530.png)

### Experiment 2: LRU vs FIFO
![Experiment 2](Screenshot%202026-10-24%20171547.png)

### Input validation
![Validation errors](Screenshot%202026-10-24%20171601.png)
