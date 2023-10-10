---
title: "OWL: Compositional Verification of Security Protocols via an Information-Flow Type System; 2023"
date: "2023-09-20"
tags:
  - modular_proofs
  - security
  - cryptography
  - composition_of_security
citation:
  author: "Joshua Gancher; Sydney Gibson; Pratap Singh; Samvid Dharanikota; Bryan Parno"
  title: "OWL: Compositional Verification of Security Protocols via an Information-Flow Type System"
  howpublished: "2023 IEEE Symposium on Security and Privacy (SP)"
  year: 2023
  month: May
  where: "Carnegie Mellon University"
  url: https://eprint.iacr.org/2023/473.pdf
---

This paper is part of the ongoing effort toward language- and type-based cryptographic security.
One distinguishing feature of OWL, according to the authors, is that OWL uses the "computational model",
_i.e._ everything is done at the level of bits
and adversaries are arbitrary poly-time Turing machines.
I find that odd, as most such papers I'm aware of use the use a similar model,
but it's true that the poly-time aspect isn't always in focus.
Anyway, OWL is strongly typed, and these types carry the burden of proof.
The actual guarentee you get is:

> OwlLang guarantees that well-typed protocols satisfy simulatability and correctness.
> Simulatability states that, for any adversary A corrupting a chosen set of names,
> running the protocol cannot leak any more information to A than it had before
> the protocol’s execution.
> Dually, correctness states that all refinements on data in the protocol hold with high probability.

Reading deeper, their "correctness" is not MPC correctness,
but rather an "almost always" version of normal type-safety.

Simulatabilty is harder to pin down.
It's game-based, and _sounds_ like MPC security, but
I'm moderately certain that Owl cannot do MPC.

More specifically what the type system does is basically just information-flow
augmented by modular composable cryptographic primitives such as \{en|de\}cryption, hashing, and DHKE.
The only actual data the implied simulator _S<sub>λ</sub>_ (definition 5) gets is _N : Name→{0,1}\*_.
_N_ is a "name environment" mapping base names to their values;
it's an argument to the semantics game and a constant within it.
(Note that the defining equation _b=b'_ is probabilistic over the sampling of _N_ from the interpretation via _Gen_.)
Of course the simulator can't use all of _N_; the rules of _Orcl_ mask off uncorrupted names,
but the point is that _S<sub>λ</sub>_ doesn't have access to the _results_ of anything they way it would in MPC.
In the proof overview of Theorem 1 (and AFAICT this is confirmed in appendix C of the big version of the paper),
they explain that security follows from applying reductions from `Real` crypto primitives to `Ideal` ones,
and then applying information-flow control.
In particular see the first column of page 20: The simulator is just running the protocol
(_K_ is a list of expressions (which are programs), one for each party),
substituting fresh random values for anything in _N_ it can't see.
If they were doing MPC, they would need to ensure the substitutions were consistent with some final output.


<sub>(Aside for anyone following along: There's a typo in the game in Fig 10.
Line 6 should be `(...) <$- [[ K[j] ]]^N ...`; this is where the _K_onfiguration gets used.)
