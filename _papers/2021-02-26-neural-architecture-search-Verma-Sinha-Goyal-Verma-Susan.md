---
title: Searcing for neural architecture via morphism hill climbing; 
date: 2021-02-26
tags:
  - machine-learning
  - architecture
citation:
  author: "Mudit Verma, Pradyumna Sinha, Karan Goyal, Apoorva Verma and Seba Susan"
  title: "A Novel Framework for Neural Architecture Search in the Hill Climbing Domain"
  howpublished: "2019 IEEE Second International Conference on Artificial Intelligence and Knowledge Engineering (AIKE)"
  url: "http://dx.doi.org/10.1109/AIKE.2019.00009"
  year: 2019
  month: June
  where: "Georgia Institute of Technology, Google Brain, University of Washington, DeepMind"
---

The authors are trying to make a system that can automatically find an effective architecture for classifier (convolution) neural networks. 
In this context "architecture really just means the list of layers and how they relate to each other. 
It's unclear to me what the point of this is, in the sense that I don't understand how running this whole system is better than spending the same amount of resources on the largest model you can afford. 

The basic idea is to define and a syntax of neural net architecture graphs, such that there's a finite batch of operations that could be applied to get you to a similar architecture.
They start with a more-or-less minimal graph, and use a "hill climbing" algorithm to find the final model. "Hill climbing" just means "try something and see if it's better". 

They also introduce an idea of "gradient" stopping, where they're basically only re-training the parts of the model in the vicinity of the modification. 

A couple of benchmarking experiments are provided to demonstrate that the system yields good results. 
I'm not much impressed with this paper, but I'm also worried that I've completely misunderstood it. 
