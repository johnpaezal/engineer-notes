# Concurrency
*Run code in parallel and manage shared state*

## Threads

```java
// Option 1: extend Thread
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Running in: " + Thread.currentThread().getName());
    }
}

MyThread t = new MyThread();
t.start();   // start (don't call run() directly)

// Option 2: implement Runnable (preferred)
Runnable task = () -> System.out.println("Task running");
Thread t = new Thread(task);
t.start();

// Thread info
Thread.currentThread().getName();   // thread name
Thread.sleep(1000);                 // pause 1 second (throws InterruptedException)
t.join();                           // wait for thread to finish
t.isAlive();                        // is thread running?
```

---

## ExecutorService
*Thread pool — preferred over creating raw threads*

```java
import java.util.concurrent.*;

// Fixed thread pool
ExecutorService executor = Executors.newFixedThreadPool(4);

// Submit tasks
executor.execute(() -> System.out.println("task"));  // fire and forget

Future<Integer> future = executor.submit(() -> {
    return 42;  // returns a result
});

Integer result = future.get();  // blocks until done

// Shutdown (always do this)
executor.shutdown();             // wait for tasks to finish
executor.shutdownNow();          // interrupt running tasks

// Common pool types
Executors.newFixedThreadPool(n);      // n threads
Executors.newCachedThreadPool();      // grows as needed
Executors.newSingleThreadExecutor();  // 1 thread, sequential
Executors.newScheduledThreadPool(n);  // for scheduled tasks
```

---

## Synchronized
*Prevent concurrent access to shared data*

```java
class Counter {
    private int count = 0;

    // synchronized method – only one thread at a time
    public synchronized void increment() {
        count++;
    }

    // synchronized block – finer control
    public void add(int n) {
        synchronized (this) {
            count += n;
        }
    }

    public int getCount() { return count; }
}

// Atomic types (faster than synchronized for simple ops)
import java.util.concurrent.atomic.*;

AtomicInteger counter = new AtomicInteger(0);
counter.incrementAndGet();   // thread-safe ++
counter.addAndGet(5);        // thread-safe +=
counter.get();               // read
```

---

## volatile
*Ensure visibility of variable across threads*

```java
class Worker {
    private volatile boolean running = true;  // visible to all threads

    void stop() {
        running = false;
    }

    void run() {
        while (running) {
            // work...
        }
    }
}
// Use volatile for flags; use synchronized/atomic for compound operations
```

---

## CompletableFuture
*Async programming without blocking*

```java
import java.util.concurrent.*;

// Run async (no return value)
CompletableFuture.runAsync(() -> {
    System.out.println("async task");
});

// Supply async (with return value)
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
    return "result";
});

// Chain operations
CompletableFuture<Integer> result = CompletableFuture
    .supplyAsync(() -> "hello")
    .thenApply(s -> s.length())        // transform result
    .thenApply(n -> n * 2);

result.get();  // 10

// Consume result
future.thenAccept(s -> System.out.println(s));

// Combine two futures
CompletableFuture<String> f1 = CompletableFuture.supplyAsync(() -> "Hello");
CompletableFuture<String> f2 = CompletableFuture.supplyAsync(() -> "World");

f1.thenCombine(f2, (a, b) -> a + " " + b)
  .thenAccept(System.out::println);  // "Hello World"

// Wait for all
CompletableFuture.allOf(f1, f2).join();

// Handle errors
future
    .thenApply(s -> s.toUpperCase())
    .exceptionally(e -> "default on error")
    .thenAccept(System.out::println);
```

---

## Interview Essentials
*Core concurrency questions explained*

### Threads vs Processes
*JVM threading model basics*

**Thread** – Shared heap, cheap, communicates via shared memory  
**Process** – Isolated memory, expensive, communicates via IPC  
**JVM** – Real OS threads, true multicore parallelism (no GIL)  
**When threads** – Almost always in Java; processes only for isolation/crash boundaries  

---

### Race Condition
*Unsynchronized access corrupts state*

**Race condition** – Outcome depends on thread scheduling  
**Why `count++` isn't atomic** – Compiles to read, increment, write (3 ops)  
**Fix** – `synchronized`, `AtomicInteger`, or a `Lock`  

