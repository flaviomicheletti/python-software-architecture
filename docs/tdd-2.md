# TDD


## Any post on Linkedin

The biggest benefit of TDD is not the code covered with tests.

Instead, it's the ability to think SMALL.

The SIZE of a problem you are trying to solve without TDD:
- Implement the complete login functionality.

The SIZE of a problem you are trying to solve with TDD:
- The login fails when an email is not in a valid format.

Solving small problems is much easier than solving big ones.

The side-effect of having the tests is a nice bonus.



## Comment 

However, it can be difficult to break down a large problem to its small 
components and it is often an iterative approach that does take some skill to 
learn. 

I often find myself on a whiteboard to sketch out a high-level idea for 
solving a big problem. And after implementing some of it I find that it was 
the wrong approach. Which leads to the issue of scaping the code and start 
over or evolving it. 

So while TDD is a great tool it is also a hard tool to master. 


## Comment 

If you know there's a chance you'll have to scrape the code, since your high-
level approach does not pan out, why lose time writing detailed test for each 
intermediate step? Just focus on making a PoC work, test on an integration 
level, by any means that will give you fastest, though perhaps not detailed, 
feedback. Only when you sure that all these components are indeed usable in 
key use-cases, then, if you wish, support your detailed implementation with 
writing tests first. But, whether the architecture and basic design will 
work - will already be known. 


## Comment 

Thinking small can work for small problems, and implies that any problem is 
solvable just by looking over the horizon only one problem ahead. This is not 
how any software of decent complexity can be built. 


## Comment 

This is a nice benefit, but I think having a well tested solution is a much 
bigger one. That allows you not only to solve a problem locally, but solve a 
problem *and be sure you didn't break anything else*. The fear of breaking 
stuff elsewhere is a real issue in low test codebases, and leads to people 
not paying back tech debt because they're scared to touch anything. 

The benefits of thinking small can be overstated - sometimes if you go one 
step at a time with your head down looking at each step, you walk into a dead 
end. 


## Comment 

Totally agree !The incremental aspect is the essence of TDD. TDD encourages 
an iterative approach to software development by focusing on solving small-
sized problems rather than diving into larger ones. By adopting an 
incremental approach, you can track and measure progress more clearly. Each 
small development step is tested and validated, allowing tangible 
improvements to be seen in the code along the way. Furthermore, resolving 
small problems one at a time helps mitigate risks and errors. You can 
concentrate on creating specific tests for each functionality, increasing 
confidence in the quality of the produced code. Additionally, the incremental 
approach of TDD provides rapid feedback on code changes. By writing tests 
first, you can immediately see if your modifications are working as expected 
or not. This fosters a more iterative and responsive development process. 

