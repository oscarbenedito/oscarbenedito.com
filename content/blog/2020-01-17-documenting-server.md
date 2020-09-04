---
title: "Documenting my server"
slug: "documenting-server"
categories: [
  "Self-hosting"
]
date: 2020-01-17
lastmod: 2020-03-01
---

Not long ago I realized that I could get $50 of credit on Digital Ocean with my
GitHub Student account, so I decided to try it. I transferred my website there,
and with time I started adding services. It is currently running the following
services:

- My webpage ([oscarbenedito.com][com]).
- Redirections from [www.oscarbenedito.com][wcom], [obenedito.org][org] and
  [www.obenedito.org][worg] to [oscarbenedito.com][com].
- A [Gotify][g] server through which I am able to send notifications to my
  phone.
- A static page showing traffic on my website thanks to [GoAccess][ga] (which
  analyzes Apache's log files).
- It runs [this script][gb] daily to back up all my git repositories and others
  I find interesting.
- It notifies me if any new documents are uploaded to my college Moodle using
  [this script][mun] and a cronjob.
- It notifies me every time someone logs in to the server using SSH.

As time passes I am adding more and more features to my server. In the first
place because it is fun to learn about different things and installing them, but
also because they are useful features (indeed I have tried to run other programs
which ended up not being as useful as I initially thought). I realized it is
getting to the point where if something was to happen to my server (and it got
erased), I would probably not remember how I set up everything, so I decided to
do some documentation work[^backup].

[^backup]: I know that taking snapshots of the server or making a backup every
  once in a while would solve that issue. However, that wasn't the only goal. I
  wanted to be able to rebuild my server from scratch again.

After some time, I am nearly done documenting everything that is set up and I am
pretty confident if I had to do it all again now, the documentation would be
very useful. Besides, it is also a good way of keeping a record of everything
running in the server and its configuration.


[com]: <https://oscarbenedito.com>
[wcom]: <https://www.oscarbenedito.com>
[org]: <https://obenedito.org>
[worg]: <https://www.obenedito.org>
[g]: <https://gotify.net/> "Gotify"
[ga]: <https://goaccess.io/> "GoAccess"
[gb]: <https://git.oscarbenedito.com/git-backup/> "Git Backup — git.oscarbenedito.com"
[mun]: <https://git.oscarbenedito.com/osf/file/moodle-updates-notifications.py.html> "Moodle Updates Notifications — git.oscarbenedito.com"
