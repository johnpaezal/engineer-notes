# Production Troubleshooting
*Methodical debugging of live systems*

## Systematic Approach
*Repeatable debugging loop*

**Reproduce** – Confirm and trigger the issue reliably  
**Isolate** – Narrow scope (which service, layer, input, user)  
**Hypothesize** – One falsifiable cause at a time  
**Test** – Change one variable, observe effect  
**Fix** – Apply minimal correct change  
**Verify** – Confirm resolved + no regression  
**Post-mortem** – Document cause, timeline, action items

```
Reproduce → Isolate → Hypothesize → Test → Fix → Verify → Post-mortem
            (binary-search the system, change ONE thing per step)
```

---

## "The Service Is Slow" Answer
*Structured interview response*

```
1. Metrics first (don't guess):
   latency p50 / p95 / p99   → all slow or just tail?
   error rate                → slow because failing/retrying?
   saturation                → CPU, memory, queue depth, conn pool

2. Narrow the layer (binary search the path):
   Load Balancer → App → DB → Downstream/3rd-party
   compare per-layer latency / span durations

3. Drill the slow path:
   traces  → which span dominates (see observability.md)
   logs    → errors/timeouts on that span (filter by trace ID)
   query   → EXPLAIN slow DB query, check missing index
```

**p50 high** – Systemic (all requests) — likely capacity/dependency  
**p99 high only** – Tail — GC pause, lock contention, cold cache, one bad node

---

## USE vs RED
*Which method, when*

(Definitions of metrics/logs/traces live in `observability.md` — here is the method)

| | USE | RED |
|---|---|---|
| Focus | Resources / infrastructure | Services / requests |
| Tracks | Utilization, Saturation, Errors | Rate, Errors, Duration |
| Question | "Is this host/disk healthy?" | "Is this endpoint healthy?" |
| Use when | Suspect a node/resource bottleneck | Suspect a service/endpoint regression |

**Combine** – RED finds the slow service, USE finds the starved resource

---

## Common Issues — First Check
*Symptom → first thing to look at*

| Issue | First thing to check |
|---|---|
| High latency | p99 vs p50, then traces for dominant span |
| Memory leak | Heap trend over time (steady climb, no GC recovery) |
| Connection pool exhausted | Active vs max connections, slow/unclosed queries |
| Thundering herd | Synchronized retries / cache expiry at same instant |
| Cascading failure | Missing timeouts / circuit breakers between services |
| Slow query | `EXPLAIN` plan, missing index, full scan, lock waits |

**Connection pool fix** – Add timeouts, close connections, raise pool sparingly  
**Thundering herd fix** – Jittered backoff, request coalescing, staggered TTL  
**Cascading fix** – Timeouts + circuit breaker + bulkhead isolation

---

## Tracing One Request
*Following a request across services*

**Correlation/Request ID** – ID generated at edge, propagated in headers  
**Header** – `X-Request-ID` / `traceparent` passed to every downstream call  
**Use** – Filter logs of all services by one ID to see full path

### Reading a Stack Trace

```
1. Read top frame   → where it threw (the symptom)
2. Read bottom-up   → your code vs framework/library
3. Find your first  → first frame in your codebase = likely cause
   own frame
4. Check exception  → type + message (NPE, timeout, constraint)
5. "Caused by:"     → unwrap to the root exception (read the last one)
```

---

## Incident Response
*Stop the bleeding, then investigate*

**Mitigate first** – Rollback, scale out, or feature-flag off  
**Then root-cause** – Investigate calmly once impact is contained  
**Blameless post-mortem** – Focus on systems/process, not people

```
Detect → Mitigate (rollback/scale/flag) → Communicate (status)
       → Root-cause → Fix → Post-mortem → Action items
```

**Order matters** – Restoring service > finding the cause

---

## Signal Cheat Sheet
*Which signal first, by bottleneck type*

**CPU-bound** – Run queue / load avg, CPU%, hot threads/flame graph  
**Memory-bound** – Heap/RSS trend, GC frequency & pause, OOM kills  
**IO-bound** – Disk await/utilization, slow queries, fsync latency  
**Network-bound** – Bandwidth, packet loss/retransmits, conn count, DNS

---

## Best Practices

- Look at metrics before forming a hypothesis (don't guess)
- Change one variable at a time, then re-measure
- Propagate a correlation ID through every service
- Mitigate (rollback/flag) before deep root-causing
- Always set timeouts and circuit breakers on remote calls
- Write a blameless post-mortem with concrete action items
- Alert on symptoms (latency, error rate), not causes (CPU)
