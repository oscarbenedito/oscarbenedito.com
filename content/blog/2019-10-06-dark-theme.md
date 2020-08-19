---
title: "Creating a dark theme"
slug: "dark-theme"
categories: "Technology"
tags: [
  "CSS",
  "Website"
]
date: 2019-10-06
---

The first contact I had with HTML and CSS was about two years ago, when I
created my first website along with a friend who already had some experience
with them, as well as with JavaScript. We used a premade theme (based on
[Bootstrap][bs]), so I didn't really learn much CSS, but I started understanding
what was HTML and how it worked. One year later, I wanted to design my own
website and I decided to build my own theme. I looked up many CSS frameworks and
ended up using [Bulma][b] because of how simple it is (I didn't need many
features for a personal website). It worked pretty well and I had a first
contact with CSS and SASS, but when I finally finished my page and released it
under my domain, I soon wanted another feature: the possibility to change to a
dark theme.

I started looking for dark colors that I liked and I came up with a nice design,
now I needed to combine the two designs with a simple toggle JavaScript
function. The way I implemented it, the function switched the default CSS file
for the one defining the dark theme. However, if you try to change your theme by
changing the stylesheet, you will realize that it takes a split of a second for
the page to re-render, especially the first time you toggle the theme since it
has to download the whole file before rendering the page. It can sound like a
minor problem, but it was notable, so I tried to shorten the time needed to
toggle the theme. I used a tool (unCSS) that removes unused CSS from a
stylesheet, which made the file so much smaller but, although the download time
was reduced, the page still took too long to re-render. Looking around online I
concluded that my best option was to make only one file using CSS variables, and
just change the value by changing HTML elements' classes with the JavaScript
function.

The problem with using variables with Bulma is that it uses SASS functions that
given a color, output a different one (and it can't do that if the input color
is a variable) so it doesn't *compile*. I tried to change the affected functions
with similar ones supported in CSS, but the result wasn't what I wanted, and it
changed a lot of things related to Bulma. After some thought, I decided to
refrain from using a framework and just create a tailored stylesheet for my
website. That would allow me to abandon the unCSS tool—which was pretty
inconvenient to use—as well as having a better understanding of my CSS file.

Looking around for simple themes to base my new stylesheet in, I found a couple
that, combined, could result in a similar website than the one I had. I based my
theme on the [Hugo Paper][hp] theme (you can see that the cards look very
similar) and I added a header (inspired by the [Hugo Grapes][hg] theme) and a
footer. I changed how some elements appeared (such as the tables), I added some
more features that I found interesting and I themed it with the colors I wanted.
I also used my old site to inspire the new features (especially the header and
footer), so it might resemble a site using Bulma, although it is not.

The process took a lot of time, since learning how everything worked and
completely redoing the stylesheet was very time-consuming, however, the result
was worth the time. Finally, you can enjoy a dark theme that toggles instantly,
and it is now so much easier for me to redesign certain parts of the website, as
I know more CSS and have a better understanding of my stylesheet.


[bs]: <https://getbootstrap.com/> "Bootstrap"
[b]: <https://bulma.io/> "Bulma"
[hp]: <https://github.com/nanxiaobei/hugo-paper/> "Hugo Paper — GitHub"
[hg]: <https://github.com/shankar/hugo-grapes/> "Hugo Grapes — GitHub"
