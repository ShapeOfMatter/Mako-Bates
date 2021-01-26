---
title: "Half Gates; Samee Zahur, Mike Rosulek, and David Evans"
date: 2021-01-19
tags:
  - circuits
  - cryptography
  - papers
  - garbled-circuits
citation:
  author: "Samee Zahur, Mike Rosulek, and David Evans"
  title: "Two Halves Make a Whole: Reducing Data Transfer in Garbled Circuits using Half Gates"
  howpublished: "EuroCrypt 2015"
  year: "2015"
  month: "April"
  where: "University of Virginia & Oregon State University"
---

The goal of this paper is to reduce the amount of material that must be transmitted from the Generator to the Evaluator in Yao's Garbled Circuits. 
It builds on a fair bit of pre existing work. 
As is often the case, the assumption is that only XOR and AND gates are used.
(In other contexts NOT would also be included; they don't mention Not here; probably it's not important.)

### Prior work:
- Point-and-permute: The wire lables (keys or whatever) include pointers to the rows they decrypt. Since the order/pointers are random, this doesn't leak anything. This doesn't save the Generator anything, but it saves the Evaluator some work (they don't have to try decrypting rows they can't decrypt).
Also, one no-longer has to use _encryption_ _per se_; you can use `XOR(hash,_)`. 
- Simple ("3") row reduction: One of the possible output wire labels from each gate is just a hash of the input labels. That means when it's XOR'd (per point-n-permute) you _a priori_ get all-zeros, which you don't need to transmit. (It's not 100% clear why this can only get you a 1/4 reduction.)
- "2" row reduction: A "polynomial interpolation" somehow reduces another row; how is not explained here. 
- Free XOR: By choosing the wire-lables as having a random, secret, _common_ XOR factor that relates each truthy value to it's corrisponding falsey one, one get's homomorphic XOR without consuming any material. This is compatable with 3-RR for the AND gates, but it doesn't work with 2-RR (because that has conflicting constraints on wire labels). 
- FleXOR: A refinement of Free XOR that does work with 2-RR, at the cost of not always actually giving free XOR gates (depending on the context).

### Half gates:
A half gate is just an AND gate for which one party (either, so long as we know who in advance) knows the plain-text of one of the inputs. 
If the knowing party is the Generator, then constructing the GC half-gate is just intelegently construcing a unary gate: either `const` or `id`. 
If the knowing party is the Evaluator, then the construciton is more complicated.
In both cases, simple row reduction works fine, so the unary gate requires only a _single unit_ of material. 

### Whole gates:
The key identity involes introducing a new value r, with random secret value chosen by the Generator.

> c = a AND b = a AND (FALSE XOR b)
>             = a AND ((r XOR r) XOR b)
>             = (a AND r) XOR (a AND (r XOR b))

Obviosly the first half (a AND r) is a Generator half-gate. 
Since the Evaluator never learns r, it's safe to share (r XOR b) with them; the Evaluator embeds the respective such values with the wire lables. 
Thus (a AND (r XOR b)) is an Evaluator half-gate. 
(In practice, the point-n-permute pointer does double-duty as (r XOR b).)

Since the combining XOR is free, that makes up a whole AND gate that consumes only two units of material _and is consistent with free XOR_.  
This is a relatively big dea. 


