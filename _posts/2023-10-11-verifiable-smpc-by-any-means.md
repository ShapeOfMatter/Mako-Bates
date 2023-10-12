---
title: "Computer verification of SMPC protocols by any means necessary"
date: 2023-10-11 13:00:00
description: "What's the state of the art for computer verification of SMPC programs?"
---

As I'll go on to describe, the PL community has been busy contributions to cryptography:
many kinds of cryptographic properties can be enforced in a program by careful static analysis, particularly of type annotations.
That said, most of this work does _not_ work when the property you want to enforce is
Secure Multi-Party Computation (MPC).
The particulars of MPC as a hyperproperty of programs make it difficult to test for;
there are some approximations that come close, but not many and not very close.

The only work specific to MPC still seems to be
[Computer-aided proofs for multiparty computation with active security](https://arxiv.org/abs/1806.07197),
which handles situations where the "Ideal Functionality" is an (efficiently!) invertible function.
Since existing general-purpose SMPC protocols can easily compute non-invertible functions, this is a serious limitation.
That said, their technique begins to get at what makes the problem so challenging.
They model SMPC as a kind of non-interference property:
Honest secrets are non-interfering on the corrupt views _conditioned on the corrupt outputs_.
Modulo the assumptions about the adversary's computational limits, that's the definition of SMPC.
If your functionality is invertible, then you can use Haagh _et al_'s system to ensure non-interference,
and your simulator will just invert from the final output, pick one of the candidate secrets, and run the protocol forward from the beginning.
If no part of the program is invertible at all, then no simulator is possible;
the simulator's _job_ is to invert from the final output to the corrupt views, which are intermediate values in the program.
Some combination of invertibility and non-interference is _necessary_, but Haagh _et al_'s is lacking in two respects:
First, the ideal functionality is abstract from the program, and no tools are provided for checking if it's efficiently invertible.
Second, existing secure protocols like GMW work just fine on circuit representations of functions we believe to be non-invertible
(such as SHA256).

Other concepts of non-interference and information-flow-control have been fruitful for other cryptographic properties.
My own work started as an extension of Darais _et al_'s language [λ-obliv](https://arxiv.org/abs/1711.09305).
Their type system supports a lemma guaranteeing uniformity and independence of random values that appear during program execution;
they use this to verify oblivious RAM structures, for example.
While this system can enforce uniformity of views, it does nothing to help incorporate the simulator's knowledge of the final output;
the remaining gap between a λ-obliv based system and an SMPC type system is basically the same as the original problem!

More recent work such as [OWL](https://eprint.iacr.org/2023/473.pdf) investigates fine-grain composition of cryptographic primitives;
the language takes a reasonably open-ended space of primitives as built-in, and the type system ensures they are used correctly
(This is non-trivial when their artifacts are nested, _e.g._ if a key gets encrypted).
This pattern taking cryptographic primitives as semantic built-ins, and enforcing correct usage via the type system,
is important in itself; many processes that are broadly assumed to be safe
(_e.g._ oblivious transfer, as seen in my own work)
don't have exact proofs of securety, and so can _only_ be incorporated by assumption.
There's even a body of work that takes MPC as a built-in (wysteria, what else?).

On the program inversion side, there is again a decent body of work none of which quite does what's needed.
The problem is posterior inference of input distributions.
Given the simulator's inputs (corrupt inputs and corrupt outputs),
infer the conditional distribution of views, or honest secrets, or some other membrane of values intermediate in the protocol.
Curiously, you can use whatever prior distribution you like;
secure programs are precisely the ones for which this doesn't matter
(TODO: find the proof of this I wrote out at some point).
To test for security, one needs to both be able to show that this posterior distribution is invariant of which _actual_ secret values were used,
and one needs to have a way of efficiently calculating and sampling from said distribution.
This test needs to be quantified over all possible corrupt inputs (and, usually, over all relevant suppositions of who's corrupt).

Techniques from Probabilistic Programming Languages may someday be applicable.
[Sum Product Networks](https://arxiv.org/abs/1202.3732) arguable do the job,
but their defining properties make them unable to represent the distributions seem in real MPC protocols
(specifically, deriving the network corresponding to a program which uses a variable more than once
gives a graph that breaks invariants of the SPN system).
[DICE](https://arxiv.org/abs/2005.09089), which is based on binary decision diagrams,
requires key variables to take concrete values;
since it's not parameterized, the work of applying it for an MPC proof is exponential.
[Lilac](https://arxiv.org/abs/2304.01339) may be useful for building a posterior-inference-based proof of MPC security by hand,
but it's not automated.

