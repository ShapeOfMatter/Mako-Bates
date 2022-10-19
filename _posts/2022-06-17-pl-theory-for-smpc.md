---
title: "PL Theory for SMPC Implementations"
date: 2022-06-17 13:00:00
description: "Programming Language(s) for automatic verification of Secure Multi-Party Computation implementations"
---

My primary research project this year is to build a language with type system enforcing MPC security.
This is _not_ a language that takes SMPC protocols as primitives;
instead it takes communication between parties as its key primitive,
and an SMPC scheme such as GMW can be build inside of it and type-checked.
Once the language can be made sufficiently expressive,
people will be able to express new or special-case protocols and use the type-checker instead of bespoke proofs of security.

[Earlier work](https://arxiv.org/abs/1806.07197) accomplished a similar goal,
but restricted itself to situations where the "Ideal Functionality" was an (efficiently!) invertible function.
Since existing general-purpose SMPC protocols can easily compute non-invertible functions, this is a serious limitation.

Our work began by building on top of Darais, Sweet, Liu, & Hicks's language [λ-obliv](https://arxiv.org/abs/1711.09305).
Their type system supports a lemma guaranteeing uniformity and independence of random values that appear during program execution;
this can be used to trivialize _most_ of the work of a hypothetical simulator of the program in question.
We've been investigating various techniques for [program inversion](https://link.springer.com/chapter/10.1007/3-540-36377-7_13)
and [causal-graphical-model analysis](https://arxiv.org/abs/1301.3847) to bridge the remaining gap.
We expect to start presenting a solution based on [Sum-Product-Networks](https://arxiv.org/abs/1202.3732) this Fall.

