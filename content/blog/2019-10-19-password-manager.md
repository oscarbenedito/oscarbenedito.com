---
title: "Switching to a password manager"
categories: "Technology"
tags: ["Privacy", "Security"]
---
Before I learned about password managers, less than a year ago, having all my passwords on the same place sounded like a really bad idea—if someone managed to get access to "that place", they could log in to all my accounts, to my *online identity*.

As I learned about security (particularly when using the internet), it became a better idea, to the point that I now have used one for over half a year. I use [KeePassXC](https://keepassxc.org/), an offline password manager. I have also been recommended an online alternative ([Bitwarden](https://bitwarden.com/)), although I haven't used it because I would much rather not have my passwords online.

## Password requirements

Before considering whether having a password manager is worth it or not, it is necessary to expose what I require of my passwords.

 - **Unique passwords for each account**: if one of the sites I use was to be hacked and my password compromised, that should not be a problem for any of my other accounts. I think it is a pretty reasonable requirement if I want to lower the chances of my accounts being accessed by unauthorised parties, however, it makes remembering all my passwords a lot harder.
 - **Complex passwords**: my passwords should be hard to guess for a computer. You can imagine what type of password is easy to guess—or you can find examples on [Wikipedia](https://en.wikipedia.org/wiki/Password_strength#Examples_of_weak_passwords)—, however, even if we complicate passwords a little more they are still pretty easy to guess. In the end, what I mean by "complex" is that they should be long [pseudo]randomly-generated passwords that contain letters, numbers and special characters (long being about 16 characters, although normally I use more since adding characters is nearly free of cost when using a password manager).

## Dealing with complex passwords

Trying to remember passwords that fulfill my requirements gets incredibly hard very quickly (at least in my case). So I eventually realized I needed to rely on something different than my own memory if I wanted unique complex passwords. I had two options: have a physical notebook where I would write my passwords (avoiding the risk of my passwords gotten stolen if my computer was compromised) or use a password manager.

The notebook option was quickly discarded since typing the passwords in would take too much time (as well as writing them down when originally generated). In my case, someone accessing the passwords in my notebook—which is a lot of people's concern—wouldn't be an issue, since the notebook could be kept safe somewhere at home, but this solution just isn't efficient enough for me.

So using a password manager was a natural solution to manage my passwords. Although there are options to self-host an online password vault, I don't feel confident doing so, that's why I use an offline password manager. All my passwords are organized in folders on an encrypted database, but KeePassXC can do a lot more than that. It can create randomly generated passwords and has an auto-type feature that makes typing 30 character long passwords a breeze. It can also store extra information like [TOTP](https://en.wikipedia.org/wiki/Time-based_One-time_Password_algorithm) keys, but also miscellaneous information, both as an attribute-value pair or as plain-text notes. It has other features you might find useful, these are just the ones I use the most.

On top of that, having a password manager enables me to track all my online accounts, making it easier to spot and remove old unused accounts.

## Final comments

There is an option I haven't discussed yet: [Multi-Factor Authentification](https://en.wikipedia.org/wiki/Multi-factor_authentication) (or Two-Factor Authentification). Although it is very useful, a lot of online services still don't offer an option for it and it is easier for me to just use a password manager, however, 2FA might be better suited for you (because it allows you to be less strict on the password requirements while still keeping your accounts safe).

On a different note, some might say that it would be unusual for someone to try and hack my accounts by brute-forcing them (after all, they don't contain anything useful to a random stranger or entity), and it is probably true, but that isn't a good enough argument to give up on my security.

On the whole, I find that using a password manager grants me a lot of useful tools, while the drawbacks are nearly imperceptible.
