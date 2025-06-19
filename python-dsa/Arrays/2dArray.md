# 🧩 Python 2D Array (List of Lists) – All Operations with Time Complexity

| Category        | Operation / Function                       | Description                                          | Time Complexity |
|----------------|---------------------------------------------|------------------------------------------------------|-----------------|
| **Create**      | `[[0]*n for _ in range(m)]`                | Initialize m x n 2D array with zeros                 | O(m * n)        |
| **Access**      | `arr[i][j]`                                | Access element at row i, column j                    | O(1)            |
| **Update**      | `arr[i][j] = val`                          | Update value at row i, column j                      | O(1)            |
| **Append Row**  | `arr.append(new_row)`                      | Add a new row to the end                             | O(1)            |
| **Append Col**  | `arr[i].append(x)`                         | Add new element to row i                             | O(1) amortized  |
| **Insert Row**  | `arr.insert(i, new_row)`                   | Insert a row at position i                           | O(m)            |
| **Insert Col**  | `arr[i].insert(j, x)`                      | Insert element x at column j of row i                | O(n)            |
| **Remove Row**  | `arr.pop(i)`                               | Remove row at index i                                | O(m) worst      |
| **Remove Col**  | `arr[i].pop(j)`                            | Remove element at column j from row i                | O(n)            |
| **Slice Copy**  | `[row[:] for row in arr]`                  | Deep copy a 2D array                                 | O(m * n)        |
| **Flatten**     | `[x for row in arr for x in row]`          | Convert 2D array into 1D                             | O(m * n)        |
| **Transpose**   | `list(map(list, zip(*arr)))`               | Transpose rows and columns                          | O(m * n)        |
| **Search**      | `target in row` inside nested loop         | Search element in entire matrix                      | O(m * n)        |
| **Row Traversal**| `for row in arr`                          | Iterate over all rows                                | O(m)            |
| **Element-wise**| `for i in range(m) for j in range(n)`      | Iterate every element in nested loop                 | O(m * n)        |

---

## 🧪 Example Snippets

```python
# Create 3x3 grid
grid = [[0 for _ in range(3)] for _ in range(3)]

# Access and update
val = grid[1][2]
grid[0][1] = 5

# Append and insert
grid.append([7, 8, 9])
grid[0].append(10)
grid.insert(1, [11, 12, 13])
grid[0].insert(0, 99)

# Remove
grid.pop()         # remove last row
grid[1].pop(2)     # remove element at col 2 of row 1

# Deep copy
copy_grid = [row[:] for row in grid]

# Flatten
flat = [x for row in grid for x in row]

# Transpose
transposed = [list(row) for row in zip(*grid)]

# Search
for row in grid:
    if 5 in row:
        print("Found")

