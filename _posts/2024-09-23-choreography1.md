---
title: "Choreographic Programming part 1 of 3?"
date: 2024-09-22 13:00:00
description: "A cursory history of Choreographic Programming"
citations:
  haschor:     <a href="https://dl.acm.org/doi/10.1145/3607849" title="the HasChor paper"              >[1]</a>
  choral:      <a href="https://www.choral-lang.org/"           title="the Choral website"             >[2]</a>
  chor-lambda: <a href="https://arxiv.org/abs/2111.03701"       title="the Chorλ paper"                >[3]</a>
  RC:          <a href="https://arxiv.org/abs/1712.05465"       title="the Robust Choreographies paper">[4]</a>
  pirouette:   <a href="https://arxiv.org/abs/2111.03484"       title="the Pirouette paper"            >[5]</a>
  polychor:    <a href="https://arxiv.org/abs/2303.04678"       title="the PolyChorλ paper"            >[6]</a>
---

> In this sequence of posts I'm going to try to summarize the state of research into Choreographic Programming (CP),
> it's recent past, status quo, and what I anticipate happening soon.
> I'm assuming any readers already have a basic sense of what CP _is_;
> if not, I'd suggest readers familiar with Haskell to start with the HasChor paper {{ page.citations.haschor }}
> and other readers to start with Choral {{ page.citations.choral }}.

The vibe among people who've been working on choreographic programming (CP)
is that CP is _about_ to become a mainstream way of writing concurrent systems.
I think there's a sense in which that's true, and I also think the situation could be much improved.
In preparation for describing my own research plans for the next year, I figured I should summarize my understanding of recent history.
There's inherent risk in writing any such thing: I'm going to get it wrong and I'm going to omit important stuff.
In fact, in this post, I'm only going to discuss six papers.
Part two will summarize my notes from the recent CP workshop at PLDI 2024.

## Choral: Object-oriented Choreographic Programming
papers to talk about:
2017 12 communication failures
2020 05 choral
2021 11 pirouette
2021 11 chor-lambda
2023 04 polychorllambda
2023 08 haschor

