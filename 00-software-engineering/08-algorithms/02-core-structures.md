# Algorithms Core Structures

## Arrays / Lists
*Contiguous indexed sequence*

**Array** – Contiguous memory, `O(1)` index by position  
**Insert/delete middle** – `O(n)` (shifts elements)  
**When to use** – Need ordered access by index, mostly append

```python
nums = [10, 20, 30]
nums[1]              # O(1) access → 20
nums.append(40)      # O(1) amortized
nums.pop()           # O(1) end
nums.insert(0, 5)    # O(n) shifts all
nums.pop(0)          # O(n) shifts all
30 in nums           # O(n) linear scan

# Usage
total = sum(nums)    # O(n) iterate
```

---

## Hash Map / Dict
*Key → value, average O(1) access*

**Hash map** – Hashes key to bucket, `O(1)` avg lookup/insert  
**Collision** – Two keys same bucket; resolved by chaining  
**Degrades to `O(n)`** – Many collisions / poor hash distribution  
**When to use** – Fast lookup by key, counting, dedup

```python
from collections import Counter

freq = Counter("banana")             # {'a':3,'b':1,'n':2} frequency count
unique = set([1, 2, 2, 3])           # {1,2,3} dedup
index = {"alice": 1, "bob": 2}       # O(1) lookup by key
"alice" in index                     # O(1) avg membership

# Usage
most_common = freq.most_common(1)    # [('a', 3)]
```

---

## Linked List
*Nodes connected by pointers*

**Linked list** – Each node holds value + pointer to next  
**Singly** – One forward pointer  
**Doubly** – Forward + backward pointers  
**Vs array** – `O(1)` insert/delete at known node, but `O(n)` access, no cache locality  
**When to use** – Frequent insert/delete at ends, unknown size, LRU cache

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev

# Usage
head = Node(1, Node(2, Node(3)))
new_head = reverse(head)   # 3 → 2 → 1
```

---

## Stack (LIFO)
*Last in, first out*

**Stack** – Push/pop at one end, `O(1)` both  
**When to use** – Undo, DFS, parsing, expression/bracket matching, call stack

```python
stack = []
stack.append("a")     # push
stack.append("b")
top = stack.pop()      # "b"  → LIFO

# Usage: balanced brackets
def is_balanced(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif not stack or stack.pop() != pairs[ch]:
            return False
    return not stack
```

---

## Queue (FIFO)
*First in, first out*

**Queue** – Enqueue at back, dequeue at front  
**`deque`** – `O(1)` both ends; `list.pop(0)` is `O(n)` (avoid)  
**When to use** – BFS, task scheduling, producer-consumer buffers

```python
from collections import deque

queue = deque()
queue.append("a")        # enqueue
queue.append("b")
first = queue.popleft()  # "a"  → FIFO, O(1)

# Usage
queue = deque([1, 2, 3])
while queue:
    process = queue.popleft()
```
</content>
