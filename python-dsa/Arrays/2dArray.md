# 🧠 NumPy 2D Array – All Operations with Time Complexity

| Category         | Operation / Function                | Description                                      | Time Complexity |
|------------------|--------------------------------------|--------------------------------------------------|-----------------|
| **Create**       | `np.zeros((m, n))`                  | Create m x n array filled with 0s               | O(m * n)        |
|                  | `np.ones((m, n))`                   | Create m x n array filled with 1s               | O(m * n)        |
|                  | `np.full((m, n), val)`              | Create m x n array filled with `val`            | O(m * n)        |
|                  | `np.arange().reshape(m, n)`         | Create m x n with sequential values             | O(m * n)        |
| **Access**       | `arr[i, j]`                         | Access element at row i, col j                  | O(1)            |
| **Update**       | `arr[i, j] = val`                   | Update value at i, j                            | O(1)            |
| **Insert**       | `np.insert(arr, i, row, axis=0)`    | Insert row at index i                           | O(m * n)        |
|                  | `np.insert(arr, j, col, axis=1)`    | Insert column at index j                        | O(m * n)        |
| **Delete**       | `np.delete(arr, i, axis=0)`         | Delete row i                                    | O(m * n)        |
|                  | `np.delete(arr, j, axis=1)`         | Delete column j                                 | O(m * n)        |
|                  | `np.delete(arr, k)`                 | Delete element k in flattened array             | O(m * n)        |
| **Append**       | `np.append(arr, row, axis=0)`       | Append row to array                             | O(m * n)        |
|                  | `np.append(arr, col, axis=1)`       | Append column to array                          | O(m * n)        |
| **Flatten**      | `arr.flatten()`                     | Convert 2D → 1D array                           | O(m * n)        |
| **Transpose**    | `arr.T` or `np.transpose(arr)`      | Transpose rows and columns                      | O(m * n)        |
| **Reshape**      | `arr.reshape((n, m))`               | Change shape                                    | O(1)* (view)    |
| **Copy**         | `arr.copy()`                        | Deep copy of array                              | O(m * n)        |
| **Stacking**     | `np.vstack([a, b])`                 | Vertical stack                                  | O(m * n)        |
|                  | `np.hstack([a, b])`                 | Horizontal stack                                | O(m * n)        |
| **Search**       | `np.where(arr == x)`                | Find indices where value == x                   | O(m * n)        |
| **Masking**      | `arr[arr > x]`                      | Boolean mask                                    | O(m * n)        |
| **Sum/Mean**     | `arr.sum(axis=0)` / `.mean()`       | Aggregation                                     | O(m * n)        |

> \* `reshape` is O(1) when it returns a view, O(n) if it copies data.
