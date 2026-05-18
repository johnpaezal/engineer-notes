# Python Concurrency

## Overview
*When to use each approach*

**threading** – I/O-bound tasks (network, disk); limited by GIL
**multiprocessing** – CPU-bound tasks; bypasses GIL with separate processes
**asyncio** – I/O-bound with many concurrent tasks; single thread

---

## Threading
*Run I/O tasks concurrently*

```python
import threading
import time

def download(url):
    print(f"Downloading {url}")
    time.sleep(2)               # simulate I/O
    print(f"Done: {url}")

# Usage
urls = ["a.com", "b.com", "c.com"]
threads = [threading.Thread(target=download, args=(url,)) for url in urls]

for t in threads:
    t.start()

for t in threads:
    t.join()    # wait for all to finish
```

### Thread-Safe Shared State
*Prevent race conditions with locks*

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(100)]
for t in threads: t.start()
for t in threads: t.join()

print(counter)  # 100
```

---

## Multiprocessing
*Parallelize CPU-bound work*

```python
from multiprocessing import Pool
import os

def compute(n):
    return n ** 2

# Usage
with Pool(processes=os.cpu_count()) as pool:
    results = pool.map(compute, range(10))

print(results)  # [0, 1, 4, 9, ..., 81]
```

### Process vs Thread
*Choose the right tool*

| | Threading | Multiprocessing |
|--|-----------|-----------------|
| GIL | Limited by it | Bypasses it |
| Memory | Shared | Separate |
| Overhead | Low | Higher |
| Best for | I/O-bound | CPU-bound |

---

## concurrent.futures
*High-level thread/process pool API*

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def fetch(url):
    return f"data from {url}"

urls = ["a.com", "b.com", "c.com"]

# Threads (I/O-bound)
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch, urls))

# Processes (CPU-bound)
with ProcessPoolExecutor() as executor:
    results = list(executor.map(compute, range(10)))
```

---

## asyncio
*Concurrent I/O on a single thread*

> See `advanced/notes.md` for full async/await patterns.

```python
import asyncio

async def fetch(url):
    await asyncio.sleep(1)      # non-blocking I/O
    return f"data from {url}"

async def main():
    results = await asyncio.gather(
        fetch("a.com"),
        fetch("b.com"),
        fetch("c.com"),
    )
    print(results)

asyncio.run(main())
```

---

## Interview Essentials
*Core concurrency questions explained*

### The GIL
*Why threads don't parallelize CPU*

**GIL** – Global Interpreter Lock; one thread runs Python bytecode at a time  
**Effect** – Threads can't use multiple cores for CPU-bound work  
**I/O exception** – GIL released during blocking I/O, so threads help I/O-bound  
**Bypass** – `multiprocessing` (separate interpreters) or C extensions release the GIL  

```python
import time
from threading import Thread

def burn():
    x = 0
    for _ in range(10_000_000):
        x += 1

# Usage
start = time.time()
threads = [Thread(target=burn) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
print(time.time() - start)  # ~same as running 4x serially (GIL serializes)
```

---

### Race Condition
*Unsynchronized access corrupts state*

**Race condition** – Result depends on unpredictable thread interleaving  
**Cause** – `count += 1` is read → add → write (3 steps), not atomic  
**Fix** – Guard the read-modify-write with a lock  

```python
import threading

# BUGGY: lost updates, final value < 1_000_000
counter = 0
def bad():
    global counter
    for _ in range(100_000):
        counter += 1            # read, +1, write — interleaves

# FIXED
lock = threading.Lock()
def good():
    global counter
    for _ in range(100_000):
        with lock:              # atomic section
            counter += 1

# Usage
ts = [threading.Thread(target=good) for _ in range(10)]
for t in ts: t.start()
for t in ts: t.join()
print(counter)  # exactly 1_000_000
```

---

### Lock vs RLock vs Semaphore
*Pick the right synchronization primitive*

**Lock** – Binary mutex; same thread re-acquiring deadlocks  
**RLock** – Reentrant; same thread can acquire N times (release N times)  
**Semaphore** – Counter; allows up to N concurrent holders  
**Event / Condition** – Signal/wait coordination between threads  

```python
import threading

rlock = threading.RLock()       # recursive acquisition OK
def outer():
    with rlock:
        inner()
def inner():
    with rlock:                 # would deadlock with plain Lock
        pass

sem = threading.Semaphore(3)    # max 3 concurrent
def limited():
    with sem:
        pass                    # at most 3 threads here

# Usage
outer()
```

---

### Deadlock — Coffman Conditions
*Four conditions; break one to prevent*

**Mutual exclusion** – Resource held exclusively  
**Hold and wait** – Holds one resource, waits for another  
**No preemption** – Resource only released voluntarily  
**Circular wait** – Cycle of threads each waiting on the next  

```python
import threading

a, b = threading.Lock(), threading.Lock()

# BUGGY: T1 a→b, T2 b→a → circular wait
# FIX: global lock ordering — always acquire a before b
def transfer():
    with a:
        with b:                 # consistent order breaks circular wait
            pass

# Usage — also: timeouts (lock.acquire(timeout=1)) break hold-and-wait
transfer()
```

**Prevention**: lock ordering, `acquire(timeout=...)`, single coarse lock, lock-free structures

---

### Producer-Consumer
*Bounded queue decouples producers*

**`queue.Queue`** – Thread-safe, built-in locking  
**`maxsize`** – Bounds memory; `put` blocks when full (backpressure)  
**Sentinel** – `None` signals consumers to stop  

```python
import threading, queue

q = queue.Queue(maxsize=10)     # bounded buffer

def producer():
    for i in range(20):
        q.put(i)                # blocks if full
    q.put(None)                 # sentinel

def consumer():
    while (item := q.get()) is not None:
        q.task_done()

# Usage
p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start(); c.start()
p.join(); c.join()
```

---

## Best Practices

**GIL** – Use `multiprocessing` for CPU-bound, `threading` for I/O-bound  
**`concurrent.futures`** – Prefer over raw `threading` for simpler code  
**Locks** – Always use `with lock:` to prevent deadlocks  
**`asyncio`** – Best for many concurrent I/O tasks (e.g. web servers)  
**Avoid shared state** – Pass data via queues or return values instead  
