---
title: "Use web feeds!"
slug: "use-web-feeds"
categories: "Technology"
tags: ["Decentralization", "Personal website", "Privacy", "Website"]
date: 2020-04-18T14:59:00+00:00
---
Web feeds are data formats used to provide users with updates through web
syndication. Websites can use web feeds to post their content in a format that
allows users to easily check for updates regularly. Examples of web feeds are
[Atom][atom], [RSS][rss] or [JSON Feed][json-feed].

The most popular is RSS, you have probably heard of it. Until a year ago, RSS to
me was an old technology that some people used to get their news on an ugly feed
reader. I thought this technology was obsolete because of the couple
[silos][silo] that monopolize online social interactions. Well, this couldn't be
further from the truth. Web feeds are definitely not obsolete, and those "ugly
readers" I remembered were just particular examples, but there are a lot of
beautiful readers out there. There's also a lot of people that want to be able
to get updates on different sites without the need to have an account on a
centralized third-party service.

Let's see the benefits of using web feeds.

### Web decentralization

Web feeds allow for web syndication, which is key in order to decentralize the
web. When you follow a blog or a podcast through web feeds, neither you nor the
content creator rely on a third party to update you on the content. There's no
need to post a new update on a social platform. When new content is published,
the subscribers will see the updates coming directly from the original domain.

### Centralized updates

Wait, what?! Well, not as in "centralized service", but as in you get all the
updates from all these different websites in one app or program. Web feeds allow
the subscriber to see all the content updates in one place, so convenient!
Without it, we probably would have to check every single website regularly to
see if new content was published (or maybe design a bot that would do that for
us, but still, annoying).

### Control over content posting

By not relying on a third party for content updates, creators have full control
over their communication channel. It will never shut down—disappearing along
with the subscribers—, unless the creator decides to do so. There also won't be
any *magical* algorithms that decide which updates are worth showing to their
subscribers and which ones are not, or even which ones *magically* get deleted.
Subscribers get all of them.

### Control over the consumption of content

By using web feed readers, you can configure a dark theme, a bigger font, etc.
You can even have the content read to you. There are accessibility features for
webpages as well, but when using a web feed it is so much easier, since the
content is presented in a standardized format. It is also in the user's power to
filter the content any way they want. Do you want to block certain words? Done!

### Privacy for the subscriber

There's no need to insist on the fact that silos are a privacy nightmare. But
there's more. If you are reading a web feed, there are no advertisements
tracking you and there are no [tracking pixels][tracking-pixel]. You read the
content (or not) whenever you want, without anybody tracking you.

### The disadvantages

So, why doesn't everyone use it? First of all, most of the blogs I read have a
web feed, Mastodon does too, as well as Youtube[^other-platforms]. However, you
cannot comment through a feed reader and you normally don't see the "related
content" and all those extra features we can find on a website[^distractions].
There is also an entry barrier: it takes a couple fewer seconds to hit
subscribe/follow than to look for the web feed and open your web feed reader to
add it.

[^other-platforms]: If you want to follow people from other big social media
  sites, there are ways to do so! Use an instance of [Nitter][nitter] for
  Twitter or an instance of [Bibliogram][bibliogram] for Instagram. If you have
  other sites in mind, look around the Internet, someone probably implemented a
  web feed for it.

[^distractions]: This is actually seen as a good thing most of the time, as you
  get to consume the content without any distractions.

Web feeds also work best when you have a lot of sites that publish every once in
a while. If you subscribe to 500 sites that publish hourly, it can get
overwhelming with the common feed readers (although there are probably others
that are ready for this kind of usage and make it nice).

Finally, web feeds avoid tracking subscribers and the embedding of adds. That
can be an inconvenience to the content owner, who might want to do that.
Although I am not a fan of it, it is definitely something that happens. If that
is your case, there is an easy solution: don't post the content on the web feed.
Simply put your title and a two-line summary of the content. Subscribers can
then press on the link and open the content. This way you keep your subscribers
up to date, without losing the capacity to embed ads.

## Why e-mail newsletters are not a web feed substitute

E-mail newsletters have that decentralized component, you don't depend on a
centralized service (although most of them do, but that isn't necessary).
However they are definitely not private. First of all, you need to give out your
e-mail address, who knows if it will end up on a spam list? If you want to
unsubscribe you have to go to their website and hope for them to erase your data
and not only archive it somewhere. Finally, e-newsletters can—and most
do—contain tracking pixels, so they can know how many times a subscriber
accesses the content and when.

If you have an e-newsletter but don't have a website for it, then you have a
reasonable excuse not to have a feed (although you should definitely make a
website!). If you post your newsletter online, then add a web feed! It is very
easy!

## Fun fact!

As a matter of fact, I started writing a post on RSS feeds about three weeks
ago. When writing why you should add the whole content on your RSS feed and not
only a summary, I remembered that to do so, I did a little hack. I would put the
whole content in the `description` tag, which was designed for a brief summary.
That got me thinking, I wanted to follow the standards. After searching for a
while, I discovered you can use the `content:encoded` tag, which is exactly what
I needed, but there where other tags that also seemed to do the same. After some
more research, I discovered RSS has some standardization issues. So I looked at
the alternative I had heard about before: Atom. Apparently, Atom arose from the
need to standardize RSS, with a new design that wouldn't have backward
compatibility. Atom is very similar to RSS, but I like the fact that there is
one clear specification (apparently it has other cool features in case you are
interested, but I didn't look into them much).

After reading about this I learned how it worked and implemented for my blog's
feed (since Hugo's default is RSS). So if you use my web feed, you are now
retrieving an Atom feed!

As you probably figured my first draft had a different approach than the final
post. This was partially because shortly after I started writing,
[this][kevq-post] post came out so I changed my focus a bit. If you don't post
your full content on your web feed, read it!


[rss]: <https://en.wikipedia.org/wiki/RSS> "RSS — Wikipedia"
[atom]: <https://en.wikipedia.org/wiki/Atom_(Web_standard)> "Atom — Wikipedia"
[json-feed]: <https://en.wikipedia.org/wiki/JSON_Feed> "JSON Feed — Wikipedia"
[silo]: <https://indieweb.org/silo> "Silo — IndieWeb Wiki"
[tracking-pixel]: <https://en.wikipedia.org/wiki/Web_beacon> "Web beacon — Wikipedia"
[nitter]: <https://github.com/zedeus/nitter> "Nitter repository"
[bibliogram]: <https://github.com/cloudrac3r/bibliogram> "Bibliogram repository"
[kevq-post]: <https://kevq.uk/why-having-a-full-post-rss-feed-is-a-good-idea/> "Why Having A Full Post RSS Feed Is A Good Idea — Kev Quirk"
