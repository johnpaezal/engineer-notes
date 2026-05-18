# Algorithms Sorting and Searching

## Binary Search
*Halve sorted range each step*

**Binary search** – Find target in sorted array, `O(log n)`  
**Pitfalls** – `left <= right`, `mid` overflow-safe, update `left = mid + 1` / `right = mid - 1`

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:                 # <= not <  (single-element range)
        mid = left + (right - left) // 2 # avoids overflow, no bias
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1               # mid+1, not mid → no infinite loop
        else:
            right = mid - 1              # mid-1, not mid
    return -1

# Usage
binary_search([1, 3, 5, 7, 9], 7)   # 3
binary_search([1, 3, 5], 4)         # -1
```

---

## Binary Search on Answer
*Search the solution space, not the array*

**Pattern** – "Minimize/maximize X such that `feasible(X)` holds"  
**Idea** – Monotonic predicate → binary search over the answer range  
**Examples** – Min capacity to ship in D days, smallest divisor, Koko eating bananas

```python
def min_feasible(lo, hi, feasible):
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

---

## Sorting Overview
*What each algorithm offers*

| Algorithm | Time | Space | Stable | Use |
|-----------|------|-------|--------|-----|
| Bubble / Insertion | `O(n²)` | `O(1)` | Yes | Teaching only |
| Merge sort | `O(n log n)` | `O(n)` | Yes | Stable, linked lists, external |
| Quicksort | `O(n log n)` avg, `O(n²)` worst | `O(log n)` | No | In-place, fast in practice |
| Timsort (`sorted()`) | `O(n log n)` | `O(n)` | Yes | **What to actually use** |

---

## Merge Sort
*Classic divide and conquer*

**Merge sort** – Split in half, sort each, merge sorted halves

```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:        # <= keeps it stable
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

# Usage
merge_sort([5, 2, 9, 1])   # [1, 2, 5, 9]
```

---

## Practical Python Sorting
*Built-in Timsort, the real tool*

```python
nums = [3, 1, 2]
sorted(nums)                       # [1,2,3] new list
nums.sort()                        # in-place
sorted(nums, reverse=True)         # [3,2,1]

words = ["bb", "a", "ccc"]
sorted(words, key=len)             # ['a','bb','ccc']

people = [("Alice", 30), ("Bob", 25)]
sorted(people, key=lambda p: p[1]) # by age

# Multi-key: by age asc, then name asc
sorted(people, key=lambda p: (p[1], p[0]))
```

---

## Implement vs Use Built-in
*Almost always use built-in*

**Use `sorted()` / `.sort()`** – Production code, interviews unless asked  
**Implement manually** – Only when explicitly asked or custom partial-sort logic  
**Reason** – Timsort is optimized, stable, `O(n log n)`, battle-tested
</content>
