---
title: "Choreographic Programming part 1 of 3?"
date: 2024-09-24 13:00:00
description: "A cursory history of Choreographic Programming"
citations:
  haschor:     <a href="https://dl.acm.org/doi/10.1145/3607849" title="the HasChor paper"              >[1]</a>
  choral:      <a href="https://www.choral-lang.org/"           title="the Choral website"             >[2]</a>
  chor-lambda: <a href="https://arxiv.org/abs/2111.03701"       title="the Chorλ paper"                >[3]</a>
  RC:          <a href="https://arxiv.org/abs/1712.05465"       title="the Robust Choreographies paper">[4]</a>
  pirouette:   <a href="https://arxiv.org/abs/2111.03484"       title="the Pirouette paper"            >[5]</a>
  polychor:    <a href="https://arxiv.org/abs/2303.04678"       title="the PolyChorλ paper"            >[6]</a>
  thesis:      <a href="https://www.fabriziomontesi.com/files/choreographic-programming.pdf" title="Fabrizio Montesi's PhD thesis">[7]</a>
  chor-lambda-2: <a href="https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ECOOP.2023.7" title="Modular Compilation for Higher-Order Functional Choreographies" >[8]</a>
---

> In this sequence of posts I'm going to try to summarize the state of research into Choreographic Programming (CP),
> it's recent past, status quo, and what I anticipate happening soon.
> I'm assuming any readers already have a basic sense of what CP _is_;
> if not, I'd suggest readers familiar with Haskell to start with the HasChor paper {{ page.citations.haschor }}
> and other readers to start with Choral {{ page.citations.choral }}.


The vibe among people who've been working on choreographic programming (CP)
is that CP is _about_ to become a mainstream way of writing concurrent systems.
I think there's a sense in which that's true, but the situation could be much improved.
In preparation for describing my own research plans for the next year, I figured I should summarize my understanding of recent history.
There's inherent risk in writing any such thing: I'm going to get it wrong and I'm going to omit important stuff.
In fact, in this first post, I'm only going to discuss six papers.
Part two will summarize my notes from the recent CP workshop at PLDI 2024.

## Choral: Object-oriented Choreographic Programming {{ page.citations.choral }}

I'm skipping about a decade of work during which CP gestated from a way of _describing_ concurrent systems,
to _specifying_, _validating_, and eventually _writing_ them
The Choral team,
Saverio Giallorenzo, Fabrizio Montesi, and Marco Peressotti,
have been working on CP for a long time, and as I understand it Choral itself was several years in the making.
As I'll touch on later, CP is not an especially counter-intuitive way of writing software,
but was a big deal in 2013 when F. Montesi showed that it was possible (and worthwhile!) to formalize the concept
{{ page.citations.thesis }}.
Prior to Choral, it wasn't really possible to _use_ CP for anything; any implementations were completely bespoke,
so it wouldn't be practical to get them to work with any existing software.
Choral jumped straight ahead to full interoperability with Java.
Any Java code can be directly imported into Choral, and Choral programs compile for the JVM.

Beyond the novelty of simply implementing a modern notion of CP,
Choral also implements higher-order choreographies and polymorphism, which are obviously desirable for real-world use.
In some ways though, Choral is quite different from most other CP systems:
it does not assume a complete communication graph.
In order for two parties to communicate, they must have a `Channel` object.
The actual implementation of these channel objects is fairly normal Java code;
the Choral compiler assumes they're implemented correctly
but can otherwise enforce the safety of whatever communication paradigm the user feels like building.
On the one hand this feels a little "low level" for a modern system,
but it's actually quite realistic for there to be parties in a choreography who can't directly communicate
or who don't know addresses for each other. 
Furthermore, `Channel`s are generic over their message type, so issues with serializability can be handled in a more fine-grained way.
Most of the contemporary work that I know of starts at a higher level, and I'm not sure that's a good thing.


## Formalisms: Chorλ {{ page.citations.chor-lambda }} and Pirouette {{ page.citations.pirouette }}

Both Pirouette and Chorλ claim to be the "first higher-order choreographic programming languages".
Who exactly gets the honor isn't interesting; more important are the differences and similarities between the two.
In both cases, the headline contribution is the ability to write functions that consume and return choreographies
(and functions that work on functions, and choreographies that yield functions, and choreographies that yield choreographies, and so on recursively).
In both cases, recursion is handled by using a top-level namespace of mutually dependent definitions;
I assume this is just to simplify the proofs.

