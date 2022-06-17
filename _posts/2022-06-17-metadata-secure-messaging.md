---
title: "COMING SOON: Metadata-privacy preserving Instant Messaging"
date: 2022-06-17 12:00:00
description: "What existing tools for private massaging exist (or could exist) beyond end-to-end encryption?"
---


{% include section.html c="TLDR: Use Signal" %}

While there are a lot of really cool projects out there that I want to write about here,
[Signal](https://signal.org/) is _ok_, and you can install it and start using it _today_.  
I look forward to a day when I can update this tldr!

{% include section.html c="Metadata privacy in Instant Messaging" %}

One of my current research interests is advanced privacy-preserving IM tools. 
E2EE, done correctly (_a la_ Signal) prevents any third parties from reading your messages,
but leaves a great deal of useful information unprotected, such as

- who you're talking to,
- when you're sending messages,
- when you're receiving messages.

Various tools exist that make this message metadata harder to learn under different networking models and threat models. 


{% include section.html c="TODO" %}

- Review Cwtch
- Review qtox
- Review Vuvuzela
- Talk about group-chat
- Lay out a proposed constellation of desired properties, and systems that have already implemented them, and how they might be made to work together.

