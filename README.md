# DesignPatterns

Different Design Patterns implemented using Python

In software engineering, when we talk about design pattern categories, we usually refer to the classic Gang of Four (GoF) classification. These 23 foundational patterns are grouped into three main categories based on their primary purpose

The "Gang of Four" (GoF) refers to the four authors: Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides—who wrote the seminal 1994 book Design Patterns: Elements of Reusable Object-Oriented Software. In this book, they cataloged 23 fundamental design patterns that solve common software design problems.

To make these patterns easier to understand and apply, the GoF distributed them into three main categories based on their primary purpose: Creational, Structural, and Behavioral.

Here is the breakdown of how the 23 patterns are distributed across these three categories:

## Creational Patterns (5 Patterns)

Creational patterns abstract the instantiation process. They help make a system independent of how its objects are created, composed, and represented. Instead of creating objects directly using new, these patterns give your program more flexibility in deciding which objects need to be created for a given use case.

**Singleton**: Ensures a class has only one instance and provides a global point of access to it.

**Factory Method**: Defines an interface for creating an object, but lets subclasses decide which class to instantiate.

**Abstract Factory**: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

**Builder**: Separates the construction of a complex object from its representation, allowing the same construction process to create various representations.

**Prototype**: Specifies the kinds of objects to create using a prototypical instance, and creates new objects by copying this prototype.

## Structural Patterns (7 Patterns)

Structural patterns are concerned with how classes and objects are composed to form larger structures. They use inheritance to compose interfaces or implementations, and they help ensure that when one part of a system changes, the entire structure doesn't need to be reworked.

**Adapter**: Converts the interface of a class into another interface clients expect. It lets classes work together that couldn't otherwise because of incompatible interfaces.

**Bridge**: Decouples an abstraction from its implementation so that the two can vary independently.

**Composite**: Composes objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly.

**Decorator**: Attaches additional responsibilities to an object dynamically. It provides a flexible alternative to subclassing for extending functionality.

**Facade**: Provides a unified interface to a set of interfaces in a subsystem. It defines a higher-level interface that makes the subsystem easier to use.

**Flyweight**: Uses sharing to support large numbers of fine-grained objects efficiently (minimizing memory usage).

**Proxy**: Provides a surrogate or placeholder for another object to control access to it.

## Behavioral Patterns (11 Patterns)

Behavioral patterns are specifically concerned with communication between objects. They abstract the control flow, shifting focus away from how objects are constructed toward how they interact and distribute responsibilities.

**Chain of Responsibility**: Passes a request along a chain of handlers. Upon receiving a request, each handler decides either to process it or to pass it to the next handler in the chain.

**Command**: Encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

**Interpreter**: Given a language, defines a representation for its grammar along with an interpreter that uses the representation to evaluate sentences in the language.

**Iterator**: Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

**Mediator**: Defines an object that encapsulates how a set of objects interact. It promotes loose coupling by keeping objects from referring to each other explicitly.

**Memento**: Without violating encapsulation, captures and externalizes an object's internal state so that the object can be restored to this state later.

**Observer**: Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

**State**: Allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

**Strategy**: Defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

**Template Method**: Defines the skeleton of an algorithm in an operation, deferring some steps to subclasses. It lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.

**Visitor**: Represents an operation to be performed on the elements of an object structure. It lets you define a new operation without changing the classes of the elements on which it operates.
