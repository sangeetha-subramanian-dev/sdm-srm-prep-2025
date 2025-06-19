# 🐍 Python List (1D Array) – All Functions with Time Complexity

| Category         | Function               | Description                                | Time Complexity |
|------------------|------------------------|--------------------------------------------|-----------------|
| **Adding**       | `append(x)`            | Add element at the end                     | O(1) amortized  |
|                  | `insert(i, x)`         | Insert x at index i                        | O(n)            |
|                  | `extend(iterable)`     | Add multiple elements                      | O(k), k = len(iterable) |
| **Removing**     | `pop()`                | Remove and return last element             | O(1)            |
|                  | `pop(i)`               | Remove and return element at index i       | O(n)            |
|                  | `remove(x)`            | Remove first occurrence of value x         | O(n)            |
|                  | `clear()`              | Remove all elements                        | O(n)            |
| **Searching**    | `index(x)`             | Return index of first occurrence           | O(n)            |
|                  | `x in lst`             | Membership test                            | O(n)            |
|                  | `count(x)`             | Count occurrences of x                     | O(n)            |
| **Sorting**      | `sort()`               | Sort list in place                         | O(n log n)      |
|                  | `sort(reverse=True)`   | Sort in descending order                   | O(n log n)      |
|                  | `sorted(lst)`          | Return new sorted list                     | O(n log n)      |
| **Reversing**    | `reverse()`            | Reverse list in place                      | O(n)            |
|                  | `reversed(lst)`        | Return reversed iterator                   | O(n)            |
| **Copying**      | `copy()`               | Shallow copy of the list                   | O(n)            |
|                  | `lst[:]`               | Slice (shallow copy)                       | O(n)            |
| **Slicing**      | `lst[a:b:c]`           | Slice with step                            | O(k), k = slice |
| **Built-ins**    | `len(lst)`             | Get number of elements                     | O(1)            |
|                  | `min(lst)`             | Minimum value                              | O(n)            |
|                  | `max(lst)`             | Maximum value                              | O(n)            |
|                  | `sum(lst)`             | Sum of all elements                        | O(n)            |
| **Logical Ops**  | `all(lst)`             | True if all elements are truthy            | O(n)            |
|                  | `any(lst)`             | True if any element is truthy              | O(n)            |
| **Iteration**    | `enumerate(lst)`       | Index-value pairs for iteration            | O(n)            |
|                  | `zip(a, b)`            | Combine iterables element-wise             | O(n)            |
|                  | `map(func, lst)`       | Apply function to all items                | O(n)            |
|                  | `filter(func, lst)`    | Filter items using a condition             | O(n)            |

---

## 🧪 Example Snippets

```python
# Adding
lst.append(10)
lst.insert(2, 5)
lst.extend([1, 2, 3])

# Removing
lst.pop()
lst.pop(2)
lst.remove(10)
lst.clear()

# Searching
lst.index(3)
3 in lst
lst.count(5)

# Sorting & Reversing
lst.sort()
lst.sort(reverse=True)
lst.reverse()
sorted_lst = sorted(lst)
rev = list(reversed(lst))

# Copying & Slicing
copy = lst.copy()
slice = lst[:]
step = lst[::2]

# Built-in & Logical
len(lst)
min(lst)
max(lst)
sum(lst)
all(lst)
any(lst)

# Iteration
for i, val in enumerate(lst):
    print(i, val)

for a, b in zip([1, 2], [3, 4]):
    print(a, b)

list(map(str, lst))
list(filter(lambda x: x > 0, lst))


