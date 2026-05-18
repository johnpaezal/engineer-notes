# Algorithms Patterns

## Two Pointers
*Two indices move toward a goal*

**When** – Sorted array pair/triplet, palindrome, partitioning

```python
def pair_sum(nums, target):           # sorted input
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target: return (left, right)
        if s < target:  left += 1
        else:            right -= 1
    return None

# Usage: Two Sum II / Valid Palindrome
pair_sum([1, 2, 4, 7], 6)   # (1, 2)
```

---

## Sliding Window
*Move a contiguous range over data*

**When** – Contiguous subarray/substring, max/min/longest of size or condition

```python
def max_sum_size_k(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]   # slide: add new, drop old
        best = max(best, window)
    return best

# Usage: Maximum Subarray of size K / Longest Substring Without Repeating
max_sum_size_k([1, 4, 2, 10, 2], 3)   # 16
```

---

## Fast & Slow Pointers
*Two speeds detect cycles*

**When** – Linked list cycle, find middle, happy number

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

# Usage: Linked List Cycle / Find Middle of List
```

---

## Prefix Sum
*Precompute cumulative totals*

**When** – Many range-sum queries, subarray sum equals K

```python
def build_prefix(nums):
    prefix = [0]
    for n in nums:
        prefix.append(prefix[-1] + n)
    return prefix

def range_sum(prefix, i, j):          # sum nums[i..j] inclusive
    return prefix[j + 1] - prefix[i]

# Usage: Range Sum Query / Subarray Sum Equals K
p = build_prefix([2, 4, 6, 8])
range_sum(p, 1, 2)   # 10
```

---

## Backtracking
*Build candidates, undo on dead end*

**When** – All combinations/permutations/subsets, constraint search

```python
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()                # undo choice
    backtrack(0, [])
    return result

# Usage: Subsets / Permutations / N-Queens
subsets([1, 2])   # [[],[1],[1,2],[2]]
```

---

## Dynamic Programming
*Solve overlapping subproblems once*

**Memoization** – Top-down recursion + cache  
**Tabulation** – Bottom-up table fill  
**When** – Optimal value with overlapping subproblems + optimal substructure  
**Classics** – Fibonacci, climbing stairs, coin change, knapsack, LCS

```python
# Top-down memo (climbing stairs: ways to reach step n)
def climb_memo(n, cache={}):
    if n <= 2: return n
    if n in cache: return cache[n]
    cache[n] = climb_memo(n - 1) + climb_memo(n - 2)
    return cache[n]

# Bottom-up table (same problem)
def climb_table(n):
    if n <= 2: return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Usage
climb_memo(5)    # 8
climb_table(5)   # 8
```

---

## Greedy
*Local optimum → global optimum*

**When** – Choosing best local move provably yields global best  
**Example** – Activity/interval scheduling: pick earliest finishing meeting

```python
def max_meetings(intervals):          # intervals = [(start, end), ...]
    intervals.sort(key=lambda x: x[1])  # earliest end first
    count, last_end = 0, float("-inf")
    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
    return count

# Usage: Non-overlapping Intervals / Jump Game
max_meetings([(1, 3), (2, 4), (3, 5)])   # 2
```

---

## Recursion Essentials
*A function that calls itself*

**Base case** – Stops recursion, returns directly  
**Recursive case** – Reduces problem toward the base case  
**Call stack** – Each call frame stacked; deep recursion → stack overflow  
**Recursion → iteration** – When depth is large or tail-recursive; use explicit stack/loop
</content>
