# solid


https://medium.com/backticks-tildes/the-s-o-l-i-d-principles-in-pictures-b34ce2f1e898


S - Single-responsiblity Principle
O - Open-closed Principle
L - Liskov Substitution Principle
I - Interface Segregation Principle
D - Dependency Inversion Principle


## Single-responsiblity Principle

A class should have one and only one reason to change, meaning that
a class should have only one job.


## Open-closed Principle

Objects or entities should be open for extension but closed for modification.


## Liskov Substitution Principle

Let q(x) be a property provable about objects of x of type T.
Then q(y) should be provable for objects y of type S where S is a subtype of T.

Simply put, if class A is a subtype of class B, we should be able to replace B
with A without disrupting the behavior of our program.


## Interface Segregation Principle

A client should never be forced to implement an interface that it doesn’t use,
or clients shouldn’t be forced to depend on methods they do not use.

The general idea of interface segregation principle is that
it’s better to have a lot of smaller interfaces than a few bigger ones.

Martin explains this principle by advising,
“Make fine grained interfaces that are client-specific.
Clients should not be forced to implement interfaces they do not use.”

For software engineers, this means that you don’t want to just start
with an existing interface and add new methods.

Instead, start by building a new interface and then let your class implement
multiple interfaces as needed.

Smaller interfaces mean that developers should have a preference for
composition over inheritance and for decoupling over coupling.

According to this principle, engineers should work to have many client-specific
interfaces, avoiding the temptation of having one big, general-purpose interface.


## Dependency Inversion Principle

Entities must depend on abstractions, not on concretions.
It states that the high-level module must not depend on the low-level module,
but they should depend on abstractions.

This principle offers a way to decouple software modules.
Simply put, dependency inversion principle means that developers should
“depend on abstractions, not on concretions.”

Martin further explains this principle by asserting that,
“high level modules should not depend upon low level modules.
Both should depend on abstractions.” Further, “abstractions should not depend
on details. Details should depend upon abstractions.”

This way, instead of high-level modules depending on low-level modules,
both will depend on abstractions.


