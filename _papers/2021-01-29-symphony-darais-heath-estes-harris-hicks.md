---
title: "Symphony; David Darais, David Heath, Ryan Estes, William Harris, and Michael Hicks"
date: 2021-01-29
tags:
  - circuits
  - cryptography
  - papers
  - symphony
  - gmw
citation:
  author: "David Darais, David Heath, Ryan Estes, William Harris, & Michael Hicks"
  title: "λ-Symphony: A Concise Language Model for MPC"
  year: "2020"
  month: "July"
  where: "University of Vermont, Georgia Institute of Technology, Galois Inc., & University of Maryland"
---


The goal of this work is largely the same as Wysteria, to provide a language in which it's easy to write sound MPC applications. 
There are several differences:

- Symphony is written in Haskell instead of Ocaml. 
- Symphony is mostly agnostic about the cryptographic primitives with which MPC operations are carried out. 
The authors seem to assume that one will use GMW or something like it, but claim that any MPC protocol would work
(and the don't actually implement the distributed/encrypted version of the semantics anyway).
- Instead of sequestering "parallel" vs "secure" computations, the [en\|de]cryptedness (and ownership and location) of _values_ is tracked in the type system.
- The formal language is more similar to the vanilla typed lambda calculus.
- Wysteria doesn't provide a good way for parties to contribute secrets to a computation they don't themselves perform.
In other words, it's not much good for outsourced-computation. 

Symphony itself is Ocaml-like in the sense of having a fairly simple type system (not counting the two dimensions of complexity for tracking who _has_ a given value and who _could use it_), being strictly evaluated, and using `ref`s to track program state. 

The authors discuss toward the end various other MPC implementations. In particular, I'm interested in moving the _ease_ and _confidience_ of Symphony in the space of _libraries_. The authors claim that MPC libraries are sub-optimal because they require a programmer to manage the parallel-ness of the application manually, but I'm unconvinced that this is true/necessary. 
