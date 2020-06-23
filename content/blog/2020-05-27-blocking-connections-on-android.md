---
title: "Blocking connections on Android"
slug: "blocking-connections-on-android"
categories: "Technology"
tags: ["Decentralization", "Personal website", "Privacy", "Website"]
date: 2020-05-27T19:01:00+00:00
---

I have been a user of [NetGuard][ng] for quite some time. It is a great Android
app that lets you control which apps get Internet access and which don't. The
paid version will allow you to block connection on a per-domain basis (for each
app), as well as let you see all the domains an app connects to (which are
normally a lot!). Furthermore, you will be able to block domains for the whole
phone. This is useful because it can act as an add blocker (by default it uses
the list of domains gathered in [this repository][repo]). The Google Play
version doesn't have this feature because Google doesn't allow add blocking on
the store, so make sure you get the app directly from GitHub!

A couple of months ago I decided to use a VPN, it felt like ISP's where very
public about everyone's data, and I decided to put my trust in a company whose
business is protecting their customers' privacy. The problem with VPNs is that
you have to trust them. There is no way for you to ensure they aren't selling
your browsing habits to the best bidder, but I did my research on the provider I
chose and I trust them a lot more than an ISP. Now you may ask, how is this
related to NetGuard? Well, NetGuard uses the VPN functionality on Android to be
able to block certain connections without root access, and Android only allows
one VPN at a time, so I had to choose one[^proxies].

[^proxies]: NetGuard offers a way to do what I wanted, through proxies, but I
  didn't like the workaround.

Finally, I decided to go with my VPN. However, I really liked the domain
blocking feature, so I decided to investigate a little further. It turns out you
can use the `/etc/hosts` files to block certain domains just like in a GNU/Linux
computer. It is an easy process and it really makes a difference in your mobile
browsing experience. I'll explain how I did it with my phone in case it helps
anyone else (although simply installing NetGuard is a simpler solution for sure,
and you get more features!).

First of all install Android Debug Bridge (ADB) on your computer. If you are
using GNU/Linux, you can use `pacman -S adb` on Arch based distributions or `apt
install adb` on Debian based distributions, look it up if you have other
distributions or operative systems. Now plug your phone into your computer and
on your phone enable developer settings (look it up if you don't know how to do
it) and do the following:

1. `Android debugging` > `on`
2. `Root access` > `ADB only`
3. Make sure your computer has access to your phone by enabling `PTP` on your
   phone (instead of `No data transfer`).
4. On the computer run `$ adb root` to get root access.
5. `$ adb remount`, which will allow you to modify the file on the phone.
6. `$ adb push /path/to/hosts/on/computer /etc/hosts`
7. Done! You can now unplug your phone (and disable the options you enabled
   previously if wanted).

If you want to edit the file manually, do the following after step 5:

1. `$ adb shell`, which will give you a terminal on the phone.
2. `# nano /etc/hosts` (`vim` also works on LineageOS).
3. Do your changes.
4. `# exit`

Easy! However, I am using LineageOS and I am unsure if you can do step 2 on a
stock ROM (if you can't, you might need a rooted device). If you try it—whether
on a stock ROM or another custom ROM—, let me know if it works! You still won't
be able to block certain apps' connections as with NetGuard, but you won't have
ads while keeping the VPN feature available for other uses.

[ng]: <https://www.netguard.me/> "NetGuard's website"
[repo]: <https://github.com/StevenBlack/hosts> "Unified hosts file repository"
