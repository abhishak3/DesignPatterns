# Singleton

**Category**: Creational

**Intent**: Ensure a class has only one instance and provide a global point of access to it.

**Problem it solves**: Some resources must be shared consistently across an application (e.g., configuration, logging, connection pools). Multiple instances could cause inconsistent state, race conditions, or resource contention. The Singleton pattern guarantees a single, coordinated instance.

## Conceptual Structure

### Key Participants

- Singleton
  - Holds the single instance
  - Controls instantiation
  - Provides global access method
- Client
  - Requests the instance instead of creating it directly

## UML

<pre>
+------------------+
|    Singleton     |
+------------------+
| - _instance      |
+------------------+
| + get_instance() |
| + business_op()  |
+------------------+

Client ---> Singleton.get_instance()
</pre>

## Collaboration Flow

Client requests the instance.

Singleton checks if an instance already exists.

If not, it creates one.

The same instance is returned for all subsequent requests.

## When NOT to use

When independent instances are needed.

When testability and dependency injection are priorities.

When global state can create tight coupling.
