---
title: Precomputing Oblivious Transfer; Donald Beaver; 1995
date: 2021-02-03
tags:
  - circuits
  - cryptography
  - papers
  - gmw
citation:
  author: Donald Beaver
  title: "Precomputing Oblivious Transfer"
  howpublished: "Advances in Cryptology - CRYPT0 ’95, LNCS 963, pp. 97-109"
  year: 1995
  where: "Penn State University, University Park, PA"
---

A lot's changed in 25 years.
The paper's entirely readable in a modern context, but everything from the class of applications in which the author is interested, to the choice of fonts, reminds the reader of this foreign context.
The paper is _short_, and half of it is just laying out the theoretical framework within which it's going to describe it's contribution. 

The lasting contribution that's of interest to my work is the ability to do most of the heavy lifting of a 1-of-2 OT in advance (that is, before either party has decided on their inputs to the "real" oblivious transfer). 
This has obvious performance implications for, for example, GMW circuit execution. 
(Actually realizing a total speed boost may not be trivial though.)

### How:

_A_ and _B_ perform normal oblivious transfer with _random_ inputs. 

> _A_ generates random values (`R0`, `R1`), and knows them.  
> _B_ generates random value `d`, and learns `Rd`.

Then at runtime, when _A_ knows the real values (`B0`, `B1`) and _B_ knows the real choice `c`, the oblivious transfer can be completed with only three more bits being communicated.  

> _B_ sends `e = c ⊕ d`.  
> _A_ sends `x0 = B0 ⊕ Re` and `x1 = B1 ⊕ R(!e)`.

Consider the four cases for `(c, d)` (neither of which are known to _A_) and `e` (which _A_ does know):

- `(0, 0), 0`: _B_ gets `B0 ⊕ R0` and `B1 ⊕ R1`. Since they already know `R0`, they can figure out `B0` (which is `Bc`), but they can't figure out `B1` because they never learned `R1`.
- `(0, 1), 1`: _B_ gets `B0 ⊕ R1` and `B1 ⊕ R0`. Since they already know `R1`, they can figure out `B0`, but they can't figure out `B1` because they never learned `R0`.
- `(1, 0), 1`: _B_ gets `B0 ⊕ R1` and `B1 ⊕ R0`. Since they already know `R0`, they can figure out `B1`, but they can't figure out `B0` because they never learned `R1`.
- `(1, 1), 0`: _B_ gets `B0 ⊕ R0` and `B1 ⊕ R1`. Since they already know `R1`, they can figure out `B1`, but they can't figure out `B0` because they never learned `R0`.

This gets used by a variety of later works, including the recent "basically free IF" paper.
