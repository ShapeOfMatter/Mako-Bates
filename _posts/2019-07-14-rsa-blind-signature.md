---
title: "RSA Blind Signature"
date: 2019-07-14
description: "An open-source implementation in C++"
---


Way back in 2019 as part of an attempt at an e-cash system, I put together an implementation of the basic RSA Blind Signature algorithm;
that code can be found [here](https://github.com/ShapeOfMatter/RSA-Blind-Signature), it's pretty small.

A blind signature is like any other cryptographic signature;
for some message `M`, `Sig(M)` is trustworthy evidence that some specified party _signed_ `M`.
A blind signature is different in that the signing party (the "Server", if you like) doesn't ever learn what it was that they signed.
Note that this is different from an HMAC or other simple hash-based systems where the Server doesn't _need_ to know `M`;
even if the Server is later presented with the `(M_1, Sig(M_1))` pair, they won't be able to tell _which_ of the (presumable multiple)
signature-creation events they participated in that pair corresponds to.

The original Blind Signature paper was published by David Chaum in 1982/83, and it's a very '80s crypto paper,
meaning that almost nothing we would consider real cryptography appears in it.
There are no citations, and critical details like "how do I actually do any of this stuff" are left as an exercise for the reader.
[The paper](http://www.hit.bme.hu/~buttyan/courses/BMEVIHIM219/2009/Chaum.BlindSigForPayment.1982.PDF)
is still interesting because it _starts_ from the application that is still most closely associated with blind signatures: e-cash.
The idea that you could go to a bank (or a bank's website, etc), and instead of withdrawing cash you'd buy a batch of blind signatures
on chits (hashes, nonces, etc).
The bank would deduct corresponding funds from your account, and anyone you gave the tokens to could redeem them for money at the bank.
This has all the _privacy_ advantages of cash, and the security/censorship \[dis\]advantages of old-school checks,
and it takes just fine to an all-digital online implementation.

Blind signatures can be used for electronic voting, although he seems less interested in that possibility.
More recently, [Martiny, Kaptchuk, _et al_](https://cs-people.bu.edu/kaptchuk/publications/ndss21.pdf)
suggested their use to avoid DDOS attacks (in the context of a suggested improvement to Signal's sealed-sender process).
In various contexts (with limitations) blind signatures allow a compromise between the privacy of peer-to-peer infrastructure,
and the ease and efficiency of centralized infrastructure.

