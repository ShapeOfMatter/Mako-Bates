---
title: Stacked Garbling; David Heath and Vladimir Kolesnikov; 2020
date: 2021-01-19
tags:
  - circuits
  - cryptography
  - papers
citation:
  author: David Heath and Vladimir Kolesnikov
  title: Stacked Garbling: Garbled Circuit Proportional to Longest Execution Path
  howpublished: Cryptology ePrint Archive, Report 2020/973
  year: 2020
  where: Georgia Institute of Technology, Atlanta, GA, USA
---

This paper outlines a strategy for reducing the size of the object that needs to be communicated from an if-else style branch in a Yao's Garbled Circut.
The extra size-complexity from the two branch paths (only one of which will actually matter at run-time) is traded for computation-complexity (and some size-complexity that's O(n) w/r/to the number of inputs to the two branch paths; the authors assume this is small).

Remember that in the context of a boolean circuit we have to use "branchless style" programming.
This usually means that an `if B then X else Y` gets expressed as `B*X + (!B)*Y`.
Side effects aren't really an issue here, but the cost of computing both `X` and `Y` when one only needs one of them is unfortunate. 

The idea of "stacked garbled circuits" already existed somewhat. It proposes saving the _size_ (not the runtime _work_) of the duplicate branches like so:

1. Generate each of the two branch circuits deterministicly from random seeds.
2. XOR them together.
3. When the Evaluator needs to evaluate one of the branches, the seed for the _other_ branch is revealed to them (by whatever mechanism). 
4. The Evaluator can now generate (from the seed) the entierty of the branch they _won't_ be taking. They can learn as much as they want about this branch, because it's a dead-end that doesn't affect the rest of the circuit. 
5. Using XOR, the Evaluator can then retrieve the proper version of the _target_ branch (but not any artifacts from during its generation).
6. The evaluator evaluates the target branch as normal. 

Step 3 above is the hard part. Prior works have addressed the case where one party or the other knows `B`, or where mid-computation communication is acceptable. This paper avoides those more specialized cases. 

Roughly speaking, the new approach is as follows:

1. Use the two possible ciphertext wire-lables for `B` as the seeds for the encrptying the _opposite_ branch circuits, and XOR the two together. 
2. The inputs and outputs to these two sub-circuits are not their normal nominal wires; extra machinery shims in-between the branches and the rest of the circuit: 
  - The "Demux" is basically a small conditional block, switching on `B`, on each input wire, such that each branch, _iff_ it's the target branch, gets wire-lables that _do_ represent the its input values. If it's _not_ the target branch, then the Demux gives it lables representing whatever values (zeros) the Generator likes, so that the Generator can know in advance what result the Evaluator will get when they evaluate the non-target branch. 
  - The "Mux" takes the two sets of "output" values from the two branches, and returns the one that's _not_ the nonsense predetermined by the Demux. 
3. When the Evaluator is ready to evalute the conditional, they'll have _a_ lable for `B`, but they won't know which one it is. They make _both_ assumptions, that it represents True/1, and subsequently (or in parallele) that it represents False/0. 
4. Under one of the two assumptions, the Evaluator will correctly generate the non-target branch circuit from its seed, retrieve the target branch via XOR, and evaluate it to get it's output. Under the other assumption, everything they produce will be meaninless gibberish, _but the evaluator won't be able to tell the difference!_
5. The Evaluator passes the two outputs to the Mux. Whichever of them is gibberish will be gibberish that was known to the Generator in advance; the Mux will be able to filter it out and pass (a new representation of) the correct output to the rest of the circuit. Since both the Mux and Demux are themselves garbled Circuits, they're opaque to the Evaluator; the Evealuator never learns which of the two branches' outputs was the correct one. 

Thoughts: 

- "Mux" is short for "multiplex"; the noun form is "multiplexer", or "muxer". It's really hard to just write "the Mux does _x_", but that's what the authors call it.
- This can all be extended to branches with more than two paths. 
- They're explicitly relying on a Random Oracle assumption, but they mention that it might not actually be necessary. 
- Is there any possibility of cutting out the extra computation cost?

{{ page.url }} urlg
{{ page.title }} title
{{ page.date }} date
{{ page.id }} id
{{ page.tags }} tags


<table>
  {% for pair in page %}
  <tr>
    <td>{{ pair[0] }}</td>
    <td>{{ pair[1] }}</td>
  </tr>
  {% endfor %}
</table>