Chorλ is a lambda calculus augmented with communication operations.
(Why does it need two? See below!)
In the "centralized" semantics (my word, they don't call it anything in particular) communication is basically a no-op;
it just changes some of the annotations.
Specifically, some terms are annotated with their owners, and communication changes the owner of its argument
(or rather copies it to a new owner, there's no mutation).
The nice thing about Chorλ is that there's not much more going on:
It's _almost just_ a lambda calculus.
That said, I wish it were even simpler.
The entire business of name-spaces and the Σ context seems like it should be possible to do without.

Pirouette does basically all the same things as Chorλ, but differently.
At first glance it seems like it's designed more with implementation in mind,
but that's probably not the whole motivation for the differences because the authors of Pirouette have a Coq proof of their core theorems.
In short, Pirouette is more imperative and less monolithic than Chorλ.
Pirouette _per se_ is an outer language with a simple imperative semantics,
but certain spots in some of the commands are expressions in an inner language
and _Pirouette is parametric over the inner language!_
This means (in principal, I'm less sure of practice) that one could use one's choice of mainstream single-threaded languages
for the local computations in a Pirouette choreography.
In any case, every such expression and every term-level variable is name-spaced to a specific location.
(There's a separate name space for choreography variables.)

Like basically all CP formalisms, Chorλ and Pirouette each have a second "local" semantics.
Specifically the "endpoint projection" operator (EPP), parameterized by a target party or location,
transforms a choreography into a program _in a different language_;
the result is a completely local implementation of that party's role in the choreography.
The local semantics is the "ground truth", it's what you would build for a real implementation.
Part of the motivation for CP is that, having written the correctness proofs for your system,
you can _stop thinking_ about the local semantics, and visualize your program in the much simpler centralized semantics.


## PolyChorλ {{ page.citations.polychor }}

After the previous two papers were published, the authors worked together on a variant system PolyChorλ,
the headline feature of which is "location polymorphism".
What this means is that a choreography can be written in terms of _roles_, and then instantiated with different parties fulfilling different roles.
Combined with higher-order choreographies, this gives a formal system that one could imagine actually writing software with,
and, as I understand it, finally brought the theory of CP up to speed with the _implementation_ of Choral. 


## HasChor {{ page.citations.haschor }}

The next big thing on the implementation side was HasChor, a Haskell library for writing choreographies.
The big deal with HasChor, aside from just having good taste in language,
is that it's _"just a library"_.
You can import it into a perfectly normal Haskell project, and use any off-the-shelf monadic function to operate on the `Choreo` monad.
Given how hard it is to get working developers to switch from one mainstream language to another,
even "interoperable" languages like Choral seem unlikely to get used much in industry.
So despite some deficiencies, HasChor has gathered a lot of attention as proof that CP has potential "in the real world".
Also, the free-monad implementation is simply intuitive!
As evidence that it's "obviously the right way" to write choreographies,
[I wrote basically the same system (worse, but the same idea) over a year earlier and before I'd ever head of choreographies](https://github.com/ShapeOfMatter/LCom/tree/f9cf5143266a91f1421886311511e96e0dcb3454).

All that said, there's one respect in which HasChor was a step backward from previous CP systems: Knowledge of Choice.
In order for a choreography to have control-flow branches, there needs to be a way to make sure
parties (not necessarily _all_ parties) agree on which branch is taken.
Basically all of the theoretical CP systems of the past decade (back to {{ page.citations.thesis }})
used a system with multiple communication operations, one of which is _just_ for communicating KoC.
The issue with such a strategy is that it's not type-directed;
in order to know if a choreography is well-formed, you have do EPP for every participant.
Since HasChor does EPP at runtime, that wouldn't be a satisfying solution.
Instead HasChor has a combined "communicate and branch" operator `cond` that broadcasts the branch-guard to all participants.
This is inefficient because not every participant will need to know every guard.


## Error Handling

One way to think about the core idea of CP is
**"If we ignore all the ways communication in a concurrent system can fail, then writing concurrent systems is easy."**
I actually think that's an important and powerful perspective;
there are a lot of contexts where it's practical to think of errors and error-handling as "out of bounds" or "out of scope".
That said, it's hard to argue that we want _more_ software around us that can't recover from failures.
_Choreographies meet Communication Failures_ {{ page.citations.RC }}
build a language Robust Choreographies that's _very much like_ choreographic programming,
but which does not assume communications always succeed.
On my TODO list is a detailed write-up of this paper; it's just one paper out of the _very_ prolific team at the University of Southern Denmark,
but so far it's the only effort I've seen to tackle the biggest hurdle to CP becoming mainstream.

There are a couple things I think are significant about this paper:
It's the only effort I'm aware of to deal with communication failures in CP. 
But also, it's not an impressive approach: basically the only recovery mechanism that seems possible under their system is "retry".
And finally, it's not entirely clear what the limits of their system actually _are_.
It's very possible I'm wrong and it's quite powerful, either case would be interesting,
and in either case it'll be interesting to see how their techniques combine with other paradigms like Enclaves-&-MLVs.

> It's impossible to summarize everything I've skipped here; my goal in the above is basically just to set the stage.
> My intention in the next post is to quickly summarize my notes from the June CP24 workshop,
> after which I'll do a post about MultiChor and my recent paper with the SoCal team. 
