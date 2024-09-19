---
title: "Casual security suggestions for friends"
date: 2022-04-25
description: "What do I suggest for friends and family worried about their cyber security?"
---

> This was prepared for a close friend who works as an independent artist/craftsperson, and was interested in basic steps to prevent 
> compromise of banking, social-media, and other accouts. 


Hello X;

As promised, some basics for personal cybersecurity.

There are two over-arching philosophies here:
Control your attack surfaces, and have depth to your security.
Most hacks these days have both a technical component _and_ a social/personal component;
by improving technical security you simultaneously remove yourself from the pool of low-hanging fruit
and mitigate the danger of minor social-engineering slip-ups.
Mitigation and remediation matter; with sufficiently “deep” security one no longer has to “be lucky every time” Thatcher-style.

1, 2, and 3 (below) are all theoretically equally important.
I guess 3-1-2 might be the right order, but anyone who could say definitively would insist you need them all.

1. Keep your devices/software up to date.
  - You're probably already doing this. Anyway it's really important.
    Getting every update the day it's pushed isn't important, but falling substantially behind would leave you
    vulnerable to a _local_ compromise of the device or browser, which would render much of
    the below moot.
2. Reduce your surface area. Basically, don't expose yourself to vectors of attack unnecessarily.
  - Use an ad-blocker. Advertisements (and the many less visible marketing-adjacent stuff webpages include) are malware vectors.
    Finding an excellent strategy here is a big subject that I know only a little about.
    My setup:
       - [uBlockOrigin](https://ublockorigin.com/) : This is an aggressive block-list based ad-blocker. It's a classic, it's trusted and effective,
         and it's the one I most often notice actually doing anything.
       - Firefox: Out-of-the-box, Firefox is pretty tight security-wise.
         It has a light ad-blocker built in, and a variety of other protections (https-everywhere, dns-over-https) are now just switches in the settings.
       - [Privacy Badger](https://privacybadger.org/) : This is also an ad-blocker, but it works in a completely different way:
         it uses behavioral heuristics to guess what it should block.
         Mostly I only see it blocking embedded SoundCloud widgets.
  - Your phone is difficult.
    Supposedly Android-level ad-blockers exist, which would be nice because a lot of apps contain ads; I've never set one up.
    I don't know what your options are for Chrome on Android; switching to Firefox would probably be good.
    (I mostly use "Firefox Focus", I would not assume that's what you want.)
  - Installing a new app, program, or plug-in is itself an opportunity to compromise your machine.
    It's also a future vector: If the provider of that app ever gets compromised or bought out, they could push malicious updates to you.
    This doesn't mean you shouldn't install stuff, but you should _hesitate_.
  - Similarly, it makes sense to uninstall stuff you're not using, but this is easy to forget.
    My basic strategy is to wipe my laptop/phone every couple years and re-install a fresh OS.
3. Secure the accounts themselves
  - Use MFA.
       - **If you're not using a password manager, then this is probably your only strong layer of protection.**
       - Set it up on any "important" account that will let you.
         This is not just stuff that would be expensive/bad to get compromised;
         it's also any account that would help an adversary get access to other accounts (email!).
       - Text-message MFA is ok; it's security vulnerabilities probably aren't important for you or me.
         But app-based MFA is _better_; it's more secure and **it's easier to use.**
         I use LastPass Authenticator for everything I can (it uses a general-purpose protocol, lots of stuff works with it).
         For jobs/school I sometimes have to use Duo Mobile, which is fine.
         And my gmail account uses google's integrated Android MFA.
  - Use a password manager.
       - This is a big step, and there are various usability considerations to think about,
         but once you get used to it it's **easier** than traditional password use.
         (Also, without it, all passwords are weak to a resourced attacker.
         Either they're too short, or they're too similar to passwords you're using on other sites.)
       - Obviously you're committing to remembering one difficult-to-remember password.
         Keeping it written down someplace _safe_ is ok!
       - Also, obviously, you'll have MFA set up for your password manager.
         Considering how you want everything to overlap, and how you want all your fail-safes configured, probably sounds like a chore.
         You don't have to do it all at once.
       - I use [LastPass](https://www.lastpass.com/). I like them; some people don't.
         Whoever you use will probably try to sell you a VPN and other services, whatever.
4. Check for existing breaches.
  - This is not a very effective thing to do in general, but there's some low-hanging items.
  - Dropping your emails and phone number into [haveibeenpwned.com](https://haveibeenpwned.com/) is generally considered safe to do.
    I think it just checks to see if you were included in any batches of hacked credentials that have been shared online.
  - Many platforms (Facebook and Google I know for sure) have a place in their settings where you can view and cancel any log-in sessions.
    This is most important when, for whatever reason, you're changing your password;
    changing the password doesn't do any good if someone is still logged in.

Hope you’re well;
--Mako
