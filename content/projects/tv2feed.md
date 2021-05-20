<!-- title: TV2Feed -->
<!-- description: TV2Feed: Follow TV shows using Atom feeds! -->

Follow TV shows using Atom feeds!

TV2Feed is a Python script that creates Atom feeds for TV shows, creating one
entry per episode. The script can be found [here][script] ([raw file][raw]). For
examples of outputs (which are not updated periodically), see [feed][] (combined
feed) or [show/210][showfeed] (single show).

## How to use

Download the script and edit the global variables to your liking. Go to
<https://www.tvmaze.com> and search the TV shows you want to follow. Write down
their IDs (the number in the URL) and then run the following:

```
tv2feed id1 id2 ...
```

Or run it multiple times to get one feed per TV show. The feeds are expected to
go under:

- `https://<domain>/<path>/feed`: if multiple shows specified
- `https://<domain>/<path>/show/<show_id>`: if only one show specified

That is because the feed URIs will point there. Note that if only one show is
specified, TV2Feed will generate it assuming there is one feed per show (which
will make the feed title the same as the show's).

The API where the data is gathered from caches results for one hour, so you
can add cron jobs to run every hour:

```
0 * * * * /usr/local/bin/tv2feed 210 431 > /srv/www/tv2feed/feed
```

or, alternatively (could also be scripted with just one cronjob):

```
0 * * * * /usr/local/bin/tv2feed 210 > /srv/www/tv2feed/show/210
0 * * * * /usr/local/bin/tv2feed 431 > /srv/www/tv2feed/show/431
```

## Other notes

Each show will make two API requests, and there is a limit of 20 requests every
10 seconds (for contents that are not cached). If you are following many shows,
this script will sleep for 10 seconds and try again if an API call returns a 429
error code, if it fails again (or the error code is not 429), it will raise an
error and exit.

TV2Feed is licensed under the GNU Affero General Public License version 3 or
later (available [here][agpl]).

All data generated is gathered from [TVmaze][]'s API.


[script]: <https://git.oscarbenedito.com/osf/file/tv2feed.py.html>
[raw]: <https://git.oscarbenedito.com/osf/raw/tv2feed.py>
[feed]: </projects/tv2feed/feed>
[showfeed]: </projects/tv2feed/show/210>
[agpl]: <https://www.gnu.org/licenses/agpl-3.0.html> "GNU Affero General Public License - GNU Project"
[TVmaze]: <https://www.tvmaze.com>
