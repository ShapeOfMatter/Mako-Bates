---
title: "Iconography for key-fingerprint comparison"
date: "2022-02-16"
tags:
  - usability
citation:
  author: "Joshua Tan, Lujo Bauer, Joseph Bonneau, Lorrie Faith Cranor, Jeremy Thomas, and Blase Ur"
  title: "Can Unicorns Help Users Compare Crypto Key Fingerprints?"
  howpublished: "Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems (CHI '17)"
  year: 2017
  month: May
  where: "Carnegie Mellon University; Stanford University; University of Chicago"
  url: https://doi.org/10.1145/3025453.3025733
---

This paper considers a handful of solutions to the problem of key comparison. 
When using cryptography, particularly for secure communication,
it is often necessary for a human to look at a key (a modestly string of binary data, that can be represented various ways)
and say if it's the same as some other known key. 
In practice, the "null" solution isn't even direct comparison of keys, but rather comparison of key "fingerprints", which are just hashes.

It was known prior to this paper that fingerprint validation was a usability problem in asymmetric cryptography. 
Several approaches have been tried,
many of which introduce a graphical component on the supposition that humans will have an easier time comparing images than strings of gibberish. 

The core of the experiment was a "roll playing" game on AMT,
in which the participants judged fingerprint representations to be the same or different, in a pretend context. 
Participants were randomly assigned to a particular style of fingerprint representation, and performed comparisons for about 30 minutes.
Afterward, they were given the opportunity to review missed cases and provide commentary. 
The representations chosen were: Hex chunks, Word-like alphabetic strings, Random words, Random numbers, Randomly generated grammatical sentences,
OpenSSH Visual Host Key, Abstract art, and Representative art (depicting unicorns). 

The representational art performed the _worst_, and the grammatical sentences performed the best. 
In general, the ability of humans to perform these judgments seems insufficient. 

### Highlights

I've used fingerprints like these on a few occasions.
Similar techniques seem to have caught on for account avatars:
if everyone's avatar is deterministically-random based on their account ID,
then it's easy to know who you're talking to without actually reading their name.
In this sense the author's findings are discouraging, but there are some details we should note.

- The weakness of graphical representations seems to be that they encourage _brief_ comparisons.
  This isn't a problem in situations where a detailed comparison is already unlikely.
- The authors have some suggestions for extending the applicability of _automated_ comparisons, for example by using QR codes.
- Human comparison of fingerprints is clearly _possible_, even if it's often _impractical_. 
