---
layout: note
tags:
- tech
- computer-science
---

# Functional Programming

If you find dealing with states in your Object Oriented Programming (OOP) codebase difficult or error-prone, you might want to say goodbye to states, and try functional programming (FP).

Functional Programming is one of the many paradigms of [[programming]].


## FP vs OOP

In OOP paradigm, you think everything in terms of objects (even non-physical entities like concepts and logics) and try to create an universe where those objects interact with each other, changing each other's state over *time*.


Example: (in Python)

```python
my_object = SomeClass()

for some_object in another_object:
    my_object.change_state(some_obbject)

my_object.print_result()

# As you see, my_object state changes over time, and we, programmers are
# responsible for actually changing state and keeping track of the changes.
```

While in FP paradigm, you think everything in terms of functions, i.e. things you encountered back then in mathematics that looked like `ƒ`, that, when given an input produces some output. There's no concept of *time* here, and hence no concept of states either.

Example: (in Elm)

```elm
myFunction dataProducerFunction =
	dataProducerFunction
	|> List.map someFunciton
	|> anotherFunction
	|> printFunction

{-| As you see, we only define a function, that will produce output when given
    some input data. The input data (a function) doesn't change.
    An outside program will use this function to change state, but we don't
    need to worry about that. In FP, we only define what happens when the data
    comes.
-}
```

FP is more closer to mathematics than OOP can ever hope to be, allowing it to reasonably tackle some of the head-scratching limitations OOP comes with.


### Why isn't Functional Programming the norm?

https://youtu.be/QyJZzq0v7Z4

## FP and Mathematics

Mathematics is the basis of FP, but IMO [[Category Theory]] defines the most interesting concepts of FP.

Two algebraic data types that define the building block that you will encounter in many FP languages are:

- Sum Type (or): Only one of the many possible values of the type can exist at one time (e.g. `int`, `char`, `enum` in OOP).
- Product Type (and): Values of different types exist together (e.g. `object`, `list of objects` in OOP).

https://youtu.be/JH_Ou17_zyU

## FP languages

Some popular FP languages are:

- [[Elm]]: My favourite FP language that offers you zero runtime error guarantee on the frontend. It's delightful as it claims and very easy to pick up.
- PureScript: Another FP language for the frontend.
- Haskell: The most popular general purpose FP language with the weird moto "avoid success at all costs"[^1].
- Erlang: FP langguage for the backend optimized for massive concurrency and fault tolerance.
- Clozure and ClozureScript: Backend and frontend FP gateway for Java developers. It's a dialect of Lisp (a family of FP languages).
- Scala: Another FP gateway for Java developers.
- Nix: A dynamic configuration/scripting language.


## Resources

### Functional Programming for Pragmatists • Richard Feldman • GOTO 2021

https://youtu.be/3n17wHe5wEw

### Functional Programming Design Patterns

https://vimeo.com/113588389

### The Functional Programmer's Toolkit

https://youtu.be/Nrp_LZ-XGsY

---

Learn More:

- https://github.com/xgrommx/awesome-functional-programming
- https://www.youtube.com/c/LambdaWorld
- SICP: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/
- https://www.youtube.com/channel/UC_QIfHvN9auy2CoOdSfMWDw
- https://www.haskellforall.com/?m=0
- Practical Common Lisp: https://gigamonkeys.com/book/
- How to use NixOS for lightweight integration tests: https://www.haskellforall.com/2020/11/how-to-use-nixos-for-lightweight.html

[^1]: https://news.ycombinator.com/item?id=12056169
