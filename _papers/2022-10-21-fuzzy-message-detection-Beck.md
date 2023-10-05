---
title: "Fuzzy Message Detection; 2021"
date: "2022-10-21"
tags:
  - instant_messaging
  - cryptography
  - differential_privacy
citation:
  author: "Gabrielle Beck, Julia Len, Ian Miers, Matthew Green"
  title: "Fuzzy Message Detection"
  howpublished: "Proceedings of the 2021 ACM SIGSAC Conference on Computer and Communications Security"
  year: 2021
  where: "Johns Hopkins University; Cornell University; University of Maryland"
  url: https://eprint.iacr.org/2021/089.pdf
---


Some background is needed to motivate this (excellent!) paper.
End-to-end encryption is pretty normal now for anyone who wants it.
(Use [Signal](https://www.signal.org/)! It's a great message app regardless if you need the security promises.)
However, there are many things a centralized messaging system could do if corrupted, without breaking E2E encryption:

- They observe who is talking to who, and when.
  This lets them build a fine-grained social graph,
  and with even minimal external knowledge (_e.g._ during a police investigation)
  they can make good guesses about the subjects of the messages.
- They can censor individuals by black-hole-ing outbound messages from them.
- They can censor at other granularities, particularly in combination with the first point.
  To give a more clear example, suppose [jMesser](#a fake company "They're not real.")
  wanted to minimize negative press from upcoming changes to their privacy policy.
  If they have a sense of who's likely to read the new policy
  and they know who can publish commentary with a large audience
  then they could simply drop all messages between those groups of uses for a few days following the announcement.

Contrast the above with a fully decentralized messaging system like [Tox](tox.chat):
Doing any of the above bad things would require monitoring/interfering with the users' internet connections
via deep-packet-analysis, and, insofar as it's possible to mask one's IP address, any such adversary can be completely thwarted.

There are, however, a couple things a fully decentralized messenger can't\* do, which can be frustrating.

- Offline messaging, where the two parties aren't online at the same time.
- Group chat in the "rooms model.

<sub>\* "can't" is a strong word; this depends a lot on one's threat model.
[Briar](https://briarproject.org/) actually does solve these problems under it's particular threat model (which is decent!).</sub>

In short, it would solve a lot of UX _and engineering_ problems if there was a way for a centralized message server to work
without the ability to know who was talking to who.
In fact, it's not very difficult to occlude who a single message is _from_;
Signal already does this (kinda, they tried).
The hard part is occluding who the messages are _for_ while still letting the server do its job.

Early versions of [Cwtch](cwtch.im) solved this by saying
"The server should send all the messages it gets to everyone."
This more or less worked in their system because the servers themselves weren't fully centralized;
the idea is there should be lots of small Cwtch servers around.
Individual servers will only "subscribe" to the servers where they have conversations.
I don't want to get side-tracked discussing the particular threat models of Cwtch;
it's sufficient to say that this system doesn't scale, or that it's janky, whichever your prefer.

## So what's fuzzy message detection?

Fuzzy message detection is a system of asymmetric-key flagging with a controllable rate of false positives.
That is to say,

- I give you a key you can use to flag messages as being for me.
- I give the server a key it can use to check if a message is for me.
- When I create the server-key, I build into it a false-positive rate _p_, such that
  Pr\[\[`is_recipient(key,message)`\]\]=_p_ when the message isn't actually for me.
  When the message is actually for me, the probability is 1, but the server has no way of distinguishing that situation.
- The result of this is that when I check in and ask the server if they have any messages for me,
  I get all of my own messages plus _p_ fraction of everyone else's messages.
  (I can tell which are which because I can only decrypt my own messages.)

Beck _et al_ show a couple different ways of accomplishing these keys;
the mathematics are sound and may be useful in other contexts too.
More importantly (for me) is the question of what kinds of privacy guarantees the system actually gives.

The bad news is that, to provide the kind of scaling we'd hope for, _p_ should be pretty small, on the order of _1/n_
(where _n_ is the number of users, or messages, or whatever).
But the smaller _p_ gets (and it's almost certainly less than _0.01_), the worse the privacy it gives is,
_i.e._ the more certain the server can be that the messages it's sending are actually for the user in question.
One might hope that this weren't a problem;
say for example _p=10<sup>-5</sup>_ but there are a million users so only a tenth of the messages I'm downloading are actually for me.
Work showing that this idea is "wrong" has been limited, but attempting to apply differential privacy to FMD have mostly failed
(That is to say, you can do it, but only by weakening your DP guarantees to the point where they don't really matter much anymore).

I should go back to this paper now, in 2023.
It's a loose thread that may still have promise.
