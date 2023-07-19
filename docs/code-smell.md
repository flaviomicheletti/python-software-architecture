# Code smells

- https://www.linkedin.com/feed/update/urn:li:activity:7076499492102918144/

Code smells are like dirty dishes. They don't necessarily mean you're a bad 
cook, but they do mean you need to clean up after yourself. They are the 
first line of defense against code that is difficult to understand, modify, 
and maintain. 

Just as dirty dishes don't necessarily mean you're a bad cook, code smells 
don't imply that you're a bad developer. However, they do indicate areas 
where the code could be improved for better understandability, 
maintainability, and extensibility. 

Code smells may not always be indicative of a problem, but they can be an 
early warning sign that there could be issues down the line. 

Below some common code smells : 

- **Long method:** A method that is too long and complex, making it difficult to 
understand and maintain. 

When a method becomes excessively long and complex, it becomes difficult to 
understand and maintain. Breaking it into smaller, more focused methods 
improves readability and makes the code easier to work with 

- **Duplicate code:** The same code appearing in multiple places, which can be a 
sign of poor design and can lead to inconsistencies and errors… Remember that 
dupplication is evil.

Duplication in code leads to maintenance issues because changes need to be 
made in multiple places. Extracting common code into reusable functions or 
classes promotes better code organization and reduces redundancy. 

- **Too many parameters:** A method that takes too many parameters, making it 
difficult to use and understand. Break it into smaller functions or if 
necessary use an object. 

Methods with a large number of parameters can be hard to use and understand. 
Refactoring them by grouping related parameters into objects or using 
parameter objects can make the code more manageable. 

- **Large class:** A class that is too large and contains too much functionality, 
making it difficult to understand and maintain. 

Classes with excessive responsibilities become harder to comprehend and 
maintain. Splitting a large class into smaller, cohesive classes that each 
have a single responsibility promotes better organization and 
maintainability. 

- **Primitive obsession:** Overuse of primitive data types instead of creating 
objects, leading to code that is hard to understand and maintain. 

Overusing primitive data types instead of creating appropriate abstractions 
can lead to code that is hard to understand and maintain. Creating objects 
with well-defined behaviors can improve code readability and prevent 
scattered logic 

- **Shotgun surgery:** Making many small changes in different parts of the code 
in order to implement a single feature or fix a single bug, which can lead to 
code that is hard to understand and maintain. 

Making scattered changes across the codebase for a single feature or bug fix 
can introduce complexity and make the code harder to maintain. Identifying 
related code and refactoring it into cohesive units can improve code 
organization and reduce the need for scattered changes. 

- **Inappropriate intimacy:** Classes or modules that depend too heavily on each 
other, making it difficult to change one without affecting the others. 

Strong dependencies between classes or modules can lead to code that is 
tightly coupled and difficult to change independently. Applying principles 
like the Single Responsibility Principle and Dependency Inversion Principle 
can help decouple classes and promote modularity. 

Code smells are not always a problem, but they can be an early warning sign 
of deeper issues with the code, and should be investigated and addressed if 
necessary. 

By being aware of these code smells and addressing them when necessary, 
developers can improve the quality of their code, making it easier to 
understand, modify, and maintain in the long run. 


