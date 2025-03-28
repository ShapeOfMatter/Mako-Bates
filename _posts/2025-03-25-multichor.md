---
title: "Choreographic Programming part 2: The MultiChor paper"
date: 2025-03-25 13:00:00
description: "We'll present our paper at PLDI!"
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

> Regardless of whether I ever get around to "summarizing the status quo of CP",
> I'm pleased to announce that I'll be presenting our recent work at PLDI in Seoul in June.

Our paper [Efficient, Portable, Census-Polymorphic Choreographic Programming](https://arxiv.org/abs/2412.02107)
has been accepted into [PLDI25](https://pldi25.sigplan.org/)!  
This paper combines some of my earliest work on CP (the **𐤄<sub>λsmall</sub>** language, now re-named **λ<sub>C</sub>**),
my own Haskell library [MultiChor](https://hackage.haskell.org/package/MultiChor),
and Rust and TypeScript libraries by [Shun Kashiwa](https://shun-k.dev/)
that have been upgraded to be basically feature-equivalent with MultiChor.
Based on presentations at last year's PLID, I think it's somewhat likely that the basic paradigm used by MultiChor is going to be the version of CP
that sees real industry use,
and MultiChor is ready for use in the wild, except that it's missing error-handling features.

While we desperately need good ways to talk about error handling in a choreographic setting,
there's also room for improvement on the theory side.
My work in the past month has been to further reduce the complexity of the core mechanics of MultiChor,
to distinguish what's fundamental to CP from emergent development patterns.

In the mean time, read the paper and I hope to see you in Seoul! 
