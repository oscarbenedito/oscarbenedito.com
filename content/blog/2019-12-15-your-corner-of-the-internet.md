<!-- title: Your corner of the Internet -->
<!-- slug: your-corner-of-the-internet -->
<!-- categories: Decentralization, Personal domain -->
<!-- lastmod: 2019-12-06T00:00:00Z -->
<!-- date: 2019-12-15T00:00:00Z -->

We tend to have online accounts across different social networks and services.
We upload our projects in some sites, we post on different ones and we follow
different people on all of them. Our online identities—along with everything we
share—are all over the place, but there is a way to solve this (and many other
problems): personal websites.

Creating a personal website is a great way to share our projects, experiences,
thoughts, etc. under our own terms, without being limited to a given theme or a
couple of available options in a certain service. A personal website allows you
to customize it as you want, whether that is quickly setting up a simple website
with a portfolio, spending time creating the perfect CSS file or even setting up
a service to share files with your friends using a password.

You can buy a personal domain at a considerably cheap price (less than $12 a
year for a `.me`, `.org` or `.com` domain), but it will provide you with
something much more valuable: your corner of the Internet. Nobody can shut down
your domain because it is no longer profitable and if your host can't continue
to provide you with what you need, or they change their terms, you can simply
switch companies, and still show your website under the same URL. You can change
anything on the "backstage", and others will always find you at the same place.

## Building the website

If you don't have any experience with programming or using plain text and you
don't want to spend time getting familiar with it, you can use WordPress[^wp] to
create your site. It is a free (as in freedom) [content management system][cms]
that will allow you to build a site without much HTML/CSS knowledge. If you are
more comfortable with plain text and the terminal or want to get in touch with
them, building a static site that supports Markdown will probably be a much
better option.

[^wp]: I use WordPress as the dynamic alternative because it has a free license,
  it is beginner-friendly, it can easily be configured to run a personal website
  with a blog and a portfolio and because it is very popular. However, if you
  are thinking about creating a dynamic personal site, you should consider other
  options that are also interesting.

### What is a static site?

Most of the websites we visit are dynamic. That means that the server we are
retrieving the pages from is executing a program, and the pages we see are the
results of that web application. Dynamic sites can be useful when we want users
to be able to edit data. For instance, if users can log in and publish posts,
that would require a dynamic site.

On the other hand, there are static websites. In this case, the server simply
serves files that are already stored on the server. So, for a given URL,
everybody sees the same HTML (and JavaScript and CSS). You probably won't
require a dynamic personal website, since you'll probably be publishing
information about you, your projects, etc., without the need of a server that
does real-time calculations to serve a page[^static].

[^static]: You can still change the contents in a static site, however, you will
  have to edit the text files manually and then upload them to the server (this
  can be automated). It is less complicated than it sounds once you learn
  Markdown (which is very simple).

Why am I talking about static sites? Well, they offer some advantages over
dynamic ones.

- **More efficient**: since serving a page doesn't need any extra server-side
  operation, static sites use way fewer resources, which can benefit you when
  considering self-hosting the site. It will also make your site more
  environmentally friendly.
- **More secure**: since there isn't an app server, potential vulnerabilities
  are reduced drastically.
- **Faster**: because the server doesn't need to do operations, it can respond
  to requests faster, hence accelerating the loading time.<br/>
  *That is a general claim, by using proper caching and using content delivery
  networks, speeds can change considerably. It also depends on the number of
  plugins installed (or other operations made by the server).*

Because of these advantages, you can find free hosting for static sites and
lower prices when self-hosting or using shared-hosting because of the lower
amount of resources needed. Furthermore, since everything is stored in plain
text and not in a database, you can easily use a version control system (such as
Git) to keep a history of all your changes and easily share the source code of
your site.

## Generating a multi-page site

To create a static website with multiple pages, you can use a static site
generator. There are a lot of static site generators, and I use Hugo (for a
couple of reasons that I might write about some other time). With the use of
Hugo—most other generators also offer this functionality—, you can code your
navigation bar in a file, your footer in a different one and include both of
them in multiple templates. These templates will then gather the content from
your Markdown (or HTML) files, put it all together and output all the HTML files
of your site. Now that I have an operative site, when I want to publish a new
post, I create a file with some metadata and the post content, and Hugo does the
rest. Post files look like the following:

```markdown
---
title: "Post title"
categories: category
tags: [ "tag1", "tag2" ]
---

Post content.
```

Thanks to Hugo, it is very easy to add content to a website, and the source code
is neatly organized. Hugo also lets you minify the content to reduce file
sizes—although some people might argue against it, I find it useful and some
files get reduced by up to 30% (CSS files)[^minify].

[^minify]: On top of that, you can always find the source code well indented in
  the repository, by clicking on *Inspect element* or by using a prettifier.

## Conclusion

Since my recent exit from multiple services because of privacy terms concerns, I
realized having a personal website can substitute social networks. I get to
share anything I want on my own terms (and with my own theme!), ensuring privacy
to anybody who wants to read, and I get to keep the copyright over my content. I
now have my corner of the Internet, where everyone can find me, contact me and
read what I have to share.


[cms]: <https://en.wikipedia.org/wiki/Content_management_system> "Content management system — Wikipedia"
