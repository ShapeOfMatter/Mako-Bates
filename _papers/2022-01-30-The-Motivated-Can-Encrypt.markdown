---
title: "The Motivated Can Encrypt; PGP in 2021"
date: "2022-01-30"
tags:
  - usability
citation:
  author: "Borradaile, Glencora, Kretschmer, Kelsy, Gretes, Michele and LeClerc, Alexandria"
  title: "The Motivated Can Encrypt (Even with PGP)"
  howpublished: "Proceedings on Privacy Enhancing Technologies"
  year: 2021
  url: https://doi.org/10.2478/popets-2021-0037
---

This paper analyses the "long-term" continued use (or not) of PGP encrypted email among people 
with (more or less) concrete threats to their privacy and security.

The focus of this work is on the interplay between _motivation_, _context_, and _useabilty_ driving use of privacy and security tools. 
The survey respondents are people who _expected to personally need_ email confidentiality
as an extra defense against state actors or well-resourced actors, 
_e.g._ to prevent email communication being used against them in court.
Not all participants had _the same_ motivation, or the same social/organizational context, or the same technical background. 

From 2014 through approximately 2017, the Civil Liberties Defense Center (CLDC) ran workshops
teaching social-movement groups in the US to use PGP email encryption
(among other things)
using Thunderbird and Enigmail.
Participants in these workshops included activists and organizers who requested training,
student workers and volunteers expecting to pass the skills on to other acquaintances,
and acquaintances of the workshop administrators. 
In 2018 (6-40 months after-the-fact), the authors emailed all participants for whom they had contact info;
26 of the 71 responded with at least a partial survey, but only 19 responses were deemed apropos. 
The survey instrument contained a mix of choose-1-of questions, unstructured-response questions, and other structured-response questions 
(_e.g._ "For each of the following twenty actions, select all of the following four statements that apply.");
the whole survey (without responses) is about two pages of text.

An important methodological detail is buried deep in the text:
Because it would have invited extra risk to the survey pool to simply _ask_ them what kind/degree of (legal or safety) risk they faced, 
the authors asked the original workshop leaders to asses from memory which respondents they _thought_ were high or low risk. 

The authors are specifically investigating
"How do users with concrete privacy threats respond in the long term to training
that aims to overcome the documented usability issues of PGP email encryption?"
They put forth several hypotheses about use of encryption technologies: 

- Easy adoption is important for continued use.
- Personal concern about surveillance is a driving factor in adoption and continued use.
- Group motivation and use is a driving factor in personal adoption and continued use.
- People may adopt PGP email encryption and then _not_ continue using it if their peers are using other encryption technology. 

Analysis of the survey responses was done using Qualitative Comparative Analysis (QCA),
an interesting technique that I haven't read about previously and don't have sufficient perspective about.

About half the respondents were still using PGP encryption. 
Technology competence was a clear factor driving continued use. 
Roughly speaking, the conditions for continued use were found to be that
_the tool is easy to use_ and either _the person feels motivated_ or _the person is not at high risk_. 
QCA includes an independent test and assessment for negative outcomes;
in this case it confirmed the intuition of the positive-outcome path,
and also highlighted that some people stopped using PGP because they thought it was hard to use _and_ their community was using other tools.

The authors were understandably perplexed to find a negative relationship between high risk and continued encryption use. 
Probably we can make sense of this, but we should also consider the possibility that it's some sort of statistical or measuring artifact. 
Certainly the reliance on second-party risk estimation, in some cases years after the estimator interacted with the subject, is dubious. 
That said, it's not clear to me that the authors should have done anything differently; their motivation for not asking directly about risk is real. 

I think this is an excellent and valuable paper, but
I'm biased and eager for news that people are successfully using E2EE "in the wild".
Also, it would be nice to see an _even more recent_ case study, probably of a different technology. 
The landscape of E2EE communication has changed dramatically since this survey was conducted;
even in the two years between the survey and the publication it became clear to the authors
that many people were migrating to E2EE hosted instant-messaging services. 


