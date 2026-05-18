# Algorithms Trees and Graphs

## Binary Tree & BST
*Hierarchical node structure*

**Binary tree** – Each node has up to 2 children (left, right)  
**BST** – Left subtree < node < right subtree (ordering property)  
**Height** – Longest root-to-leaf path; **depth** – distance from root  
**Balanced** – Height `O(log n)` → fast ops; **skewed** – degrades to `O(n)`

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bst_insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = bst_insert(root.left, value)
    else:
        root.right = bst_insert(root.right, value)
    return root

# Usage
root = bst_insert(None, 5)
bst_insert(root, 3)        # goes left; lookup is O(log n) if balanced
```

---

## Tree Traversals
*Visit every node once*

**Inorder** – Left, node, right (BST → sorted order)  
**Preorder** – Node, left, right (copy/serialize tree)  
**Postorder** – Left, right, node (delete tree, evaluate expression)  
**Level-order** – Breadth by levels (BFS with `deque`)

```python
from collections import deque

def inorder(node):
    if not node: return
    inorder(node.left); print(node.value); inorder(node.right)

def level_order(root):
    if not root: return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value)
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)

# Usage
inorder(root)        # ascending values for a BST
level_order(root)    # top-down, left-to-right
```

---

## Graph Representations
*How edges are stored*

| Aspect | Adjacency list | Adjacency matrix |
|--------|----------------|------------------|
| Space | `O(V + E)` | `O(V²)` |
| Edge exists? | `O(degree)` | `O(1)` |
| Iterate neighbors | `O(degree)` | `O(V)` |
| Best for | Sparse graphs (most cases) | Dense graphs |

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
}   # adjacency list — default choice
```

---

## BFS
*Level-by-level, shortest path unweighted*

**BFS** – Explore neighbors before going deeper, uses queue  
**Use** – Shortest path in unweighted graph, level info

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

# Usage
bfs(graph, "A")   # {'A','B','C','D'} — visits closest nodes first
```

---

## DFS
*Go deep before backtracking*

**DFS** – Follow a path fully, then backtrack  
**Recursive** – Uses call stack; **iterative** – explicit stack  
**Use** – Cycle detection, connected components, path existence, topological sort

```python
def dfs_recursive(graph, node, visited=None):
    if visited is None: visited = set()
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

def dfs_iterative(graph, start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    return visited

# Usage
dfs_recursive(graph, "A")   # {'A','B','C','D'}
```

---

## BFS vs DFS & Advanced
*Pick the right traversal*

**Use BFS** – Shortest path (unweighted), minimum steps, level order  
**Use DFS** – Path existence, cycles, components, backtracking, topological sort  

**Dijkstra** – Shortest path with weighted edges (priority queue); see `09-system-design/`  
**Topological sort** – Linear ordering of a DAG (task scheduling, build order)
</content>
