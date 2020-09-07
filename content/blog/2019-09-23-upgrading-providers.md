<!-- title: Upgrading to privacy-conscious providers -->
<!-- slug: upgrading-providers -->
<!-- categories: Cryptography, Decentralization, Privacy -->
<!-- date: 2019-09-23T00:00:00Z -->
<!-- lastmod: 2019-09-24T00:00:00Z -->

I have been reading a lot about decentralization and not depending too much in
one company in the past six months and I realized how much I relied on Google:
my email, all my files, contacts, calendars, pictures... Most of my data was
stored on their servers. This was inconvenient for three reasons: (1) if
something was to happen to Google or my account, I would lose a lot of data, (2)
Google doesn't use end-to-end encryption, which means that they (and anyone with
access to their servers) can see all my files, emails, etc. and (3) Google
already uses all this data (and other it collects) to better know my
personality.

Some people might think that the main three problems I have with Google aren't
that important. In fact, I have used Google for many years because that was my
opinion for a long time. However, the more I read about the issue, the more I
realize they aren't minor problems. I realized that for me it is worth it to pay
$12 or $24 a year in exchange for privacy. If you are still doubting, [this
post][mw] might change your mind.

***

Let's see what I needed out of my new providers/configuration:

1. Control over my data: if something were to happen to my account, it shouldn't
  affect me too much.
2. Encrypting my data: end-to-end encryption for my services, so there wasn't a
  need to "trust" the provider, as well as to avoid any problems in case the
  servers were compromised—which is not that uncommon.
3. Privacy: the provider shouldn't be using my data in any way (which is mostly
  solved with end-to-end encryption).

### 1. Control over my data

My first problem was easily solvable, I simply needed to back up everything that
was on the cloud. That process was pretty easy using [Google's export tool][to].
With a few clicks, everything was ready, and I only had to wait for Google to
collect all the data and create the file. I'm not sure how much that took, I
would say less than an hour, but definitely less than a day (it was a long ago,
so I don't remember).

Selecting all the different services I wanted to export from one page instead of
having to go to each service's URL and then select export made the process so
much smoother. I was surprised by how easy the export was, and all the data was
in convenient files to import to other services: contacts in a VCF file,
calendar in an iCal file... which makes a lot of sense, but not all services
allow such an easy process to export everything and ready to use in a different
service. Fortunately, that was the case, so my next problem was a lot easier to
solve.

### 2. Encrypting my data

In order to encrypt my content, I needed to find an alternative to a lot of
services that Google was offering me (or use tools such as [Cryptomator][c],
which was discarded because of problem number 3). And so the search
began.

#### Email

There are a lot of encrypted mailboxes and there is also the option of
self-hosting email. I wasn't interested in managing my own server just for my
email, so I had to choose a provider. Many of the sources I checked recommended
[Protonmail][pm] and [Tutanota][tn], among others. They both looked nice and
offered a free tier, so I tried them. After some time, I finally decided to go
with Tutanota because of how they approached their user community as well as
other details (for instance, their app not using any of the Google Play
Services), although it was a hard choice.

#### File storage

Most of my files in the cloud were old and not usually needed, they were just
online because I used Google Drive as my home folder. The solution was easy: I
backed them up on an offline external storage as well as on my computer and
deleted them from the cloud.

As for the few files I actually needed online (the ones I use both at home and
at college), I now use a USB stick to have them wherever I go, as well as
backing them up every once in a while. No need to have them online, and it is
faster to plug in a USB stick than log in to Google Drive and download the files
(which was what I was doing on all computers running GNU/Linux).

There is one type of file I haven't replaced yet: anything that was shared is
still on my Drive (even if other services offer it, for now, I am fine with
using Google).

#### Calendar and contacts

I created an account in a Nextcloud instance for my calendar and contacts.
Nextcloud is very intuitive and I like the user interface. There's the
[DAVx⁵][dx] app that synchronizes them to my phone, so that was an easy choice.
Having an account at a Nextcloud instance is also useful in case I want to
upload files and it also allows me to sync my [Joplin][j] notes.

#### Search

I thought the search engine would be the hardest service to substitute, however,
there are a lot of good alternatives. The one I went for is [DuckDuckGo][ddg]
which works pretty well and also works if you are connected to the internet
through the [Tor network][tor].

#### Others

I never had to substitute the web browser since I already used [Firefox][ff],
and as for the photo hosting service, I just don't upload them online anymore
and I use the [Simple Gallery][sg] app (you can install it for free from
[F-Droid][fd]). I also substituted Android's custom ROM, but I will talk about
that some other time.

#### Temporarily not replaced

I temporarily haven't replaced one service: Google Maps. Its accuracy is so good
that it is hard to match. I have downloaded [OsmAnd][oa], but when searching for
public transport routes, I still check Google Maps.

### 3. Privacy

When looking for all the new services in order to get end-to-end encryption, I
already looked at their policies in relation to privacy, so this problem was
solved as well.

## Conclusion

It took me some time to make all these changes, especially my phone's operative
system and my email address—I still use the old one with a lot of people, I am
progressively updating it. Some of the services are hard to replace and it takes
time to get used to the new providers. However, if you are interested in getting
privacy when sending personal emails or saving files online, it is worth the
change.


[mw]: <https://www.gnu.org/proprietary/malware-google.html> "Google's Software is Malware — GNU Project"
[to]: <https://takeout.google.com/> "Takeout — Google"
[c]: <https://cryptomator.org> "Cryptomator"
[pm]: <https://protonmail.com> "Protonmail"
[tn]: <https://tutanota.com> "Tutanota"
[dx]: <https://www.davx5.com> "DAVx5"
[j]: <https://joplinapp.org> "Joplin"
[ddg]: <https://duckduckgo.com> "DuckDuckGo"
[tor]: <https://www.torproject.org> "Tor project"
[ff]: <https://www.mozilla.org/firefox/> "Firefox"
[sg]: <https://www.simplemobiletools.com/gallery/> "Simple Gallery"
[fd]: <https://f-droid.org/en/packages/com.simplemobiletools.gallery.pro/> "Simple Gallery — F-Droid"
[oa]: <https://osmand.net/> "OsmAnd"
