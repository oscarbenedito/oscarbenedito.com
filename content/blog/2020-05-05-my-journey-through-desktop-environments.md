---
title: "My journey through desktop environments"
slug: "my-journey-through-desktop-environments"
categories: [
  "FOSS",
  "Miscellany"
]
date: 2020-05-05T19:26:00+00:00
lastmod: 2020-05-06T07:52:00+00:00
---

My first experience with GNU/Linux was with KDE. It is the desktop environment
used on my college computers, and it was more or less the only experience I had
with the GNU/Linux operative system, so it was the desktop environment I
installed at home (at that point I don't think I knew the difference between a
distribution and a desktop environment). After some time, I got comfortable with
the new OS and learned that distributions and desktop environments were
completely different things, so I started to look around for other DEs and
decided to go with GNOME. It was a weird choice, as I had only read—and
heard—bad things about GNOME, but I was reading a lot about the GNU project and
decided to go with the DE that was part of the project, just to try it out.

Well, GNOME is great. I love GNOME! I am glad I wanted to try it (for a more or
less stupid reason) against what people were writing/saying. It works great out
of the box, it has programs for everything I needed and can easily be configured
to fit your needs[^detail]. With Debian 10, the dark theme is great, and other
apps like firefox also go dark with it[^not-gnome]. It was a bit confusing the
first couple of days, but it was easy to get used to. GNOME has worked great for
me (and still does). With the lack of a bar with all the open windows (like on
KDE), I have gotten more used to moving around with the keyboard. I also made a
conscious effort to use the keyboard more, as I had seen many people move around
faster and more naturally when they weren't using the mouse. So, after gaining
confidence with the keyboard, I decided to finally give i3 a *real* shot a
couple of weeks ago.

[^detail]: A very simple example is setting up "natural scroll" for the
  trackpad, which I had a couple of issues the first time I tried with some DEs.
  But there are many things.

[^not-gnome]: I know this feature is not exclusive for GNOME (indeed, I
  configured i3 to act like this), but it works out of the box, which is the
  point I am making.

[i3][i3] is a tiling window manager, which means that it is a window manager
that arranges windows in a way that they don't overlap. A window manager is the
software that manages your windows (resize, move, close, etc.). The difference
with desktop environments is that the latter come with a window manager, but
also many more programs (like a terminal emulator or a text editor) as well as
panels, system menus, and other features. These normally all look alike and work
well together.

I say I decided to give it a *real* shot because I have tried i3 multiple times
before: mainly logging in, seeing how ugly everything looks, logging
out[^hidpi]. This time it was different: I had time to figure everything out, so
I decided to push through the first days (when everything is to be configured"),
and then decide. I installed it, tweaked it a little, didn't like some things,
installed [sway][sway], it fixed some things but messed up others, I also
considered other tiling window managers like [dwm][dwm], and went back and forth
a couple of times (all in one day). Eventually, I decided sway had one problem I
couldn't cope with[^sway] and decided to stick with i3. I made a list of
everything that was missing (or "wrong") and went to bed.

[^hidpi]: I have a HiDPI screen which made everything look super tiny. I had
  some issues with HiDPI screens with KDE (there was always a weird app that
  didn't work well with it). This got solved (out of the box!) with GNOME, and
  after all the frustration I had in the past, seeing it back was a nightmare.
  This was finally solved pretty easily, although the solution is a little hacky
  so I can also plug my computer into non-HiDPI screens.

[^sway]: The problem is that applications using Xwayland are blurry on HiDPI
  screens, and that wasn't solvable as far as I could tell. They also had no
  plans to solve it anytime soon (according to sway developers, it is an
  Xwayland problem, and it's on them to fix it, which is a fair point).

The next day, I grabbed the list and started working on the items. Some of them
were very easy to fix, like make the sound buttons work. Some others were a
little harder, like mounting USB automatically. I even had to reinstall i3—a
fork of i3 actually—so I could have gaps between windows (yes! I needed those!).
I also added more items to the "problems-to-fix" list as I kept using i3. After
about a week, I had fixed everything on the list!

This process of going through a lot of minor things made me realize how awesome
GNOME is. It has so many features, without a need for the user to spend hours
and hours making everything work. KDE probably also goes into this category, but
I haven't used it as much so I can't say. Other DEs that I have tried have given
me some problems here or there, nothing major, but it isn't the out-of-the-box
experience I appreciate in GNOME.

Some people quickly disregard these DEs because they are "bloated". In my
opinion, it is true. They have an absurd number of features, but for myself,
when I simply need everything to work without any tweaking, this is great. As a
new GNU/Linux user, I wanted my computer to work without much configuration,
while still being able to be "picky" about some stuff. Even as a
moderately-confident user, I didn't have a week to spend making i3 look and act
as I wanted. For all my little things to be included, there are probably many
more that I don't want, and are also included (and other people want). I am fine
with my desktop environment being bloated. That changes for pretty much any
other software I run on my computer, I like simple things, but I also don't have
unlimited time. Indeed, my initial reason to switch to i3 (or a tiling window
manager) wasn't "less bloat" or simplicity[^less-bloat] (I find GNOME very
distraction-free, and it has a good performance on my computer). I switched
because I was tired of overlapping windows and I wanted to make more use of my
keyboard for managing everything.

[^less-bloat]: Now that I have tried it and feel comfortable, my next
  installation might come without GNOME and probably have much less bloat, which
  I will appreciate for sure. It simply hasn't been a priority so far.

With all the changes, I am very satisfied with i3, and haven't gone back to
GNOME for a week. It did take a lot of time to figure everything out (and
configure it), but it was something I had wanted to do for a long time (that's
why the many attempts) and I finally had extra time to do it. It was definitely
worth it!

## Final note

I think one of the major issues I had on my previous attempts was the `$mod` key
used for all i3 shortcuts. It is so hard to reach the `Super` key! I had already
switched the mapping of `Caps lock` and `Escape` (which improved my vim
experience drastically), so I knew `Caps lock` was the key I needed for my
shortcuts (it is so easy to reach!). I have now mapped `Caps lock` to act as
`Escape` if I tap it, and as `Super` if I hold down. With this little trick, i3
becomes a lot nicer, but without damaging vim's experience. If you are
considering using a tiling manager, think about it! Also recommended if you use
vim!


[i3]: <https://i3wm.org/> "i3"
[sway]: <https://swaywm.org/> "Sway"
[dwm]: <https://dwm.suckless.org/> "dwm"
