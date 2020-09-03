---
title: "A lighter website"
slug: "lighter-website"
categories: [
  "Personal domain"
]
date: 2020-03-21
---

Following up with the [last post][post], I decided to make my website even
faster (which probably doesn't make a difference anymore).

## The logo

My pages (HTML only) were about 21KB (without compression), but 11KB of those
consisted of an SVG that appeared in all of them: the logo. The logo wasn't
requested from a different static file because I needed to modify it using CSS
(so that colors would change when switching to the dark theme) and, at the time,
I thought inlining was the only option to allow that. However, investigating a
little I found out there are alternatives to inlining: we can take advantage of
the `use` tag of SVGs to "inline" an SVG from a different URL. By using that, my
pages are now around 10KB of size (plus the statics files, which have a total
size of 37KB for the pages without MathJax).

## The static files

Considering that the `favicon.ico` is already 15KB, 47KB for a page is very
good! Nevertheless, I wanted to reduce it even more[^fun]. I looked into browser
caching and liked the idea. I'll explain the basics. When our browser sends a
request for a certain resource (URL/file), the server that responds can add
information that tells the browser how long it should keep the file for. If the
next time you browse that site and need the file again the file hasn't
"expired", your browser will not request it, but instead make use of the copy
previously downloaded. This reduces the number of requests made and the
bandwidth used.

[^fun]: By now you have probably figured out this is more of a hobby than
  something useful, as the size reduced is ridiculously small.

The only problem with browser caching is that if the contents of a certain file
change, your users will not see those until their copies expire. We want to
maximize the time a file is used for before requesting it again while minimizing
the time between update checks (unless our static files never change). To solve
that, I used [Hugo's Pipes][hp], which allows you to add the SHA256 sum of a
static file to its name automatically (and all the places where the file is
referenced). Now when downloading the CSS file, your browser is requesting
`https://oscarbenedito.com/css/style.min.<SHA256>.css`, which will (highly
probably) change when the contents change. Since the URL will be different, the
browser will request the new file.

## The uncompressed SVGs

I found out that SVG files where not being compressed by default[^reason]. So I
also enabled that!

[^reason]: I don't really know the reason why. It might have something to do
  with `.svgz` files. No idea.

## Final comment

My webpage is ridiculously small and all these optimizations aren't that
important. However, it is fun to learn about all of this and it can also be
helpful if in the future I have a site with bigger static files (or someone
reading this has!).


[post]: <{{< ref "/blog/2020-03-12-lightweight-website.md" >}}> "A lightweight website — Oscar Benedito"
[hp]: <https://gohugo.io/hugo-pipes> "Hugo Pipes"
