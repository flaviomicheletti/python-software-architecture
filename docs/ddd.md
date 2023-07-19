# DDD (Domain-Driven Design)

- https://www.domainlanguage.com/
- https://www.domainlanguage.com/ddd/reference/attachment/pattern-language-overview-med/

DDD stands for Domain-Driven Design, which is an approach to software 
development that focuses on modeling the business domain and incorporating 
that model into the software design process. It was first introduced by Eric 
Evans in his book "Domain-Driven Design: Tackling Complexity in the Heart of 
Software" published in 2003. 

The main idea behind DDD is to align the software design with the business 
domain, emphasizing the understanding and collaboration between domain 
experts and software developers. By doing so, DDD aims to produce software 
systems that accurately reflect the real-world problem being solved and 
provide solutions that are maintainable, flexible, and adaptable to changing 
business needs. 

Key concepts in DDD include: 

**Ubiquitous Language:** DDD promotes the use of a common language shared by 
all team members, including domain experts, developers, and stakeholders. 
This language helps to bridge the communication gap between technical and non-
technical team members, ensuring that everyone has a shared understanding of 
the domain. 

**Bounded Contexts:** A bounded context is a specific boundary within which a 
particular model, language, and design are defined. Different parts of a 
software system may have distinct bounded contexts, allowing each part to 
have its own model and terminology that makes sense within that context. This 
helps manage the complexity of large systems and enables teams to work on 
different parts independently. 

**Aggregates:** Aggregates are clusters of related objects that are treated 
as a single unit. They encapsulate a set of entities and value objects, 
ensuring that their consistency and invariants are maintained. Aggregates 
help define transactional boundaries and enforce business rules within a 
domain. 

**Entities and Value Objects:** Entities represent objects with unique 
identities and have a lifespan that extends beyond a single transaction or 
session. Value objects, on the other hand, are objects without identity and 
are defined solely by their attributes. Distinguishing between entities and 
value objects helps model the domain more accurately. 

**Domain Events:** Domain events capture meaningful occurrences within the 
business domain. They represent significant changes or updates that need to 
be propagated to other parts of the system. Domain events enable loose 
coupling between different components of the system, allowing them to react 
and update accordingly. 

DDD provides a set of principles, patterns, and practices to guide the 
development process. It encourages iterative development, where the domain 
model evolves and is refined over time based on continuous learning and 
feedback from domain experts. 

Overall, Domain-Driven Design promotes a collaborative and iterative approach 
to software development, focusing on understanding the business domain and 
aligning the software design accordingly. By doing so, DDD aims to build 
software systems that are both technically robust and closely aligned with 
the real-world problems they solve. 


## Main Topics

Here are the key concepts and principles of Domain-Driven Design (DDD) 
that constitute the most important 20% of learning, which will help 
you understand 80% of DDD:

1. Ubiquitous Language: Focus on developing a shared language with domain 
experts and team members. A common language helps bridge the communication 
gap and ensures a shared understanding of the domain. 

2. Bounded Contexts: Identify and define specific boundaries within which a 
particular model, language, and design are applied. Bounded contexts help 
manage the complexity of large systems and allow different parts to have 
their own models and terminologies. 

3. Aggregates: Clusters of related objects treated as a single unit. 
Aggregates encapsulate entities and value objects, ensuring consistency and 
enforcing business rules within a domain. 

4. Entities and Value Objects: Entities represent objects with unique 
identities and lifespans that extend beyond a single transaction or session. 
Value objects are objects defined solely by their attributes, without 
identity. 

5. Domain Events: Capture meaningful occurrences within the business domain. 
Domain events represent significant changes or updates that need to be 
propagated to other parts of the system, enabling loose coupling and allowing 
components to react accordingly. 

6. Domain Model: Develop a conceptual model that accurately reflects the 
business domain. The domain model is based on the understanding of the 
business problem and is used to drive the design of the software system. 

7. Context Mapping: Establish relationships and interactions between bounded 
contexts. Context mapping techniques, such as partnership, shared kernel, and 
customer-supplier, help manage the integration points and ensure consistency 
across contexts. 

8. Strategic Design: Focus on the overall structure and organization of the 
system. Strategic design decisions involve identifying the core domain, 
supporting subdomains, and generic subdomains, and defining the relationships 
between them. 

9. Tactical Patterns: Apply tactical patterns such as repositories, 
factories, and specifications to solve recurring design problems within the 
domain model. 

10. Continuous Collaboration: Foster ongoing collaboration between domain 
experts and software developers to ensure the model evolves and accurately 
represents the changing business needs. 

