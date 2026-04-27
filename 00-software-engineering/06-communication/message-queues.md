# Message Queues & Event-Driven Architecture
*Decoupling services through asynchronous messaging*

## Why Message Queues
*Problems they solve*

```
Without queues (synchronous):
  OrderService ──► EmailService ──► (waits 2 seconds) ──► returns

Problems:
  - OrderService blocked waiting for email
  - If EmailService is down, order fails
  - Spike in orders overwhelms EmailService

With queues (asynchronous):
  OrderService ──► Queue ──► returns immediately
                      ↓
               EmailService processes at its own pace
```

**Decoupling** – Services don't need to know about each other  
**Resilience** – Messages persist even if consumer is down  
**Scalability** – Add more consumers when queue grows

---

## Core Concepts
*Key terms in messaging*

**Producer** – Service that sends messages  
**Consumer** – Service that receives and processes messages  
**Queue** – Buffer that stores messages until consumed  
**Message** – Unit of data sent through the queue  
**Broker** – The message queue system (SQS, RabbitMQ, Kafka)

---

## Messaging Patterns

### Point-to-Point (Queue)
*One producer, one consumer per message*

```
Producer ──► [Queue] ──► Consumer A
                    (message deleted after consumed)
```

**Use** – Tasks that should be processed once (send email, process payment)

### Pub/Sub (Topic)
*One producer, many consumers*

```
Producer ──► [Topic] ──► Consumer A (email service)
                    ├──► Consumer B (analytics service)
                    └──► Consumer C (audit service)
```

**Use** – Events that multiple services care about (user.registered, order.placed)

### Fan-Out
*One message triggers multiple queues*

```
SNS Topic ──► SQS Queue 1 ──► Email Service
         ├──► SQS Queue 2 ──► SMS Service
         └──► SQS Queue 3 ──► Push Notification
```

---

## Event-Driven Architecture
*System where components communicate through events*

**Event** – Something that happened: `order.placed`, `user.registered`  
**Event-driven** – Services react to events instead of calling each other directly

```
Traditional (synchronous):
OrderService.placeOrder()
  → calls EmailService.sendConfirmation()
  → calls InventoryService.decrementStock()
  → calls AnalyticsService.trackPurchase()

Event-driven (asynchronous):
OrderService.placeOrder()
  → publishes event: order.placed {order_id, user_id, items}
  → returns immediately

EmailService      ←subscribes── order.placed → sends email
InventoryService  ←subscribes── order.placed → updates stock
AnalyticsService  ←subscribes── order.placed → tracks metric
```

---

## Popular Brokers

### Amazon SQS
*Simple, managed queue (AWS)*

```
Type: Point-to-point queue
Retention: up to 14 days
Delivery: at-least-once
Ordering: Standard (best-effort) or FIFO (guaranteed order)
Use: Task queues, decoupling AWS services
```

### Amazon SNS
*Simple notification service — pub/sub (AWS)*

```
Type: Pub/Sub topic
Subscribers: SQS, Lambda, HTTP, email, SMS
Use: Fan-out pattern, notifications
```

### RabbitMQ
*Feature-rich message broker*

```
Type: Queue + pub/sub
Protocols: AMQP
Features: Routing, dead letter queues, priorities
Use: Complex routing logic, on-premise
```

### Apache Kafka
*High-throughput event streaming*

```
Type: Distributed log / event stream
Retention: Configurable (messages not deleted after consume)
Throughput: Millions of messages/second
Ordering: Guaranteed within partition
Use: Event sourcing, analytics pipelines, audit logs, high volume
```

---

## Dead Letter Queue (DLQ)
*Handling failed messages*

**DLQ** – Separate queue for messages that failed processing repeatedly

```
Normal Queue ──► Consumer processes message
                 │
                 └── fails 3 times ──► Dead Letter Queue
                                            ↓
                                    Alert + manual review
```

---

## Key Concepts

**At-least-once delivery** – Message delivered minimum once (may duplicate)  
**Exactly-once delivery** – Message delivered exactly once (harder, use FIFO)  
**Idempotency** – Processing same message twice = same result as once  
**Backpressure** – Slow consumers signal producers to slow down

```python
# Idempotent consumer example
def process_order(order_id):
    # Check if already processed (idempotency key)
    if db.exists(f"processed:order:{order_id}"):
        return  # skip duplicate

    # Process
    fulfill_order(order_id)

    # Mark as processed
    db.set(f"processed:order:{order_id}", True)
```

---

## Best Practices

- Design consumers to be idempotent (at-least-once delivery is common)
- Always configure a Dead Letter Queue
- Monitor queue depth (growing = consumers too slow)
- Use FIFO queues only when order is critical (lower throughput)
- Keep messages small — put large data in S3, send reference in message
- Set message retention long enough to survive consumer downtime
