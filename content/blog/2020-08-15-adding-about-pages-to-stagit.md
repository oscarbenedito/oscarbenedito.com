---
title: "Adding about pages to stagit"
slug: "adding-about-pages-to-stagit"
categories: [
  "FOSS",
  "projects"
]
date: 2020-08-15T19:59:00+00:00
---

I use [stagit][sg] to show the public repositories of my Git server on the web.
I chose stagit because it is a very simple and lightweight tool, which makes
tinkering with the source code very straightforward (which I have been doing a
bit lately) and because the resulting website is static: easy to set up, faster,
and there aren't any application-specific issues (there is no application).
Static sites are also nice because you know exactly what is going on when a page
is requested—the file is served—, whereas if it is a dynamic site, you might or
might not know what operations the server is doing to answer the request.

Stagit doesn't have many features. This isn't necessarily bad, as it keeps the
source small and readable and it still does everything I consider necessary, it
even has an Atom feed for commits! The one feature I really missed was being
able to show an about page with the repository's readme file when it is
opened[^nt]. For me, it is a basic feature, especially with repositories for
projects without a website/wiki. When I hear about a piece of software, the
first I do is go check out the repository and read a bit about it, and readme
files make that easier. Since most of my repositories have readmes written in
Markdown, I wanted stagit to convert them to HTML, so they could be shown nicely
on the repositories' website.

[^nt]: Stagit has a link on the navigation bar to the readme file, and you could
  easily make that the default `index.html` file, but it is just the page with
  the raw file (as any other file is shown), it isn't presented like an about
  page.

If you want to try it out yourself, the change on stagit is very simple, just a
couple of lines, but it will add a dependency to the program[^dep]. I use
[md4c][md4c] to parse the files, and it is ridiculously fast. I haven't noticed
any changes in the time it takes for stagit to run. Check out [this commit][cm]
if you want to know how I did it, and feel free to suggest other approaches if
you think they are better.

[^dep]: The dependency is only for parsing Markdown, if you don't need that, you
  can just show the raw file without the line numbers and metadata, this is what
  [I do][nm] when the readme file isn't a Markdown file.


[sg]: <https://codemadness.org/stagit.html> "Stagit blog post — codemadness.org"
[md4c]: <https://github.com/mity/md4c> "md4c — GitHub"
[cm]: <https://git.oscarbenedito.com/stagit/commit/1fdbc7e8ef4025e50678261ca670daca85ac298c.html> "Add about page for repos with REAMDE — git.oscarbenedito.com"
[nm]: <https://git.oscarbenedito.com/stagit/commit/1fdbc7e8ef4025e50678261ca670daca85ac298c.html#h5-5-16>
