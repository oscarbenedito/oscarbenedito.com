---
title: "Securing communications"
slug: "securing-communications"
categories: "Knowledge base"
tags: [
  "Cryptography",
  "Software",
  "Privacy",
  "Security",
  "Encryption"
]
date: 2020-01-12
lastmod: 2020-08-10
---

We use cryptographic techniques daily without really knowing how they work, so
I'm going to try and explain some basic concepts. Let's start with Wikipedia's
current definition:

> Cryptography or cryptology is the practice and study of techniques for secure
> communication in the presence of third parties called adversaries.
>
> --- *[Wikipedia's cryptography entry][cry]*

One cryptographic process we are all familiar with is encryption, that allows us
to change the contents of a message so only certain people with a "key" can
decipher and read it. A simple—and well known—example of encryption is the
[Caesar cipher][cc] (if you haven't heard of it, check out how it works!).

Let's consider the following scenario with three people (or parties): Alice, Bob
and Craig. Alice wants to contact Bob privately, while Craig is trying to
eavesdrop. This is all happening through a network, in this particular scenario,
they are communicating through the mail. Craig works at the postal office, so he
could get Alice's letter, open it, read it, put it back in a new envelope that
looks exactly the same as Alice's and then send it to Bob.

Craig's attack is known as a man-in-the-middle attack, happening when the
attacker is able to secretly relay information between two parties (and with the
ability to change the contents of the communication). This attack isn't
particularly hard to carry out on the Internet, but we are normally protected by
cryptographic methods (that ensure the privacy and authenticity of our
communications).

## Encrypting a message

Alice knows about the flaws of the mail system, so she decides to encrypt her
message. She could use the Caesar cipher. If Bob knows how much Alice "shifted"
the alphabet, he will be able to read her message, while Craig won't. Or will
he? Couldn't Craig just try all the numbers from 1 to 25 and just see which one
gives a message that makes sense? And how did Alice tell Bob how much she
"shifted" the alphabet without Craig reading it?

Those are good points. We currently use better encryption methods than the
Caesar cipher that tackle these issues. The first concern is talking about a
brute-force attack (when the attacker tries many keys in order
to—eventually—find the correct one). We can protect our messages against
brute-force attacks by using an encryption method that admits a huge number of
different possible keys. How big? If you create a key with GPG, the minimum key
size is 1024 bits (which gives us 2<sup>1024</sup> different possible keys). How
hard would it be to crack it? [This video][yt] explains it pretty well for a key
that is 256 bits long (2<sup>256</sup> possible keys). First problem solved! Bob
isn't deciphering our letter anytime soon!

About the second issue... How can Alice tell Bob her secret password before they
can encrypt anything? It turns out she doesn't need to do that at all! She can
use asymmetric cryptography to solve this problem. In asymmetric encryption,
everyone has two keys[^nodetail]: a public key and a private key. Our public key
will be *public*! Everyone can know it (and that won't put our encrypted
messages in danger), while our private key will only be known to us. When using
asymmetric encryption, we encrypt messages using someone else's **public** key,
but only someone with the **private** key will be able to decipher it.

[^nodetail]: These pair of keys are created in a particular way (that "links"
  them). I won't get into detail on how it works (it is beyond the scope of this
  post), but there is a lot of information on the Internet if you are
  interested.

So now Bob can simply send Alice his public key, which she will use to encrypt
the message. Only Bob with his private key will be able to decipher the message.
A system of communication that is resistant to Craig's attacks, so far...

## Signing a message

Craig can't decipher the message, so he might try another strategy: change it!
He will get Alice's letter, destroy it, and send a different one to Bob (making
it look like it came from Alice). The communication is private, but not secure
yet!

Once again, cryptographic techniques come to the rescue with the ability to
digitally sign messages (also using asymmetric cryptography). What signing a
message does is kind of the opposite of encryption: Alice can use her
**private** key to sign her message, which will output a new file (the
signature). Now, anybody with the message, the signature made by Alice, and her
**public** key can check that the message was signed using Alice's private key,
therefore ensuring nobody changed it (signatures are different for different
messages).

Now, Craig can still destroy the message and send a different one. However, Bob
will realize there isn't a signature (or the one given doesn't match the
message). This will alert Bob that the contents of the message might indeed not
come from Alice. Bob might not be able to get Alice's message, but Craig will
never be able to impersonate her.

## Final notes

The problem with the digital signature is that there has to be an initial
contact that both parties know has not been compromised[^sharingpk]. This could
be achieved by meeting in person and exchanging keys, although that could be
hard for two parties that live in different parts of the world trying to talk
over the Internet. There are methods to work around this problem, although none
is perfect.

[^sharingpk]: If not, the first time Alice sends her public key, Craig could
  change it a different one and therefore being able to successfully sign
  messages with what Bob trusts is Alice's private key.

Hopefully, this post gave you a basic overview of some things that can be done
using cryptographic techniques and how they are necessary when securing our
online communications.

*Edit*: Invidious link has been changed to YouTube as Invidious instance is
shutting down.


[cry]: <https://en.wikipedia.org/wiki/Cryptography> "Cryptography — Wikipedia"
[cc]: <https://en.wikipedia.org/wiki/Caesar_cipher> "Caesar cipher — Wikipedia"
[yt]: <https://www.youtube.com/watch?v=S9JGmA5_unY> "How secure is 256 bit security? — YouTube"
