class PostDTO:
    def __init__(self, title, content):
        self.title = title
        self.content = content

"""
In this file, we have the PostDTO class, which represents a Data Transfer 
Object (DTO) for a blog post. The PostDTO class has two attributes: title and 
content, which correspond to the title and content of a blog post, 
respectively. 

A DTO is a simple container object used to transfer data between different 
layers or components of an application. It provides a convenient way to 
encapsulate and transport data without exposing the underlying domain model. 

The purpose of the PostDTO class is typically to carry data from the 
application layer to the presentation or communication layer and vice versa. 
It helps in decoupling the internal representation of data from the external 
interfaces. 

In practice, you might have additional attributes or methods in the DTO class 
based on the specific requirements of your application. 

Remember that a DTO is a separate concept from domain entities or value 
objects in DDD. It serves as a representation of data rather than 
encapsulating behavior or enforcing business rules.
"""