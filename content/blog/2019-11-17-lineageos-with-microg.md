---
title: "Switching to LineageOS with microG"
slug: "lineageos-with-microg"
categories: [
  "FOSS",
  "Privacy"
]
date: 2019-11-17
lastmod: 2019-11-22
---

One of the things I wanted to do when switching to more privacy-respecting
providers was getting rid of Google Services on my phone. According to multiple
articles, your Android phone gathers a lot of data and sends it to Google. It is
true that my daily routine isn't a big secret, and any friend who asked me could
probably get my location, but giving it away without my (explicit) consent is a
completely different thing.

## First attempt

I first installed LineageOS on my phone in January 2019. I tried installing it
with Google Apps, but I then realized I was back with Google, so I decided to go
with [microG][mg] (a free/libre re-implementation of Google’s proprietary
Android user space apps and libraries). But for some reason—unknown to me back
then—, microG didn't work. As a result, the apps that required those libraries
didn't work either. Apps that I wasn't willing to stop using, so I switched back
to Android's stock ROM[^note].

[^note]: It wasn't actually that quick. I tried to reinstall LineageOS with
  Gapps once again, but, for some reason, it wouldn't work and the phone stopped
  working (it was stuck on the boot screen, I left it for hours). I finally got
  help from an acquaintance (we had to go into Emergency Download Mode using the
  test point) and I was finally able to go back to Android's stock ROM.

## Finding the problem

For some time I used Android's stock ROM, when, by chance, I read the following:

> MicroG requires a patch called "signature spoofing", which allows the microG's
> apps to spoof themselves as Google Apps. LineageOS' developers refused
> (multiple times) to include the patch, forcing us to fork their project.

LineageOS' developers had their reasons to refuse to do it. Luckily, the microG
project has found a solution: they forked the project to add the signature
spoofing patch. This way, you can get LineageOS with microG without having to
worry about the patching part. They also added the "F-Droid Privileged
Extension":

> [F-Droid Privileged Extension] allows F-Droid to install and update apps
> without the need of user interaction or the unsafe "Unknown sources" option.

You can find more information about the fork at <https://lineage.microg.org/>.

## Second attempt

So I tried installing microG's fork. The installation process is the same, so it
was very easy, as I already had all the required software installed on my
computer and had already done all the steps multiple times before.

This time everything turned out fine and microG libraries worked fine. I
installed the apps I needed from [F-Droid][fd] and those that weren't there, I
got from the [Aurora Store][as], an app that allows the user to download apps
from the Google Play Store without actually having it installed.

## Performance

I had my doubts on whether the apps that require Google's libraries would
function, but most of them did (and perfectly fine!), even the ones using Google
Maps—which are now using MapBox—or the ones using location services. There was
one app that didn't work, a game. I am not sure which was the problem, but I
wasn't playing the game much anyway, so I just deleted the app.

Most of the time I don't even notice that my OS doesn't have any Google
proprietary code, as it behaves (nearly) the same as if it did. If you are
thinking of moving to LineageOS, check out the fork, microG works very well!

## Final comments

There is one alternative to microG's fork (besides LineageOS itself) that is
also an "unGoogled" version of Android, [/e/][e]. Their product looks
interesting, however, I didn't need the extra features they add on top of
LineageOS so I went with the simpler option. If you are thinking about
installing /e/, you might be interested in what the [ewwlo][ew] website claims
about the project.


[mg]: <https://microg.org> "microG"
[gd]: <https://f-droid.org> "F-Droid"
[as]: <https://auroraoss.com> "Aurora Store"
[e]: <https://e.foundation/> "/e/ Foundation"
[ew]: <https://ewwlo.xyz/> "ewwlo"
