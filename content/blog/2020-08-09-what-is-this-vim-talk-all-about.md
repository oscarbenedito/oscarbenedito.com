---
title: "What is this vim talk all about?"
slug: "what-is-this-vim-talk-all-about"
categories: [
  "FOSS",
  "miscellany"
]
date: 2020-08-09T15:16:00+00:00
---

Oh no! Another [vim][vim] post! Well... yes. I have seen a lot of people
criticizing vim before even trying it, so I am going to try and explain my
history with it and what I like about it. If you aren't aware, vim is a text
editor that is normally used from the command line (and, normally, the mouse
doesn't work in it or is deactivated).

## Getting into vim

When I first saw people that got around a computer with the keyboard, I realized
how much faster you can do stuff when you don't use your mouse. By that time, I
used the copy/cut/paste shortcuts and that was pretty much it, I didn't even use
`Alt`+`Tab` to change between windows, so I was mindblown when I saw people
moving around so quickly without touching the mouse. For me, the keyboard was
simply a tool to write text.

Although I realized that being more familiar with the keyboard would make me
more efficient, it was hard to get used to it. I had to think before every
keystroke, and everything was very slow. GNU/Linux helped a lot with getting
more used to the keyboard, not only did I use a couple more shortcuts, but I
also found myself using the terminal often.

At some point, a friend introduced me to vim. I remember[^memory] seeing such a
weird program—and in the terminal!—and thinking: why would anyone use that?! I
was told that there were a lot of shortcuts, and experienced programmers could
move through a file very quickly with it, as well as do complex operations with
the file contents. I believed it, but I didn't want to spend years mastering
vim, so I kept going with a simpler text editor. A couple of months later, I had
a programming class where the teacher would sometimes show us his screen while
writing solutions to exercises. He was fast, very fast. He moved around the file
very quickly and the craziest part was that he was using Geany. All that speed
was reached with `Home`, `End`, arrow keys, etc. No *real* shortcuts. I think
that is the point in time when I understood what a program focused on keyboard
shortcuts (like vim) had to offer.

[^memory]: This is how I remember it, but it was—I think—three years ago, so it
  might not be completely accurate.

Since then, I have tried vim many times and, truth be told, it is hard to start
with. I also didn't code a lot during certain times, and when I had to, I just
wanted to get stuff done, so finding times to figure out vim wasn't as easy.
Another friend recommended using vim when editing Latex files because of a
plugin. I was creating Latex documents for some classes so I used vim for a
while to edit those files[^tex]. This is how I started to be able to do some
things in vim. I eventually started managing servers and used it more and
finally, at the start of the confinement, I decided to use it exclusively. It
took some time adjusting to it, but I haven't opened any other editor except for
a couple of occasions.

[^tex]: The plugin is really nice (especially when writing big amounts of text),
  but I was so uncomfortable with vim that I would write everything in vim and
  then edit/review it with a different editor.

## What I like about vim

The first thing that I like is that it is a modal editor, meaning it has modes:
you are always on one mode, and the editor responds differently to keypresses
depending on the mode. The two most basic modes are normal and insert. Insert
mode responds to keypresses like you would expect from a text editor: if you
press `x`, an `x` is appended to the file you are editing, and so on. Normal
mode, however, will not print the letter you just typed. For instance, if you
press `x` the letter under the cursor will be deleted, and if you press `w` the
cursor will move to the first character of the next word. This is great because
there are a lot of shortcuts on normal mode that are incredibly useful, and let
you move around the document without the need of leaving the [home row][hr] or
pressing modifier keys.

Now, normal mode has a ridiculous amount of shortcuts, each key has some
behavior assigned to it, so it can be hard to learn it all. In the end, it is
only a matter of practice and it is easier than it looks like. On top of that,
these shortcuts act like a language, which makes them really powerful. With
that, I mean that shortcuts can be mixed to create new shortcuts. It is hard to
explain and there are a lot of explanations online, so I will refer you to two
sources, and you can keep investigating if you are interested:

- [Your problem with Vim is that you don't grok vi][so]: A very detailed Stack
  Overflow answer.
- [Mastering the Vim Language][yt]: A YouTube video of a talk in the Boston Vim
  Meetup of 2015 by Chris Toomey.

This is it for me. The fact that you can do so many things with the keyboard
without the need to keep `Ctrl` or `Alt` pressed and do them in such a natural
"language" is what makes vim the best editor I have tried so far. Of course, you
can make other editors behave like vim ([vi][vi] really), but vim is the best
one I've tried. Well... I actually use [neovim][nv], but for my use-case, I
probably wouldn't be able to tell them apart.

## Final comments

There are still a lot of things left for me to learn about vim, especially when
dealing with a project with lots of files, but I am now more comfortable with
vim than with a normal editor where you move around using the mouse.

As you can see from this post, what I appreciate the most of vim is how it
behaves, so I could easily change to another editor that would copy this
behavior and add other features. It is useful that it is run on the terminal, as
it is normally how I move around the computer, but I don't have anything against
other editors. I also want to try [Emacs][emacs] again at some point (with [Evil
mode][em], of course), we'll see how that goes!


[vim]: <https://www.vim.org/> "Vim"
[hr]: <https://en.wikipedia.org/wiki/Home_row> "Home row — Wikipedia"
[so]: <https://stackoverflow.com/a/1220118> "What is your most productive shortcut with Vim? — Stack Overflow"
[yt]: <https://www.youtube.com/watch?v=wlR5gYd6um0> "Mastering the Vim Language — Youtube"
[vi]: <https://en.wikipedia.org/wiki/Vi> "Vi — Wikipedia"
[nv]: <https://neovim.io/> "Neovim"
[emacs]: <https://www.gnu.org/software/emacs/> "Emacs"
[em]: <https://www.emacswiki.org/emacs/Evil> "Evil mode — EmacsWiki"
