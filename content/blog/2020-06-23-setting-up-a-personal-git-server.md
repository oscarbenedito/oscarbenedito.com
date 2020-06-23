---
title: "Setting up a personal Git server"
slug: "setting-up-a-personal-git-server"
categories: technology
tags: [
    "Decentralization",
    "Git",
    "Personal domain",
    "Personal server",
    "Privacy",
    "Self-hosting",
    "Software",
    "Website",
]
date: 2020-06-23T16:10:00+00:00
---

Running a personal Git server is something that has been on my mind for quite a
long time. One of the most popular solutions I have seen around is
[Gitea][gitea]. A couple of months ago, when trying out different things, I
decided to run Gitea locally to see how easy it would be to implement on my
server. It turns out pretty easy, especially if you are using Docker. However,
my server doesn't run Docker as of now and it also felt like customizing it
would be hard (for example, getting rid of the username in the URLs). Gitea
looks like a very good solution for self-hosting Git (and the sites look very
nice!), but in my case, it felt like using a sledgehammer to crack a nut. I
figured most self-hosted Git solutions would turn out to be a bit too much for
my use case, so I decided to look into hosting Git without any other program.

I had experience setting up a bare-bones Git server only usable through SSH, so
I looked up how to create a website with the `bare` repositories. It turns out
there's even a built-in option[^giw]! Other programs have more or less similar
looks, but I decided to check if there was any way to have a static generator
for the webpage—the fewer things running on my server the better! And there is
one (that I found): [stagit][stagit]. It is very simple, and it does the job. On
top of that, the program is super small, which makes it very easy to modify it
if needed[^mods]. I gave it a try and it worked nicely. I decided that it was a
good solution for my use case, therefore having a vanilla Git server would work,
so I started building it[^already].

[^giw]: Run `git instaweb` from a Git repository to try it.

[^mods]: I haven't modified the source code much yet, but I have some ideas in
  mind.

[^already]: Funnily enough, I had already set up a Git server there for a couple
  of repositories containing a lot of personal information to avoid hosting them
  on GitLab or GitHub. I completely forgot about it. I deleted it and started
  from scratch, as I wanted to document the process on my personal wiki.

Let's see how to set it up!

## Setting up a Git server

What will happen is we'll have `bare` repositories on our server which we'll
then clone/fetch/push to using SSH[^bare]. We'll put these repositories on the
`/srv/git` directory—because I keep everything served from my server on
`/srv`—but any location will work. To keep Git separated from the root user,
we'll create a new `git` user, with `/srv/git` as its home folder, this way, the
remote address will be `git@domain:repo.git` (no need for an absolute address).
Let's do that:

[^bare]: Bare repositories are simply a folder with the files of the `.git`
  directory of a repository. Indeed, you can clone a repository from your
  computer running `git clone /path/to/repo/.git cloned-repo`. This directory
  contains all the information of the repository, that is why Git is
  distributed.

```sh
useradd -d /srv/git git
mkdir /srv/git
```

Now, let's create the folder for the SSH configuration where we'll add our
public key.

```sh
su git
cd
mkdir .ssh && chmod 700 .ssh
touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys
```

We could stop here, adding our key to the file (you can also use `ssh-copy-id`),
but we can take a couple more steps to isolate the user from the server, useful
especially if you want to share access to the git user with someone else.

To do that, we'll use the `git-shell` shell, which will only run scripts found
on `~/git-shell-commands`.[^issue]

[^issue]: If the `chsh` command doesn't work, make sure `git-shell` is in
  `/etc/shells`, if not, add it manually.

```sh
chsh git -s $(which git-shell)
```

Now if you add someone else's public SSH key to the server, they won't be able
to run any command. If you want to allow some commands, create scripts on
`~/git-shell-commands`. For example, I have scripts to initiate repositories,
add SSH keys and other useful commands, you can see them all [here][gsc].

## Making repositories public

Now we can pull and push to our repository, and we can share access to them by
adding SSH keys (or sharing the password if you use one). However, we might want
to have public repositories that people should be able to clone without the need
to have access to all of them. To do so, we'll use the Git Daemon (that uses the
Git Protocol). All we have to do is run the following command (and keep it
running, I recommend running a systemd service if you use systemd, there is an
example [here][prot-doc]).

```sh
git daemon --reuseaddr --base-path=/srv/git/ /srv/git/
```

This daemon will only serve repositories that have a file named
`git-daemon-export-ok` in them, so if you want to make a certain repository
public, all you have to do is run:

```sh
touch /srv/git/repo.git/git-daemon-export-ok
```

