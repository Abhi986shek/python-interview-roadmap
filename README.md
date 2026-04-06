# Python Roadmap


[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-130_Problems-orange.svg)](https://leetcode.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📊 Repository Stats

- **130 LeetCode Problems** (Easy: 55 | Medium: 50 | Hard: 25)
- **50+ Data Structure Implementations**
- **100% Working Solutions** with test cases
- **Zero Dependencies** - Pure Python

---

## 📁 Repository Structure

```
📁 My Python Playlist/
├── 🎯 LEETCODE/                    # 130 curated interview problems
│   ├── EASY/                       # 55 problems - Build confidence
│   │   ├── ARRAYS/                 # Two pointers, sliding window
│   │   ├── STRINGS/                # Palindromes, anagrams
│   │   ├── LINKED LIST/            # Reverse, merge, cycle detection
│   │   ├── TREES/                  # Traversals, depth, inversion
│   │   └── MATH/                   # Number operations
│   ├── MEDIUM/                     # 50 problems - Core patterns
│   │   ├── ARRAYS/                 # Matrix, intervals, search
│   │   ├── STRINGS/                # Substring, DP on strings
│   │   ├── LINKED LIST/            # Reorder, partition
│   │   ├── TREES/                  # BST, LCA, construction
│   │   ├── GRAPHS/                 # BFS, DFS, topological sort
│   │   ├── DYNAMIC PROGRAMMING/    # Knapsack, subsequence
│   │   └── STACK AND QUEUE/        # Monotonic stack, decode
│   └── HARD/                       # 25 problems - Advanced
│       ├── ARRAYS/                 # Trapping water, median
│       ├── DYNAMIC PROGRAMMING/    # Edit distance, regex
│       ├── TREES/                  # Serialize, max path sum
│       └── GRAPHS/                 # Word ladder, critical edges
│
├── 📚 DATA STRUCTURES AND ALGORITHMS/
│   ├── ARRAYS/                     # Sorting, searching, manipulation
│   ├── LINKED LIST/                # Singly, doubly, circular
│   ├── STACK/                      # Array/linked list implementation
│   ├── QUEUE/                      # Circular, deque, priority
│   ├── TREES/                      # Binary, BST, traversals
│   ├── GRAPHS/                     # BFS, DFS, shortest path
│   ├── HASHING/                    # Hash maps, collision handling
│   ├── HEAP/                       # Min heap, max heap
│   └── STRINGS/                    # Pattern matching, manipulation
│
├── 🔢 NUMBERS/                     # Basic operations
│   ├── factorial.py
│   ├── gcd.py, lcm.py
│   ├── reverse_number.py
│   └── sum_of_numbers.py
│
├── 🎨 PATTERNS/                    # Visual learning
│   ├── triangle_patterns.py
│   ├── pyramid_patterns.py
│   ├── diamond_patterns.py
│   └── heart_pattern.py
│
├── 🔄 RECURSIONS/                  # Recursive implementations
│   ├── factorial_recursion.py
│   ├── fibonacci_recursion.py
│   └── number_operations_recursion.py
│
├── 🎲 NUMBER DETECTORS/            # Special number types
│   ├── armstrong_number.py
│   ├── perfect_number.py
│   ├── prime_operations.py
│   ├── palindrome_number.py
│   └── 10+ more special numbers
│
└── 🔧 MISCELLANEOUS/               # Utility programs
    ├── case_detector.py
    ├── vowel_detector.py
    └── days_in_month.py
```

---

## 📚 Special Numbers Quick Reference

### Armstrong Number
**Definition**: Sum of digits raised to power of digit count equals the number  
**Example**: `153 = 1³ + 5³ + 3³ = 153`  
**Trick**: Only check up to 4 digits (very rare beyond that)

### Perfect Number
**Definition**: Sum of proper divisors (excluding itself) equals the number  
**Example**: `6 = 1 + 2 + 3`  
**Trick**: Check divisors only up to √n for O(√n) complexity

### Prime Number
**Definition**: Only divisible by 1 and itself (greater than 1)  
**Example**: `2, 3, 5, 7, 11, 13`  
**Trick**: After checking 2, only test odd numbers up to √n

### Neon Number
**Definition**: Sum of digits of its square equals the number  
**Example**: `9 → 9² = 81 → 8+1 = 9`  
**Trick**: Extremely rare (only 9 below 10,000)

### Spy Number
**Definition**: Sum of digits equals product of digits  
**Example**: `1124 → sum=8, product=8`  
**Trick**: Must contain 1 or result in 0

### Happy Number
**Definition**: Repeated sum of squares of digits eventually reaches 1  
**Example**: `19 → 1²+9² = 82 → 8²+2² = 68 → ... → 1`  
**Trick**: Use a set to detect cycles (unhappy numbers loop)

### Duck Number
**Definition**: Contains zero but doesn't start with zero  
**Example**: `102, 2050, 7068`  
**Trick**: Simple string check: `'0' in str(n) and not str(n).startswith('0')`

### Automorphic Number
**Definition**: Square ends with the number itself  
**Example**: `25² = 625` (ends with 25)  
**Trick**: Check if `str(n*n).endswith(str(n))`

### Niven/Harshad Number
**Definition**: Divisible by the sum of its digits  
**Example**: `18 → 1+8=9, 18÷9=2 ✓`  
**Trick**: Quick modulo check after digit sum

### Strong Number
**Definition**: Sum of factorials of digits equals the number  
**Example**: `145 = 1! + 4! + 5! = 1 + 24 + 120`  
**Trick**: Pre-compute factorials for digits 0-9

---

## 🧠 Data Structure Decision Guide

### When to Use STACK 📚
**Pattern Recognition:**
- Matching pairs (parentheses, brackets, tags)
- Reverse order needed (undo/redo operations)
- Nested structures
- Expression evaluation
- Backtracking problems

**Keywords**: "balanced", "valid", "matching", "nearest smaller/greater", "most recent"

**Examples**: Valid parentheses, Next greater element, Daily temperatures, Browser history

---

### When to Use QUEUE 🎫
**Pattern Recognition:**
- First-come-first-served processing
- Level-by-level traversal (BFS)
- Sliding window problems (with deque)
- Task scheduling
- Shortest path in unweighted graphs

**Keywords**: "level order", "BFS", "first", "sliding window", "shortest path"

**Examples**: Binary tree level order, Rotting oranges, Sliding window maximum

---

### When to Use HASH MAP/SET 🗂️
**Pattern Recognition:**
- Fast lookup needed O(1)
- Count frequency/occurrences
- Check existence quickly
- Remove duplicates
- Two-sum pattern problems

**Keywords**: "unique", "duplicate", "frequency", "count", "anagram", "pair"

**Examples**: Two sum, Group anagrams, Longest substring without repeating, First non-repeating

---

### When to Use HEAP/PRIORITY QUEUE ⛰️
**Pattern Recognition:**
- Find kth largest/smallest element
- Merge k sorted arrays/lists
- Top k frequent elements
- Running median
- Task scheduling with priority

**Keywords**: "kth", "top k", "largest", "smallest", "median", "merge k", "priority"

**Examples**: Kth largest element, Merge k sorted lists, Top k frequent, Meeting rooms

---

### When to Use TREE 🌳
**Pattern Recognition:**
- Hierarchical data representation
- Fast search in sorted data (BST)
- Range queries
- Prefix matching (Trie)
- Parent-child relationships

**Keywords**: "hierarchy", "parent-child", "sorted order", "prefix", "ancestor"

**Examples**: BST operations, Lowest common ancestor, Serialize/deserialize, Autocomplete

---

### When to Use GRAPH 🕸️
**Pattern Recognition:**
- Network/connection problems
- Shortest path between nodes
- Cycle detection
- Connected components
- Dependency resolution

**Keywords**: "network", "connected", "path", "route", "island", "prerequisite", "cycle"

**Examples**: Number of islands, Course schedule, Word ladder, Clone graph

---

## 🎯 Algorithm Pattern Recognition

### Two Pointers 👉👈
**When to Use**: Sorted arrays, palindrome checks, remove duplicates, container problems

**Template**:
```python
left, right = 0, len(arr) - 1
while left < right:
    if condition:
        # process
        left += 1
    else:
        right -= 1
```

**Problems**: Two sum II, Container with most water, Valid palindrome

---

### Sliding Window 🪟
**When to Use**: Subarray/substring problems, "longest/shortest" with constraint

**Template**:
```python
left = 0
for right in range(len(arr)):
    # expand window
    while condition_violated:
        # shrink window
        left += 1
    # update result
```

**Problems**: Longest substring without repeating, Minimum window substring

---

### Binary Search 🔍
**When to Use**: Sorted array, "find target", search space can be divided

**Template**:
```python
left, right = 0, len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

**Problems**: Binary search, Search in rotated array, Find minimum in rotated

---

### DFS (Depth-First Search) 🏔️
**When to Use**: Tree traversal, backtracking, explore all paths, connected components

**Template**:
```python
def dfs(node):
    if not node:
        return
    # process current node
    dfs(node.left)
    dfs(node.right)
```

**Problems**: Tree traversals, Number of islands, Path sum, Validate BST

---

### BFS (Breadth-First Search) 🌊
**When to Use**: Shortest path (unweighted), level-by-level processing, minimum steps

**Template**:
```python
from collections import deque
queue = deque([start])
visited = {start}
while queue:
    node = queue.popleft()
    for neighbor in get_neighbors(node):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

**Problems**: Binary tree level order, Rotting oranges, Word ladder

---

### Dynamic Programming 💎
**When to Use**: "Maximum/minimum", "count ways", overlapping subproblems

**Template**:
```python
dp = [0] * (n + 1)
dp[0] = base_case
for i in range(1, n + 1):
    dp[i] = transition(dp[i-1], dp[i-2], ...)
```

**Problems**: Climbing stairs, House robber, Coin change, Longest increasing subsequence

---

## ⏱️ Complexity Cheat Sheet

### Common Time Complexities (Best to Worst)
- **O(1)** - Constant: Array access, hash map lookup
- **O(log n)** - Logarithmic: Binary search, balanced tree operations
- **O(n)** - Linear: Single loop, linear search
- **O(n log n)** - Linearithmic: Merge sort, heap sort
- **O(n²)** - Quadratic: Nested loops, bubble sort
- **O(2ⁿ)** - Exponential: Recursive fibonacci (no memo)
- **O(n!)** - Factorial: Generate all permutations

### Data Structure Operations

| Structure | Access | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Stack | O(n) | O(n) | O(1) | O(1) | O(n) |
| Queue | O(n) | O(n) | O(1) | O(1) | O(n) |
| Hash Map | - | O(1)* | O(1)* | O(1)* | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) | O(n) |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Heap | - | O(n) | O(log n) | O(log n) | O(n) |

*Average case; worst case O(n) due to collisions

### Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

---



