---
title: "Notes tangential to the BGW protocol"
date: 2021-03-03
description: "What's going on and how do I think it might be improved"
---


{% include section.html c="Shamir's Secret Sharing" %}

Shamir's secret sharing is a scheme where a value can be split into _n_ shares, each of which doesn't tell one anything about the secret value.
Get enough of them together though, and you can recover the secret. 
A simpler scheme would be just be to split your secret into _n_ random values that add back up to the secret. 
(This works better and makes more sense in a finite field. Basically everything from here on out will be in the finite field of size two, _i.e._ "bits".)

In Shamir's scheme (from here on: SSS), we pick a random polynomial _f_ of some known degree _t-1_ such that _f(0)_ is the secret value. 
Each party _p_ then gets as their share the value _f(p)_. 
To reconstruct the secret, we just need any _t_ of the values; that's enough to pin down the polynomial and that gives us _f(0)_.

{% include section.html c="The Ben-Or Goldwasser Widgerson protocol" %}

One application of SSS is for secure multi-party computation
(basically the same idea as Homomorphic Encryption, but with _p_ parties involved).
Like all MPC systems I'm aware of, BGW starts by building a "circuit" representing the computation. 
The components of these circuits are primitive gates: NOT, XOR, and AND. 
We can use SSS for this because the shares have the two key homomorphisms: additive and multiplicative. 

- If I know _f(p)_ and _g(p)_, and I want _h(p)_ where _h(x)=f(x)+g(x)_, I can just add my two existing shares together. 
  Note that the resulting polynomial _h_ will have the same degree as _f_ and _g_ (assuming they were they same).
- If I know _f(p)_ and _g(p)_, and I want _h(p)_ where _h(x)=f(x)\times g(x)_, I can just multiply my two existing shares together. 
  Note that the resulting polynomial _h_ will have _double_ the degree of _f_ and _g_ (the degree sums).

Remember we're working in the finite field of size two; NOT is negation, XOR is addition, and AND is multiplication. 
So far this looks like a really good MPC protocol. The computations are cheap and we have information-theoretic security. 
The problem is that the degree of the polynomial goes up with every AND gate; if _t>p_, then not enough shares exist to recover the secret.
The solution is to rebuild the polynomial after every AND to reset the degree. 

**Questions:**

- How really does the reliniarization work? I've found conflicting explainations.
- Can relinearization be done on multi-secret shares? I think the answer is yes, but it's not clear yet. 

I think the key to reliniarization is that reconstruction of a secret is a function of the secret shares
_that can be represented as a circuit without multiplication_. 
Therefore if one has a _share_ of each _share_, one can get a share of the "truth".
This strongly suggests that multiple secrets could be relinearized at once, but I have to actually put together the matrixes in question to do that.
