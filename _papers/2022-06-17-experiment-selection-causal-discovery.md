---
title: "Experiment Selection for Causal Discovery; 2013"
date: "2022-06-17"
tags:
  - causal_graphical_models
  - experiment_design
citation:
  author: "Antti Hyttinen, Frederick Eberhardt, Patrik O. Hoyer"
  title: "Experiment Selection for Causal Discovery"
  howpublished: "Journal of Machine Learning Research 14"
  year: 2013
  where: "Helsinki Institute for Information Technology; California Institute of Technology; "
  url: https://www.jmlr.org/papers/volume14/hyttinen13a/hyttinen13a.pdf
---

I read this paper as part of a research project to buid a static analysis tool for validating experiment design.
While the basic _model_ that they're operating within is the one we want, it's not clear yet what of the results they summarize we can actually use.

### Common assumptions:

- Acyclic: as usual. We could take this assumption provisionally...
- Causal Sufficiency: There are no un-observed causes common to multiple observed variables. 
  Like Acyclicity, this would appear to apply to the STS engine, because most variables will be _a priori_ dependent or independent, 
  but even if that's true there could still be cycles/unobserved common causes between the dependent variables. 
- Faithfulness: What does this even mean?
  Observed independence is "real" in the sense that it's not a causal dependence that happens to be tuned to look like independence, I think...
- Parametric Form: Dependencies between variables have simple parametric structures, _e.g._ linear. 

### Common conditions for experiment sets:

These are frequently quantified over all pairs of verticies:

- Unordered Pair Condition for {x, y}:
  There exists experiment E=(J,U) in {E...} such that x in J and y in U OR visa-versa. 
- Ordered Pair Condition for (x, y):
  (x != y)
  There exists experiment E=(J,U) in {E...} such that x in J and y in U.
- Covariance Condition for {x, y}:
  There exists experiment E=(J,U) in {E...} such that x and y are both in U.

The discussion on page5 suggests that we don't really care about the Order Pair Condition?

Some more set-oriented properties:

- Separating system:
  C = {J...} where all J are subsets of V, and for all (distinct) x,y in V there exists J in C such that x in J and y not in J OR visa-versa.
  This corrisponds with a set of experiemnts satasfying all possible Unordered Pair Conditions.
- Completely Separating System:
  C = {J...} where all J are subsets of V, and for all (distinct) x,y in V there exists J1,J2 in C
  such that x in J1 and y not in J1 AND y in J2 and x not in J2.
  This corrisponds with a set of experiments satasfying all possible Ordered Pair Conditions.
- (Undirected) Cut covering:
  A set of cuts of an undirected graph such that the union of all the edge-sets contains all edges.
- Directed Cut Covering:
  Remember that a directed cut (J,U) only cuts the edges from J to U. 
  A directed cut covering is the same as an undirected cut covering, but for directed graphs/cuts.

> Fig.3 (page9) shows how to construct experiments satasfying all Unordered Pair Conditions.

> Fig.7 (page14) and Algorithm 2 show how to construct a minimal (w/r/t intervetions) batch of experiments of a fixed size
  while satasfying all Unorder Pair Conditions.

- Antichain (aka Sperner system):
  Antichain {Si} over a set S is a family of subsets of S such that no Si is a subset of another. 
  Is it also supposed to cover S? the subsequent use of the term makes more sense if that was the intent.

> Fig.6 (page12) shows how to construct experiemnts satasfying all Ordered Pair Conditions.

> Getting minimal experiment batches satasfying all Ordered Pair Conditions is more complicated,
  and depending what's being minimized may not even be a generally solved problem? 
  Section 5.2 (page16) covers this.

### Background Knowlege

Given a graph with vertecies/variables V, there are O(|V|^2) pairs of vertecies,
which means we may be interested in O(|V|^2) [Un]Ordered Pair Conditions. 
Much of the domain/background knowlege we might bring into a problem can be represented by "checking off" pair conditions as unnecessary. 
Instead of searching for minimal cut coverings of _complete_ [un]directed graphs over V, we can consider incompletely connected graphs.

Doing this in a minimal way is NP-hard, and basically reduces to graph-coloring.
This isn't bad: existing aproximations of the graph coloring problem can be applied without additonal loss.

When

- The underlying model is acyclic
- and causally sufficient
- and the background knowlege is from passive observation or "suitable" previous epxeriments
  (why should this matter?)

then we can (usually? depending on the observability of a "skeleton"?) consturct a Markov Equivilence Class
representing the possible underlying models that the background knowlege would be incapable of distinguishing.

