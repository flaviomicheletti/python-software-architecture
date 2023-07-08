class CommentDTO:
    def __init__(self, content):
        self.content = content


"""
In this file, we have the CommentDTO class, which represents a Data Transfer 
Object (DTO) for a comment. The CommentDTO class has a single attribute, 
content, which corresponds to the content of a comment. 

Similar to the PostDTO, a CommentDTO is a simple container object used to 
transfer data between different layers or components of an application. It 
helps in decoupling the internal representation of data from the external 
interfaces. 

The purpose of the CommentDTO class is to carry comment data between 
different parts of the application or to communicate with external systems or 
interfaces. It provides a way to represent comment information without 
exposing the underlying domain model or business logic. 

In practice, you may have additional attributes or methods in the DTO class 
based on your specific application requirements. 

Remember that DTOs are separate from domain entities in DDD. They are 
primarily used for data transfer and are not responsible for encapsulating 
behavior or enforcing business rules.
"""