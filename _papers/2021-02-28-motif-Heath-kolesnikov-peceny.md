---
title: MOTIF: Cheap branching in GMW
date: 2021-02-28
tags:
  - GMW
  - cryptography
  - circuits
citation:
  author: "David Heath, Vladimir Kolesnikov, and Stanislav Peceny"
  title: "MOTIF: (Almost) Free Branching in GMW via Vector-Scalar Multiplication"
  howpublished: "IACR-ASIACRYPT-2020 "
  year: 2020
  month: September
  where: "Georgia Institute of Technology, Atlanta, GA, USA"
---

Even given precomputed oblivious transfer, GMW still requires three bits sent from each party for every AND gate in the circuit.
The AND gates also consume the precomputed OT material.
The advancement of this paper is that it lets parties evaluate, for _basically_ the cost of a single AND gate, one gate in each of however many mutually exclusive branches. 
The has obvious parallels with the earlier Stacked Garbling process, but the technique is totally different. 

The central idea is the introduction of a "vector-scalar" gate, in which a whole set of values are multiplied (AND'd) with another single value.
Such a gate can be evaluated with only one round of OT.

The way to leverage VS gates is by applying the "AND FALSE" part of the branching at the beginning. 
Then, with a little extra (cheap) finagling, the true value of all wires in branches not taken will be 0. 
For each of the parallel AND gates, pick one of the wires as "x", and the other as "y".
It's safe to XOR all the x's together because only one of them can be non-zero.
AND'ing that with each of the y's is a VS operation, 
and will yield 0 on all the output wires in the inactive branches (as required) and the correct result in the active branch. 

I need to spend more time on this paper, in particular to figure out if any part of it can help out with the BGW scheme. 

The Related works section of this paper also needs a closer reading.



