---
title: "Notes tangential to the BGW protocol
date: 2021-03-03
description: "What's going on and how do I think it might be improved"
---


{% include section.html c="Shamir's Secret Sharing" %}

Shamir's secret sharing is a scheme where a value can be split into $n$ shares, each of which doesn't tell one anything about the secret value.
Get enough of them together though, and you can recover the secret. 
A simpler scheme would be just be to split your secret into $n$ random values that add back up to the secret. 
(This works better and makes more sense in a finite field. Basically everything from here on out will be in the finite field of size two, _i.e._ "bits".)

In Shamir's scheme (from here on: SSS), we pick a random polynomial $f$ of some known degree $t-1$ such that $f(0)$ is the secret value. 
Each party $p$ then gets as their share the value $f(p)$. 
To reconstruct the secret, we just need any $t$ of the values; that's enough to pin down the polynomial and that gives us $f(0)$.

{% include section.html c="The Ben-Or Goldwasser Widgerson protocol" %}

One application of SSS is for secure multi-party computation
(basically the same idea as Homomorphic Encryption, but with $p$ parties involved).
Like all MPC systems I'm aware of, BGW starts by building a "circuit" representing the computation. 
The components of these circuits are primitive gates: NOT, XOR, and AND. 
We can use SSS for this because the shares have the two key homomorphisms: additive and multiplicative. 

- If I know $f(p)$ and $g(p)$, and I want $h(p)$ where $h(x)=f(x)+g(x)$, I can just add my two existing shares together. 
  Note that the resulting polynomial $h$ will have the same degree as $f$ and $g$ (assuming they were they same).
- If I know $f(p)$ and $g(p)$, and I want $h(p)$ where $h(x)=f(x)\times g(x)$, I can just multiply my two existing shares together. 
  Note that the resulting polynomial $h$ will have _double_ the degree of $f$ and $g$ (the degree sums).

Remember we're working in the finite field of size two; NOT is negation, XOR is addition, and AND is multiplication. 
So far this looks like a really good MPC protocol. The computations are cheap and we have information-theoretic security. 
The problem is that the degree of the polynomial goes up with every AND gate; if $t>p$, then not enough shares exist to recover the secret.
The solution is to rebuild the polynomial after every AND to reset the degree. 
