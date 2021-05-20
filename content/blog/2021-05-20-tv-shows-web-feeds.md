<!-- title: Follow TV shows with web feeds -->
<!-- slug: tv-shows-web-feeds -->
<!-- categories: FOSS, Projects -->
<!-- date: 2021-05-20T19:19:00Z -->

I am quite strict about which messages make it to a push notification on my
phone. I don't like to receive notifications unless they are important or
urgent. The same thing happens with emails—indeed, it's one of the few
applications which have notifications enabled. However, I also don't want to
regularly check different places for updates. Because of this, most of the
updates I receive are through another channel: web feeds.

[I have written before][feeds] about using web feeds (Atom, RSS, JSON feed...)
to keep track of updates to sites. I use my feed reader to get updates about
some of the software I use, YouTube videos, newsletters, and, of course, blogs.
They are all things I don't want to miss out on, but I don't want to be notified
about. Instead, Miniflux (my feed reader) stores them until I decide to log in
and read them. This allows me to disable any notifications but have them all
centralized in one place.

Lately, many TV shows are starting to air again, meaning that there are new
episodes weekly of some series that I am watching, and soon more will follow.
Because of this, I want to keep up to date with which TV series are coming up,
but I don't want push notifications or emails (or checking their websites). I
just want a way to know that there are new episodes for me to watch, but without
the hassle of looking it up... Ring a bell? Web feeds!

Yesterday I quickly looked around to see if there was any service offering that
for free or cheaply, and there was none. The ones I saw were about 5€/month,
which is more than any other service I use (a small VPS, email provider or
Miniflux). I was not willing to pay that much, and I was motivated enough to do
such a service myself, it sounded like a fun and easy project to take on for a
day or two, so I did.

Luckily, [TVmaze][] offers a free API with all the information I needed, and
there I went with a Python script. After some time, I had it running, and today
I polished it a bit. I can say it is fully working now!

The script takes TV series IDs (as many as you want) and creates an Atom feed
with an entry for each episode there is. Just run it as a cron job every hour
and put the output on a static site, you're done! Alternatively, you can make
one feed per show, so multiple people can subscribe to their desired shows.

If you are interested, there is a bit more information about how it works
[here][tv2feed] and the code is [here][code].


[feeds]: </blog/2020/04/use-web-feeds/> "Use web feeds! - oscarbenedito.com"
[TVmaze]: <https://www.tvmaze.com>
[tv2feed]: </projects/tv2feed/>
[code]: <https://git.oscarbenedito.com/osf/file/tv2feed.py.html>
