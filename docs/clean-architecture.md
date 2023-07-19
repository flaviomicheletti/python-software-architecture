# Clean Architecture

- https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html

Clean Architecture is a software design philosophy introduced by Robert C. 
Martin, also known as Uncle Bob. It provides a set of principles and 
guidelines for creating modular, maintainable, and testable software systems. 
The goal of Clean Architecture is to separate the core business logic of an 
application from the specific implementation details, such as frameworks, 
databases, or user interfaces. 

![](./imgs/clean-architecture.jpg)

Clean Architecture emphasizes the following key principles: 

1. **Independence of Frameworks**: The innermost and most essential parts of 
the system, often referred to as the "core" or "domain" layer, should be 
independent of any external frameworks or libraries. This allows the core 
business logic to remain stable and reusable, even if the frameworks or 
technologies change. 

2. **Separation of Concerns**: The architecture promotes dividing the system 
into distinct layers, with each layer having a specific responsibility. The 
most common layers include the Presentation layer (UI), Application layer (
business logic), Domain layer (core business logic), and Infrastructure 
layer (external dependencies like databases or APIs). Each layer has clear 
boundaries and dependencies flow inward, toward the core. 

3. **Dependency Rule**: The dependencies between the layers follow a specific 
pattern called the Dependency Rule. It states that dependencies should only 
flow inward, from the outer layers to the inner layers. In other words, the 
inner layers should not know anything about the outer layers. This rule 
ensures that the core business logic remains decoupled and can be easily 
tested and modified without affecting other parts of the system. 

4. **Testability**: Clean Architecture promotes high testability by allowing 
easy isolation and testing of each layer independently. Since the core 
business logic is separated from the external dependencies and frameworks, 
unit tests can be written without any reliance on specific technologies. This 
makes it easier to write automated tests and maintain the codebase's overall 
stability. 

5. **Use Cases and Entities**: Clean Architecture encourages the use of use 
cases and entities as central components of the system. Use cases represent 
the application-specific actions or behaviors that encapsulate the business 
rules, while entities represent the core business objects and concepts. By 
focusing on these components, the architecture prioritizes the business logic 
over the technical implementation details. 

Clean Architecture is technology-agnostic and can be applied to various 
programming languages and frameworks. It promotes a modular and flexible 
design, making it easier to evolve and maintain software systems over time. 
By enforcing clear boundaries and focusing on the core business logic, Clean 
Architecture can lead to codebases that are easier to understand, extend, and 
refactor. 