```java
class Counter {
    private int bad = 0;
    void badIncrement() { bad++; }           // lost updates under contention

    private final java.util.concurrent.atomic.AtomicInteger good
        = new java.util.concurrent.atomic.AtomicInteger();
    void goodIncrement() { good.incrementAndGet(); }  // atomic CAS
}

// Usage: 10 threads x 100_000 → good == 1_000_000, bad < that
```

---

### synchronized vs volatile vs Atomic
*Choose the right tool*

| | Visibility | Atomicity | Use for |
|--|-----------|-----------|---------|
| `volatile` | Yes | No | Flags, single read/write |
| `synchronized` | Yes | Yes (block) | Compound operations |
| `AtomicInteger` | Yes | Yes (CAS) | Counters, single var |

**Rule** – `volatile` for visibility only; compound ops need `synchronized`/Atomic  

---

### happens-before
*JMM ordering guarantee*

**happens-before** – If A happens-before B, A's effects visible to B  
**Monitor unlock** – Unlocking a lock happens-before next lock of it  
**volatile write** – happens-before every later read of that field  
**Thread start/join** – `start()` HB thread's run; run HB `join()` return  
**Purpose** – Defines when one thread's writes are visible to another  

---

### Lock vs ReentrantLock vs Semaphore
*Beyond synchronized*

**ReentrantLock** – Explicit lock; supports `tryLock`, timeout, fairness, interruptible  
**ReadWriteLock** – Many readers OR one writer  
**Semaphore** – Permits; bounds N concurrent accessors  
**vs synchronized** – More flexible but must `unlock()` in `finally`  

```java
import java.util.concurrent.locks.ReentrantLock;

ReentrantLock lock = new ReentrantLock();
void critical() {
    if (lock.tryLock()) {            // non-blocking; avoids deadlock
        try { /* work */ }
        finally { lock.unlock(); }   // always release in finally
    }
}

// Usage
java.util.concurrent.Semaphore sem = new java.util.concurrent.Semaphore(3);
sem.acquire();  try { /* max 3 here */ } finally { sem.release(); }
```

---

### Deadlock — Coffman Conditions
*Four conditions; break one to prevent*

**Mutual exclusion** – Resource held exclusively  
**Hold and wait** – Holds one lock, waits for another  
**No preemption** – Lock released only voluntarily  
**Circular wait** – Cycle of threads waiting on each other  

```java
// BUGGY: T1 locks a→b, T2 locks b→a → circular wait
// FIX: global lock ordering — always acquire in the same order
void transfer(Object a, Object b) {
    synchronized (a) {
        synchronized (b) { /* work */ }   // consistent order
    }
}
// Also: tryLock(timeout) breaks hold-and-wait
```

**Prevention**: lock ordering, `tryLock` with timeout, single coarse lock

---

### Producer-Consumer
*BlockingQueue decouples producers*

**`BlockingQueue`** – Thread-safe; `put`/`take` block when full/empty  
**`ArrayBlockingQueue(n)`** – Bounded buffer → backpressure  
**Poison pill** – Sentinel object signals consumers to stop  

```java
import java.util.concurrent.*;

BlockingQueue<Integer> q = new ArrayBlockingQueue<>(10);  // bounded

Runnable producer = () -> {
    try {
        for (int i = 0; i < 20; i++) q.put(i);  // blocks if full
        q.put(-1);                               // poison pill
    } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
};

Runnable consumer = () -> {
    try {
        int item;
        while ((item = q.take()) != -1) { /* process */ }
    } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
};

// Usage
new Thread(producer).start();
new Thread(consumer).start();
```

---

## Best Practices

**ExecutorService** – Prefer pools over raw `new Thread()`; always `shutdown()`  
**`volatile`** – Visibility only; never for compound operations  
**Atomics** – Use for counters/flags instead of `synchronized` when possible  
**Locks** – Always `unlock()` in `finally`; prefer consistent lock ordering  
**Immutability** – Immutable objects are inherently thread-safe  
**`BlockingQueue`** – Use bounded queues for backpressure in producer-consumer  
