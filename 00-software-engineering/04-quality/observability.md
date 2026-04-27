# Observability
*Understanding what your system is doing in production*

## The Three Pillars
*Core components of observability*

**Logs** – Timestamped records of discrete events  
**Metrics** – Numerical measurements over time  
**Traces** – End-to-end journey of a request through services

```
Logs    → "What happened?" (events, errors, actions)
Metrics → "How much / how fast?" (latency, error rate, CPU)
Traces  → "Where did it happen?" (which service, which function)
```

---

## Logs
*Structured records of events*

### Log Levels

**DEBUG** – Detailed info for debugging (dev only)  
**INFO** – Normal operation events  
**WARNING** – Unexpected but not critical  
**ERROR** – Something failed, needs attention  
**CRITICAL** – System is unusable

```python
import logging

logger = logging.getLogger(__name__)

logger.debug("Processing item %s", item_id)
logger.info("User %s logged in", user_id)
logger.warning("Retry attempt %d for order %s", attempt, order_id)
logger.error("Payment failed for order %s: %s", order_id, error)
logger.critical("Database connection lost")
```

### Structured Logging
*Log as JSON for easy querying*

```python
import structlog

log = structlog.get_logger()

log.info("order.created",
    order_id=order.id,
    user_id=order.user_id,
    total=order.total,
    items_count=len(order.items)
)
# Output: {"event": "order.created", "order_id": 42, "user_id": 7, ...}
```

```
❌ Unstructured: "Order 42 created by user 7 for $99.00"
✅ Structured:   {"event": "order.created", "order_id": 42, "user_id": 7, "total": 99.00}
```

---

## Metrics
*Numerical data over time*

### Metric Types

**Counter** – Only goes up (requests, errors, logins)  
**Gauge** – Can go up or down (CPU%, memory, active connections)  
**Histogram** – Distribution of values (response times, request sizes)

```python
# Prometheus metrics example
from prometheus_client import Counter, Histogram, Gauge

request_count = Counter("http_requests_total", "Total requests", ["method", "endpoint"])
request_duration = Histogram("http_request_duration_seconds", "Request duration")
active_connections = Gauge("active_connections", "Current active connections")

# Usage
request_count.labels(method="GET", endpoint="/users").inc()
active_connections.set(42)

with request_duration.time():
    response = process_request()
```

### Key Metrics to Track

```
RED Method (for services):
  Rate     → requests per second
  Errors   → % of failed requests
  Duration → response time (p50, p95, p99)

USE Method (for infrastructure):
  Utilization  → CPU/memory/disk %
  Saturation   → queue length, waiting
  Errors       → error rate
```

---

## Traces
*Following a request across services*

**Trace** – Full journey of one request (start to finish)  
**Span** – One operation within a trace (DB query, API call)  
**Trace ID** – Unique ID that links all spans of a request

```
Request: POST /checkout

Trace ID: abc-123
├── Span: API Gateway          (5ms)
├── Span: OrderService         (120ms)
│   ├── Span: validate_cart    (10ms)
│   ├── Span: DB query         (45ms)
│   └── Span: PaymentService   (65ms)
│       └── Span: Stripe API   (60ms)
└── Span: NotificationService  (8ms)

Total: 133ms
Bottleneck: Stripe API call
```

---

## Tools

### Logging
**ELK Stack** – Elasticsearch + Logstash + Kibana (search and visualize logs)  
**CloudWatch Logs** – AWS native log storage and search  
**Loki + Grafana** – Lightweight log aggregation

### Metrics
**Prometheus** – Metrics collection and storage  
**Grafana** – Visualization dashboards  
**CloudWatch Metrics** – AWS native metrics  
**Datadog** – SaaS full observability platform

### Tracing
**Jaeger** – Open source distributed tracing  
**Zipkin** – Open source tracing  
**AWS X-Ray** – AWS native distributed tracing  
**OpenTelemetry** – Standard SDK for all three pillars

---

## Alerting
*Getting notified when things go wrong*

```
Alert conditions:
  Error rate > 1% for 5 minutes
  P99 latency > 2 seconds
  CPU > 85% for 10 minutes
  Disk > 90% full
  Service health check failing

Alert channels:
  PagerDuty → on-call engineer (critical)
  Slack     → team channel (warning)
  Email     → non-urgent
```

---

## Best Practices

- Log at the right level (don't log everything as ERROR)
- Never log passwords, tokens, or PII
- Include correlation/trace ID in every log line
- Set up dashboards before you need them, not after an incident
- Alert on symptoms (high error rate), not causes (CPU spike)
- Define SLOs (Service Level Objectives) and alert when at risk
