---
title: Learning Transferable Graph Exploration
date: 2021-02-08
tags:
  - machine-learning
  - graphs
  - automated-testing
citation:
  author: "Hanjun Dai, Yujia Li, Chenglong Wang, Rishabh Singh, Po-Sen Huang, Pushmeet Kohli"
  title: "Learning Transferable Graph Exploration"
  howpublished: "33rd Conference on Neural Information Processing Systems (NeurIPS 2019), Vancouver, Canada."
  year: 2019
  where: "Georgia Institute of Technology, Google Brain, University of Washington, DeepMind"
---

The authors demonstrate reinforcement learning _vis-a-vis_ graph exploration.
The specific kind of task they're concerned with is ones in which exploration _per se_ is the goal.
The two cases they consider are maze exploration and code fuzzing, but the underlying implementation targets arbitrary connected graphs. 

They're specifically using a "Graph Neural Network". This is probably best thought of as a _layer_ type (in that sense analogous to a CNN).
The key attribute of a GNN is that it's output is invariant to reordering of the inputs (and therefor doesn't assume any spatial relationship _a prior_). 

The space of actions they make available to the agent in their setup is not exactly the space of "adjacent" nodes in the graph, rather it's some more abstract action that could possibly rebuild the graph from scratch (but in practice just changes which nodes are "visited" and may "discover" new nodes). The actual training setup seems somewhat advanced, which could be a problem for replication. 
