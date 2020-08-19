---
title: "Getting my own domain name"
slug: "getting-a-domain"
categories: "Incidental"
tags: [
  "Personal domain",
  "DNS Record"
]
date: 2019-09-09
lastmod: 2020-03-01
---

After thinking about getting my own domain name for a while and letting the
thought rest for a couple of months, I finally bought one. It is a very easy and
inexpensive process, and I am happy I did it. The original idea was to set up my
email with it, so I could change my email provider without changing the address
(I am in the process of changing my provider, and it takes a lot of effort), but
having a domain name opens a world of opportunities.

***

Although I had known about how to get a domain for a while, I didn't have much
experience on which companies were "better" or "worse" (since I only needed a
domain but no hosting, I am not sure why a company could give me a more
appealing offer, since prices are the same in all websites). I finally decided
to go with [Gandi.net][g] because a known site uses it, I had heard about it on
the [Fediverse][f], and it looked like a good and reliable company. The hardest
part was figuring out which domain I wanted, once that was decided, buying it
took around 5 minutes.

Since I had never seen a DNS record before, configuring my email provider was a
little trickier. My provider gave me some lines to copy and paste into the
record, but they needed some modification in order to work, so it took me a
little while to figure it out. The next part was setting a landing page for my
domain: if someone saw my email address and wanted to check what
[obenedito.org][org] was all about, I didn't want them to get a 404. So I
designed a very simple page with my name and a link to my email address and one
to my GitLab account. Since I don't have a home server or a VPS, I decided to
host my page on GitLab (basically because it's free and I don't need a dynamic
website). I once again had some trouble setting up the GitLab custom domain—the
lines I was given to add to the record weren't the ones I actually needed to
add, so that took a bit to figure out as well.

I still have a lot to learn about how DNS records work (for instance the
difference between a type A or CNAME entry), but, for now, it works just fine.

*Edit*: My personal domain has been moved to [oscarbenedito.com][com].


[g]: <https://www.gandi.net> "Gandi"
[f]: <https://en.wikipedia.org/wiki/Fediverse> "Fediverse — Wikipedia"
[org]: <https://obenedito.org>
[com]: <https://oscarbenedito.com>