Remove that file to make it private again. The cloning address will be
`git://domain/repo.git` and you can't push to that address. You can also serve
repositories through HTTP which will allow you to have fine-grained control over
who can access which repositories, look it up if you are interested.

## Making a website

Now we can host private and public repositories, but we may want to share the
public ones easily. A website is a good way to allow people to quickly see your
repositories without the need to clone every single one of them. We'll use
stagit to create the HTML files which we'll host as a static site. First of all,
let's install stagit:

```sh
git clone git://git.codemadness.org/stagit
cd stagit
sudo make install
```

To create a website for a repository run

```sh
stagit /path/to/repo.git
```

from the directory where you want the site built. To create an index file with
all your repositories simply run

```sh
stagit-index /path/to/repo-1.git /path/to/repo-2.git > index.html
```

with the path to all your repositories. Make sure you have the correct
information on the `owner`, `description` and `url` files so that stagit uses
them when creating the HTML.

Having to do this is every time you update your repositories is not a reasonable
solution, but we can set up a `post-receive` hook to do it for us. There are
examples of scripts to use as an initial creation script for the whole site and
a post-receive hook on stagit's source code repository. I have changed those
scripts a bit to only process public repositories (the ones with the
`git-daemon-export-ok` file) as well a modified the source a bit. You can find
the changes on my [stagit fork][sg-fork].

## Pros of this setup

I have only been using this server for a couple of days, but I have also been
setting up a bunch of [suckless][sl] tools[^ff], so I have been using Git a lot.
One of the best things is that setting up repositories has never been easier. No
need to open a browser, log in to GitLab/GitHub and go through the process of
creating a new repository. I just run

[^ff]: Fun fact: after setting everything up I realized that suckless uses
  stagit to show their repositories, indeed the author of stagit is the current
  maintainer of some suckless projects like [st][st] and [dmenu][dmenu].

```sh
ssh git@oscarbenedito.com
init reponame
```

Done! I can also set it up as public by running a script I have on my
`git-shell` and change the description/owner/url just as easily.

Another thing I have noticed is that Git's clone/fetch/push commands are
significantly faster on this server than GitLab or GitHub. However, I don't know
compared to a self-hosted instance of Gitea or [Gogs][gogs].

## Cons of this setup

One thing that might be missed by this setup is the ability to download a
tarball with the code from a certain commit, browse the code as it was in a
given commit, see git blame, etc. This could be solved by using another tool for
the website part—such as [cgit][cgit]—so if I ever want to do that, it shouldn't
be hard.

Another thing is how the website looks. Other self-hosting solutions like Gogs,
Gitea, GitLab... look a lot nicer than stagit. However this isn't a priority
right now and I appreciate the ability to have full control over how the server
works—and it has been very interesting to learn about it all. Once again this is
something to do with the website, and not the repository hosting itself.

## Final comments

It has been fun to set everything up and realize how easy it is to self-host Git
without the need for other software. On top of that, I can now share my
repositories from my domain, which means it is easier to stop using other
hosting services if I stop wanting to accept their policies, similar to having
email on my domain.

For now, I will still have my public repositories hosted on GitLab and GitHub,
as I don't mind it and some people might be more used to those UIs. They also
act as a backup in case something happens to my server or if I want to edit my
repositories from a computer without SSH access to my server.

Finally, I have talked about some software that will allow you to self-host Git,
but I don't want to end this post without mentioning [sourcehut][sh]. I find it
a very good solution because everyone can contribute to your projects without
the need to create yet another account. Everything is done through email, which
is nicely supported by Git (learn more [here][g-email]).

I almost forgot! If you want to check out my Git website or clone some
repositories from my domain, you can find all of that here:
<https://git.oscarbenedito.com>.

[cgit]: <https://git.zx2c4.com/cgit/about/> "cgit's information"
[dmenu]: <https://tools.suckless.org/dmenu/> "dmenu's homepage"
[g-email]: <https://git-send-email.io/> "Learn to use email with Git!"
[gitea]: <https://gitea.io> "Gitea's home page"
[gogs]: <https://gogs.io> "Gogs' homepage"
[gsc]: <https://git.oscarbenedito.com/utilities/> "Personal git-shell commands"
[prot-doc]: <https://git-scm.com/book/en/v2/Git-on-the-Server-Git-Daemon> "Git daemon documentation"
[sg-fork]: <https://git.oscarbenedito.com/stagit/> "Personal stagit fork"
[sh]: <https://sourcehut.org/> "Sourcehut's homepage"
[sl]: <https://suckless.org> "Suckless' homepage"
[st]: <https://st.suckless.org/> "st's homepage"
[stagit]: <https://codemadness.org/stagit.html> "Stagit blog post"
