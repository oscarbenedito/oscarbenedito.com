<!-- title: Switching to my own static site generator -->
<!-- slug: switching-to-own-ssg -->
<!-- categories: FOSS, Personal domain, Projects -->
<!-- date: 2020-09-27T16:27:00Z -->

Since the start of this website (its first anniversary was a couple of weeks
ago!) until recently, I have been using the static site generator [Hugo][h].
Static site generators are very useful when building relatively complex static
websites, and Hugo has served me well. I have also used [Lektor][l] and
[Jekyll][j] before for other projects, but for a site with a blog, I like Hugo
the most. However, with time, some issues have arisen with Hugo, and I finally
decided to change my site's generator.

## Issues with Hugo

If you build your website with a static site generator, it will probably be the
most critical dependency of your site. Of course, it's a dependency I'm fine
with as it makes things much easier (dealing with Markdown content, categories,
web feeds...), but if something goes wrong, the site won't render as you want.
Hugo in particular is a very big project and I don't feel like jumping into the
source code every time I have an issue with the program (especially since I've
never used Go, and I don't want to spend hours for minor annoyances). Although
Hugo works wonderfully, I have encountered moments where it has acted
unpredictably, and documentation doesn't help most of the time.

On top of that, although it works perfectly well (and it is one of the most
popular SSGs), it is on a beta stage and the developers have made
backward-incompatible changes without warning in the past. The change I have in
mind was clearly stated on the release page, but I normally let my package
manager handle the updates, and I want my computer to keep working correctly (or
throw big red warnings all over the place). In this case, HTML inside Markdown
files stopped rendering, and I only found out coincidentally a couple of weeks
later as the web feed was not valid anymore. From that moment on, I started
checking the release notes for every update (which are frequent, about once a
week), but it was an annoying routine.

I understand that the program is in beta and it was on me to check for breaking
changes, but to be fair, Hugo is marketed as a fully functional program (as if
it wasn't on a beta stage) on the official website. Considering my last issue,
this was concerning and ended up creating uncertainty on the stability of Hugo
and the transparency of the developers, so I decided to change my site
generator.

## Taking the leap

I wanted to move to something lightweight that could still be useful in a few
years' time, ideally a program that was easy to understand and maintain. The
problem was that I had some very specific needs that small programs didn't
fulfill, leaving only big programs as an option (which I didn't want to use). I
thought of the possibility of creating my own site generator, but it looked like
a large task I didn't want to spend my time on. Hugo was working fine, and
although I kept looking up other SSGs when I discovered them, I stopped actively
looking for alternatives or thinking about designing my own.

Until the night of the 5th of September, when I came across [makesite.py][ms].
This project was just perfect, and I couldn't resist. Let me show you an extract
of the README:

> Have you used a popular static site generator like Jekyll to generate your
> blog?

Yes...

> I have too. It is simple and great. But then did you yearn to use something
> even simpler to generate your blog? Do you like Python? Perhaps the thought of
> writing your own static site generator crossed your mind but you thought it
> would be too much work?

Yes, yes, and definitely yes!

> If you answered "yes" to these questions, then this project is for you.

Nice! That night I read the README and the source code (which is shorter than
the README). The program is very simple and a lot of the basic functionality I
needed out of a static site generator was already there. On top of that, it
didn't use any non-standard Python library except for the Markdown parser. I
really liked the project and I thought it could be the foundation of my personal
static site generator.

It was. The next morning, I started coding to make it usable for my website. I
had to implement many new features, but with Python it was [easy and fun][xkcd].
After two days of working on it, I finally released my site using a personal
fork of makesite.py, [gensite.py][gs]!

## The new benefits

So, why change the SSG if Hugo was working fine? As I said, I've had my issues
with Hugo, and I don't want to be forced to leave my static site generator if
more arise in the future. I don't know if I'll be able to switch SSGs when (and
if) the time comes, and now I have the time and motivation needed to do it, so I
decided to take the chance while it was there. On top of that, *gensite.py* is
not only my "way out of Hugo", it is a program that has many features that could
have made me do the change without having any troubles with the last SSG.

First of all, the program is very small, it's only about 270 lines of code and
it's written in Python. That makes it very easy for me to read and understand
the whole program very quickly, even if I have completely forgotten everything
about it. Obviously, this doesn't count the lines of code of the libraries it
depends on, but those are all standard libraries and the functions are easy to
understand, except for the Markdown parser, but if that ever gives me any
trouble I can change it without much effort.

Since *gensite.py* is made exclusively for my website, it is more closely tied
to the rest of my site. For example, it doesn't have a complex template engine,
instead, templates only process the following two snippets:

- `{{ var }}`: substitutes the string for the value of variable `var`.
- `{{ _if var }}text{{ _fi }}`: will render the text `text` if variable `var` is
  defined. You can't have an `_if` inside another.

If I need anything more complex, I will use Python to create the text and pass
it as a variable when rendering the template. I prefer this approach as it is a
lot nicer to implement those features in Python than it is with a template
engine. For some pages—for example, the archive—Python does some more heavy
lifting and creates part of the HTML. This can sound weird in comparison with
other static site generators, where HTML is only dealt with in the template
files, but it makes things simpler, and I no longer need hacky templates to
create certain outputs.

Moreover, I like the file structure a lot better (I designed it!), and if I ever
want to change it, it shouldn't take long to do so. Similarly, any other design
options are exactly as I want them to be, since it is me who decided them. In
case it is not clear: everything works exactly as I want it to!

Finally, it's a project that doesn't move too fast. One of the problems with
websites is that links are easily broken: entities change their backend, run out
of money, mess up an update, etc. and let their links break. Right now, I am
pretty dedicated to my website, and if my SSG broke something on my website, I
would spend the time to fix it, but I can't ensure I'll do the same in two or
five years (and I don't want to break any links, even on the long term, but
that's a post for another day). Unless something happens with Python,
*gensite.py* will work and so will the generation of my website. There won't be
any updates that break some random page or that change a certain behaviour[^u].
I hope *gensite.py* can stand the test of time, but we'll see...

[^u]: Also, whenever I make changes to *gensite.py*, I can run `diff -r` to
  check for differences for the outputs before and after the update. With Hugo,
  many files changed without explanation (although it was mostly style choices,
  it made it hard to see the real changes in content between updates).

## Final comments

Forking *makesite.py* and setting up everything I needed for my website was very
fun, but it is surely a process that not everyone will enjoy. I have lately been
leaning towards software that is a simple as possible, software that is easy to
understand and change if needed. It takes time to set up, but once it's working,
you can forget about it (and if you need to make changes, they are quickly
implemented) and you will have software that works exactly as you want it to. I
am very meticulous about this website and try to have good control over
everything that happens during the website's generation, and I couldn't be
happier with *gensite.py*.

On another note, I don't want to end this post without saying that Hugo has been
a great static site generator, and I'd recommend it to anyone who wants to have
a blog on a static website. In a new update with breaking changes, they did
throw errors if the old feature was used, so maybe my experience wouldn't happen
again. Just remember, it's still in beta.


[h]: <https://gohugo.io> "Hugo"
[l]: <https://www.getlektor.com> "Lektor"
[j]: <https://jekyllrb.com> "Jekyll"
[ms]: <https://github.com/sunainapai/makesite> "makesite.py — GitHub"
[xkcd]: <https://xkcd.com/353/> "Python — xkcd"
[gs]: <https://git.oscarbenedito.com/oscarbenedito.com/file/gensite.py.html> "gensite.py — git.oscarbenedito.com"
