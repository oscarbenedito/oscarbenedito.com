<!-- title: A lightweight website -->
<!-- slug: lightweight-website -->
<!-- categories: Personal domain -->
<!-- date: 2020-03-12T00:00:00Z -->

Since the start of this site, having a lightweight website has been one of my
priorities. Every file served has been minimized, you won't see any pictures
that aren't vector graphics (except for the `favicon.ico` file) and users don't
need to download fonts or JavaScript libraries. On top of that, the amount of
JavaScript required is minimum. Indeed, as of right now, the only JS that runs
is a very simple function to toggle the theme and another one to open the
navigation menu on small screens. That results in super lightweight pages, which
keeps the loading time to a minimum and reduces the bandwidth usage of the
server.

The one thing I've had doubts about is minimizing HTML. Some friends argued that
minimizing the code obscures it, while I argued that it is easy to *prettify*
HTML with one of the many tools online. However, lately, I have been a bit
frustrated with Hugo's minimizing tool as it had some unexpected behavior with
SVG's, so I decided to investigate the pros and cons of file minimization a bit
further.

When you access a webpage it is normally compressed (if the server supports it),
and this compression makes the previous minimization of files almost useless.
Let me explain: my main blog page's size is about 18.3KB, but it can be reduced
down to 17.2KB with Hugo's minimizing tool[^errors]. Once compressed with
[gzip][gz], the sizes are 5845 and 5747 bytes respectively, so the bandwidth
save is only 100 bytes! Similar results have been obtained for all the pages of
the site that I have tested, so it looks like minimizing isn't helping that
much.

[^errors]: It is actually 15.5KB, but that includes errors on the SVG's
  minified, once fixed, it becomes the 17.2KB mentioned.

On the other hand, I see the point made by the friends who argue that having the
code available when pressing `view source` can be useful, even if code could
potentially be prettified. Given this, I have decided not to minimize the HTML
files. A similar argument could be made to not minimize CSS and JS (indeed, in
the future I might change my mind), but they will stay minimized for
now[^css-js].

[^css-js]: These files can be found more easily on the source code since they
  are not build up from templates, and it is uncommon to view the source code of
  those files, as they are normally viewed from the browser's inspection tools.
  On top of that, CSS is "compiled" from SCSS files, and once again, these files
  are easily reachable at the public repository of the website. Finally, the
  change in size is higher (1.5KB for the CSS file).


[gz]: <https://en.wikipedia.org/wiki/Gzip> "gzip — Wikipedia"