11. Iterative Development: Embrace an iterative and incremental approach to 
software development. Iterate on the domain model and incorporate feedback 
from domain experts and stakeholders to refine and improve the software 
system. 

12. Test-Driven Development (TDD): Use test-driven development techniques to 
drive the design and implementation of the domain model. Write tests that 
capture the desired behavior of the system and then implement the necessary 
code to make the tests pass. 

13. Event Storming: Conduct collaborative workshops, such as event storming, 
to gain a deeper understanding of the business domain and identify domain 
events, aggregates, and bounded contexts. 

14. Domain-Driven Design Patterns: Familiarize yourself with common DDD 
patterns like aggregate roots, value objects, domain services, and event 
sourcing. These patterns provide practical solutions for modeling complex 
business domains. 

15. Domain-Driven Database Design: Align database design with the domain 
model to ensure data consistency and reflect the business rules. Techniques 
such as table inheritance and denormalization can be used to map the domain 
model to the database schema. 

16. CQRS (Command Query Responsibility Segregation): Consider using CQRS to 
separate read and write operations in complex domains, allowing for 
independent scalability and optimization. 

17. Event Sourcing: Implement event sourcing to store a log of domain events 
as the source of truth, enabling the ability to reconstruct the state of the 
system at any point in time. 

18. Anti-Corruption Layer: Use an anti-corruption layer to isolate and 
encapsulate legacy or third-party systems that don't align well with the 
domain model. 

19. Domain-Driven Design in Microservices: Understand how DDD principles can 
be applied in a microservices architecture to achieve bounded contexts and 
autonomous services. 

20. Continuous Learning: Stay updated with the latest developments and 
advancements in DDD. Engage with the DDD community, attend conferences, and 
explore new resources to continue expanding your knowledge. 

Focusing on these key concepts and principles will provide you with a solid 
foundation in DDD and help you understand the core ideas and techniques 
behind it. 



## Plan to study

1. Understand the Core Concepts: 

- Start by reading the book "Domain-Driven Design: Tackling Complexity in the 
Heart of Software" by Eric Evans. It provides a comprehensive introduction to 
DDD and covers the core concepts, principles, and patterns. 
- Take notes and highlight key concepts while reading the book to solidify 
your understanding. 
- Explore online resources and tutorials that explain DDD concepts in 
different contexts. 

2. Practice Ubiquitous Language: 

- Focus on developing a shared language with domain experts and team members. 
Engage in discussions to clarify and define terms and concepts related to the 
business domain. 
- Identify the core concepts and domain terms from the book and start using 
them in your conversations and documentation. 

3. Apply DDD in a Small Project: 

- Choose a small project or a specific module within a larger project to 
apply DDD concepts. 
- Identify the bounded contexts and their relationships within your project. 
- Create a domain model using entities, value objects, aggregates, and domain 
events. 
- Implement the model in your chosen programming language (Python in your 
case) and use it as a starting point for further exploration. 

4. Learn from Real-world Examples: 

- Study existing projects or case studies that have successfully implemented 
DDD. 
- Analyze their domain models, bounded contexts, and how they handle complex 
business logic. 
- Examine how they integrate DDD with other architectural patterns and 
practices. 
- Look for open-source DDD projects or sample codebases in Python and explore 
their implementations. 

5. Collaborate with Domain Experts: 

- Engage in regular discussions with domain experts to gain a deeper 
understanding of the business domain. 
- Seek feedback on your domain models and solicit their insights on how the 
software can better align with the real-world problem being solved. 

6. Attend Workshops and Conferences: 

- Look for workshops, conferences, or webinars related to DDD where you can 
learn from experienced practitioners and industry experts. 
- Participate in interactive sessions and ask questions to clarify your 
understanding. 

7. Join Online Communities: 

- Join online forums, discussion groups, or social media communities focused 
on DDD. 
- Engage in conversations, share your experiences, and learn from the 
experiences of others. 
- Ask questions, seek advice, and contribute to discussions to deepen your 
knowledge. 

8. Continuous Learning and Improvement: 

- Stay updated with the latest trends and advancements in DDD by reading 
blogs, articles, and books authored by DDD practitioners. 
- Explore advanced topics like event sourcing, CQRS (Command Query 
Responsibility Segregation), and tactical patterns such as repositories, 
factories, and specifications. 

Remember, learning DDD is an iterative process. It's essential to apply the 
concepts in real-world scenarios, seek feedback, and continuously refine your 
understanding and skills over time. 

