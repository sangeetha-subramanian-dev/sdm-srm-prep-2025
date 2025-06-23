# 🐍 Python List – All Operations with Time Complexity

| Category         | Operation / Function          | Description                                   | Time Complexity |
|------------------|-------------------------------|-----------------------------------------------|-----------------|
| **Create**       | `lst = [0] * n`               | Create a list with n zeros                    | O(n)            |
|                  | `list(range(n))`              | Create list of n sequential numbers           | O(n)            |
| **Access**       | `lst[i]`                      | Access element at index i                     | O(1)            |
| **Update**       | `lst[i] = x`                  | Update value at index i                       | O(1)            |
| **Append**       | `lst.append(x)`               | Add element to end                            | O(1) amortized  |
| **Insert**       | `lst.insert(i, x)`            | Insert x at index i                           | O(n)            |
| **Extend**       | `lst.extend([x, y])`          | Add multiple elements                         | O(k), k = len() |
| **Pop**          | `lst.pop()`                   | Remove and return last element                | O(1)            |
|                  | `lst.pop(i)`                  | Remove element at index i                     | O(n)            |
| **Remove**       | `lst.remove(x)`               | Remove first occurrence of value x            | O(n)            |
| **Delete**       | `del lst[i]`                  | Delete element at index i                     | O(n)            |
|                  | `lst.clear()`                 | Delete all elements                           | O(n)            |
| **Search**       | `x in lst`                    | Membership test                               | O(n)            |
|                  | `lst.index(x)`                | Index of first occurrence                     | O(n)            |
|                  | `lst.count(x)`                | Count occurrences of x                        | O(n)            |
| **Sort**         | `lst.sort()`                  | Sort list in-place                            | O(n log n)      |
|                  | `sorted(lst)`                 | Return sorted list (new)                      | O(n log n)      |
| **Reverse**      | `lst.reverse()`               | Reverse list in-place                         | O(n)            |
|                  | `list(reversed(lst))`         | Return reversed list                          | O(n)            |
| **Slice**        | `lst[:]`, `lst[a:b:c]`        | Copy or partial list                          | O(k)            |
| **Copy**         | `lst.copy()`                  | Shallow copy                                  | O(n)            |
| **Length**       | `len(lst)`                    | Length of list                                | O(1)            |
| **Aggregate**    | `sum(lst)`                    | Sum of elements                               | O(n)            |
|                  | `min(lst)`, `max(lst)`        | Min or max value                              | O(n)            |
| **Comprehension**| `[x for x in lst]`            | Create list using comprehension               | O(n)            |
| **Map/Filter**   | `list(map(...))`              | Transform list                                | O(n)            |
|                  | `list(filter(...))`           | Filter list                                   | O(n)            |
| **Enumerate**    | `enumerate(lst)`              | Index + value iterator                        | O(n)            |
| **Zip**          | `zip(lst1, lst2)`             | Combine lists                                  | O(n)            |

---

## 🧪 Example Snippets

```python
# Create
lst = [0] * 5
lst = list(range(5))

# Access / Update
x = lst[2]
lst[2] = 99

# Add
lst.append(10)
lst.insert(1, 20)
lst.extend([30, 40])

# Remove
lst.pop()
lst.pop(1)
lst.remove(30)
del lst[0]
lst.clear()

# Search
5 in lst
lst.index(99)
lst.count(10)

# Sorting / Reversing
lst.sort()
lst.sort(reverse=True)
reversed_lst = list(reversed(lst))
lst.reverse()

# Slice / Copy
copy = lst[:]
copy2 = lst.copy()
slice = lst[1:4]

# Aggregates
len(lst)
sum(lst)
min(lst)
max(lst)

# Comprehension, map, filter
squared = [x**2 for x in lst]
mapped = list(map(str, lst))
filtered = list(filter(lambda x: x > 10, lst))

# Enumerate / Zip
for i, val in enumerate(lst):
    print(i, val)

zipped = list(zip([1, 2], [3, 4]))
