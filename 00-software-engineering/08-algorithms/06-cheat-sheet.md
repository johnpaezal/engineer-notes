# Algorithms Cheat Sheet

## Which Data Structure?
*Pick by access need*

| Need | Use |
|------|-----|
| Fast lookup by key | Hash map (`dict`) |
| Dedup / membership test | `set` |
| LIFO (undo, DFS, parsing) | Stack (`list`) |
| FIFO (BFS, scheduling) | Queue (`deque`) |
| Ordered + range queries | BST / sorted array |
| Index access, mostly append | List / array |
| Frequent insert/delete at ends | Linked list / `deque` |
| Top-K / priority order | Heap (`heapq`) |
| Hierarchy (files, org) | Tree |
| Relationships / networks | Graph |

---

## Pattern Recognition
*Problem clue → pattern*

| Clue in problem | Pattern |
|-----------------|---------|
| Sorted array + pair/triplet | Two pointers |
| Contiguous subarray/substring | Sliding window |
| Linked list cycle / find middle | Fast & slow pointers |
| Many range-sum queries | Prefix sum |
| All combinations/permutations/subsets | Backtracking |
| Overlapping subproblems + optimal | Dynamic programming |
| "Minimize/maximize X such that" | Binary search on answer |
| Sorted input + find element | Binary search |
| Local choice → global optimum | Greedy |
| Shortest path (unweighted) | BFS |
| Connected components / cycles | DFS |
| Top-K / K-th largest | Heap |

---

## Complexity Cheat Sheet
*All structures, key operations*

| Structure | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| Array / list | `O(1)` | `O(n)` | `O(n)` | `O(n)` |
| Hash map / set | — | `O(1)`* | `O(1)`* | `O(1)`* |
| Linked list | `O(n)` | `O(n)` | `O(1)`† | `O(1)`† |
| Stack / queue | — | — | `O(1)` | `O(1)` |
| BST (balanced) | — | `O(log n)` | `O(log n)` | `O(log n)` |
| Heap | `O(1)` min | `O(n)` | `O(log n)` | `O(log n)` |

*average case  †at known node

---

## Interview Checklist
*Steps for every problem*

1. **Clarify input** – Types, size, sorted?, duplicates?, range  
2. **Edge cases** – Empty, single element, duplicates, negatives, overflow  
3. **Brute force first** – State its complexity out loud  
4. **Optimize** – Apply a pattern, justify the trade-off  
5. **State complexity** – Final time and space  
6. **Test with example** – Walk through code with a small input

---

## Must-Know Problems
*Canonical study checklist by pattern*

- [ ] Two Sum (hash map)
- [ ] Valid Palindrome (two pointers)
- [ ] Best Time to Buy/Sell Stock (sliding window / greedy)
- [ ] Longest Substring Without Repeating Chars (sliding window)
- [ ] Valid Parentheses (stack)
- [ ] Merge Two Sorted Lists (linked list)
- [ ] Linked List Cycle (fast & slow)
- [ ] Binary Search (binary search)
- [ ] Invert Binary Tree (tree recursion)
- [ ] Level Order Traversal (BFS)
- [ ] Number of Islands (DFS/BFS grid)
- [ ] Subsets / Permutations (backtracking)
- [ ] Climbing Stairs (DP)
- [ ] Coin Change (DP)
- [ ] Kth Largest Element (heap)
</content>
