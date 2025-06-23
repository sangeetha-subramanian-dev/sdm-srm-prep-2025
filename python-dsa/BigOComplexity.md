# 📚 Common Data Structure Operations

This document summarizes the **time and space complexity** of common operations across widely used data structures.

---

## 📊 Time & Space Complexity — Common Data Structures

### 1. 🧱 Array

#### 📊 Time & Space Complexity 

| Operation                    | Time Complexity | Space Complexity | Notes                                                             |
|-----------------------------|------------------|------------------|-------------------------------------------------------------------|
| Access (by index)           | O(1)             | O(1)             | Direct index-based access                                         |
| Search (unsorted array)     | O(n)             | O(1)             | Linear search through all elements                                |
| Search (sorted array)       | O(log n)         | O(1)             | Binary search (if sorted)                                         |
| Insert at end (append)      | O(1) *amortized* | O(1)             | Python lists have dynamic arrays with resizing                    |
| Insert at beginning/middle  | O(n)             | O(1)             | Needs shifting of elements                                        |
| Delete at end               | O(1)             | O(1)             | No shifting required                                              |
| Delete at beginning/middle  | O(n)             | O(1)             | Needs shifting of elements                                        |
| Traversal (e.g., loop)      | O(n)             | O(1)             | Visit each element once                                           |
| Resize (dynamic array)      | O(n)             | O(n)             | Python dynamically resizes underlying array                       |
| Copy array                  | O(n)             | O(n)             | New memory allocation required                                    |
| Space to store `n` elements | —                | O(n)             | Required for all elements                                         |
---

### 2. 📚 Stack (LIFO)

| Operation   | Time (Avg) | Time (Worst) | Space |
|-------------|------------|---------------|--------|
| Access      | Θ(n)       | O(n)          | O(n)   |
| Search      | Θ(n)       | O(n)          | O(n)   |
| Insertion   | Θ(1)       | O(1)          | O(n)   |
| Deletion    | Θ(1)       | O(1)          | O(n)   |

---

### 3. 🚶 Queue (FIFO)

| Operation   | Time (Avg) | Time (Worst) | Space |
|-------------|------------|---------------|--------|
| Access      | Θ(n)       | O(n)          | O(n)   |
| Search      | Θ(n)       | O(n)          | O(n)   |
| Insertion   | Θ(1)       | O(1)          | O(n)   |
| Deletion    | Θ(1)       | O(1)          | O(n)   |

---

### 4. 🔗 Singly Linked List

| Operation   | Time (Avg) | Time (Worst) | Space |
|-------------|------------|---------------|--------|
| Access      | Θ(n)       | O(n)          | O(n)   |
| Search      | Θ(n)       | O(n)          | O(n)   |
| Insertion   | Θ(1)       | O(1)          | O(n)   |
| Deletion    | Θ(1)       | O(1)          | O(n)   |

---

### 5. 🔁 Doubly Linked List

| Operation   | Time (Avg) | Time (Worst) | Space |
|-------------|------------|---------------|--------|
| Access      | Θ(n)       | O(n)          | O(n)   |
| Search      | Θ(n)       | O(n)          | O(n)   |
| Insertion   | Θ(1)       | O(1)          | O(n)   |
| Deletion    | Θ(1)       | O(1)          | O(n)   |


---

✅ *Useful for interviews, algorithm analysis, and system design discussions.*

