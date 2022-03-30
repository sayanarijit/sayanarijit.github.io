---
layout: note
tags:
- tech
- programming
- learning
---

# Functional Programming

If you find dealing with states in your Object Oriented Programming (OOP) codebase difficult or error-prone, you might want to say goodbye to states, and try functional programming (FP).


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

{-| As you see, we only define a function, without actually changing any state.
    An outside program will use this function to change state, but we don't
    need to worry about that. In FP, we only define what happens when the data
    comes.
-}
```

FP is more closer to mathematics than OOP can ever hope to be, allowing it to reasonably tackle some of the head-scratching limitations OOP comes with.

## FP and Mathematics

Mathematics is the basis of FP, but IMO [[Category Theory]] defines the most interesting concepts of FP.

Four primary mathematical data types that you will encounter in many FP languages are:

- Unit Type: Only one version of the data can exist in the entire category (e.g. `null` in OOP).
- Sum Type: Only one of the many versions of data in a particular category can exist (e.g. `int`, `char`, `enum` in OOP).
- Product Type: A collection of Unit Type, Sum Type and Product Type data (e.g. `object`, `list of objects` in OOP).
- Function: Functions are first-class citizens in FP. i.e. they can be passed around as argumets like any other data type.

## FP languages

Some popular FP languages are:

- Elm[^1]: My favourite FP language that offers you zero runtime error guarantee on the frontend. It's delightful as it claims and very easy to pick up.
- PureScript: Another FP language for the frontend.
- Haskell: The most popular general purpose FP language.
- Erlang: FP langguage for the backend optimized for massive concurrency and fault tolerance.
- Clozure and ClozureScript: Backend and frontend FP gateway for Java developers. It's a dialect of Lisp (a family of FP languages).
- Scala: Another FP gateway for Java developers.
- Nix: A dynamic configuration/scripting language.

---

Learn More:

- https://github.com/xgrommx/awesome-functional-programming
- https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/

[^1]: https://elm-lang.org/
