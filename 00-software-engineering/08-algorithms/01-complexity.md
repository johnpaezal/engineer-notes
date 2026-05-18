# Algorithms Complexity

## Big-O Notation
*Growth rate as input grows*

**Big-O** – Upper bound on time/space as `n → ∞`  
**Why it matters** – Predicts scalability, compares algorithms hardware-independently  
**Drop constants** – `O(2n) → O(n)`, `O(n/2) → O(n)`  
**Drop non-dominant terms** – `O(n² + n) → O(n²)`

```python
def has_duplicate(items):
    seen = set()              # O(n) space
    for item in items:        # O(n) time
        if item in seen:      # O(1) avg lookup
            return True
        seen.add(item)
    return False

# Usage
has_duplicate([1, 2, 3, 2])  # True  → O(n) time, O(n) space
```

---

## Common Complexities
*Ordered slowest-growing to fastest*

| Big-O | Name | Example operation |
|-------|------|-------------------|
| `O(1)` | Constant | Dict lookup, array index |
| `O(log n)` | Logarithmic | Binary search |
| `O(n)` | Linear | Single loop over list |
| `O(n log n)` | Linearithmic | Merge sort, `sorted()` |
| `O(n²)` | Quadratic | Nested loop, bubble sort |
| `O(2ⁿ)` | Exponential | Naive recursive Fibonacci |
| `O(n!)` | Factorial | Generating all permutations |

---

## Time vs Space
*Two independent cost dimensions*

**Time complexity** – How operations grow with input size  
**Space complexity** – Extra memory used (excludes input itself)  
**Trade-off** – Often spend memory (cache/hash) to save time

```python
# Time-heavy, space-light: recompute each time → O(n²) time, O(1) space
# Space-heavy, time-light: memoize results → O(n) time, O(n) space
```

---

## Analyzing a Function
*Map code shape to Big-O*

**Single loop** – `O(n)`  
**Nested loop** – `O(n²)` (or `O(n·m)` for two inputs)  
**Sequential loops** – Added then dominant kept: `O(n)`  
**Halving each step** – `O(log n)`  
**Recursion** – `O(branches^depth)`; recurrence intuition below

```python
# T(n) = 2·T(n/2) + O(n)  → O(n log n)   (merge sort: 2 calls, half size, linear merge)
# T(n) = T(n-1) + O(1)    → O(n)         (linear recursion)
# T(n) = 2·T(n-1) + O(1)  → O(2ⁿ)        (naive fibonacci: 2 calls, n-1)
```

---

## Amortized Complexity
*Average cost per operation over a sequence*

**Amortized** – Worst-case averaged across many operations  
**Dynamic array append** – Occasional `O(n)` resize, `O(1)` amortized  
**Hash map insert** – Occasional rehash, `O(1)` amortized

```python
items = []
for i in range(1000):
    items.append(i)   # mostly O(1); doubling resize is rare → O(1) amortized

# Usage
# 1000 appends ≈ O(1000) total, not O(1000²)
```

---

## Best / Average / Worst Case
*Performance depends on input shape*

**Best case** – Most favorable input (e.g. already sorted)  
**Average case** – Expected over random inputs  
**Worst case** – Adversarial input; the one to quote in interviews

**Quicksort** – Best/avg `O(n log n)`, worst `O(n²)` (bad pivot on sorted data)  
**Binary search** – Best `O(1)` (mid hit), worst `O(log n)`

---

## Python Operations Reference
*Common structure operation costs*

| Operation | list | dict / set | str |
|-----------|------|-----------|-----|
| Index `x[i]` | `O(1)` | — | `O(1)` |
| Lookup `x in y` | `O(n)` | `O(1)` avg | `O(n)` |
| Append / add | `O(1)` amort. | `O(1)` avg | immutable |
| Insert / delete middle | `O(n)` | `O(1)` avg (by key) | — |
| Concatenation | `O(n)` | — | `O(n)` |
| Iterate | `O(n)` | `O(n)` | `O(n)` |

**Rule** – Membership test: prefer `set`/`dict` (`O(1)`) over `list` (`O(n)`)
</content>
</invoke>
