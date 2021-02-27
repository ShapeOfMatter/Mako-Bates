---
title: Wysteria; Aseem Rastogi, Matthew Hammer, and Michael Hicks; 2014
date: 2021-01-24
tags:
  - circuits
  - cryptography
  - papers
  - wysteria
  - gmw
citation:
  author: Rastogi, Aseem and Hammer, Matthew A. and Hicks, Michael
  title: "Wysteria: A Programming Language for Generic, Mixed-Mode Multiparty Computations"
  howpublished: "SP '14 Proceedings of the 2014 IEEE Symposium on Security and Privacy"
  year: "2014"
  month: May
  isbn: "978-1-4799-4686-0"
  where: "University  of  Maryland,  College  Park"
---

I'm not going to be able to do this justice in one pass.
On the other hand, it doesn't seem like this paper introduces any significant _theoretical_ advancements.
Rather, this is a _substantially better than previous_ compiler for the GMW protocol.

### GMW

The GMW protocol (Goldreich,Micali, and Wigderson) is a circuit-based protocol for n-party MPC.
Wire values are represented in cipher-space as Shamier shares.

Assuming (as is typical) that the circuit is a boolean circuit, `NOT` and `XOR` can be performed without communication.
Other gates can be performed using oblivious transfer:
"I know what my share _would_ be for each of your possible shares, so I'll OT to you the one that corresponds to the shares you actually do have."
(How does that part translate to n parties?)

### Mixed-mode computation

The biggest contribution of this paper/language is that it's a single language that expresses and compiles to mixed-mode computations.
A mixed-mode computation is just one that has MPC and parallel un-encrypted steps interleaved. 
The un-encrypted sections are called "parallel" because they're typically performed by several parties (e.g. _all_ the parties) at once in parallel; everyone arrives at the same result/continuation deterministically. 
Previously MPC implementations left this interleaving mostly manual, which meant the correctness of that aspect of one's program needed to be checked by hand.
Wysteria annotates values/computations with "mode" attributes, and checks rules about the contexts in which any given mode is allowed. 

### Single-threadedness

Wysteria really has two "implementations", which can be proven to be equivalent. The one intended for actual use compiles down to the needed collection of parallel-step machine code MPC circuits (there's a whole client/server architecture to actually run these programs). The other implementation let's one imagine the system as a monolithic single-threaded computation; this is easier to think through the behavior of, and one can rely on the provided equivalence proofs. 




