---
title: "Deploying a website using the WebDAV protocol"
categories: "Technology"
tags: ["WebDAV", "Scripts", "rsync", "File synchronization", "davfs2", "Autistici/Inventati"]
---
Now that my website is [hosted by Autistici/Inventati]({{< ref "/blog/2019-11-04-new-host.md" >}}), I can no longer deploy it by just pushing my git repository's changes to GitLab, as I used to. In order to deploy my website, I need to access the server using the WebDAV protocol. To do so, I use [davfs2](https://savannah.nongnu.org/projects/davfs2)—which mounts the WebDAV resource—so I can access it like any other folder in the filesystem.

I had never used the WebDAV protocol before, so I used A/I's tutorial. It was was a very simple tutorial, but it goes straight to the point, without giving unneeded explanations. I set it all up and edited the `~/.davfs2/secrets` file to make the mounting process smother. I know that having a password in plain text is a potential security risk, but the password only gives access to the WebDAV service (not my whole A/I account) and is easily resettable. If someone got hold of the password, all they could do is change my website, until I realized it and change it.

Deploying the website would mean copying all the output files from [Hugo](https://gohugo.io/)—the static site generator used to build my site—to the specified folder on the mounted filesystem. The problem was that copying files (as well as removing them) takes a long time, I am guessing due to A/I's resources' configuration. To give some context, it took around 1 minute to copy 1MiB worth of files, plus 10 seconds to delete them. So deleting and copying the whole folder again every time I changed something wasn't a good deploying method (besides, it wastes resources server-side).

The solution I chose was [rsync](https://rsync.samba.org/). It is a great piece of software that efficiently transfers files from one folder to another. It checks the last modification time and the file size to avoid transferring files that are up to date. I already knew this program as I use it to back up my computers to hard drives (it reduces the backup time considerably after the first time), so implementing it should have been a breeze. I encountered two problems:

1. By default, `rsync` makes use of modification times to check whether a file should be transferred, but every time I build my site, all files are created again, so the modification times are always newer than the ones in the server.\
  There is a quick fix for this: the program has an option (`-c` or `--checksum`) that makes the program use the checksum of a file (instead of the modification time) along with the file size to determine whether it has changed.

2. `rsync` makes use of auxiliary files while synchronizing them. For some reason (that I still don't know, my guess is something to do with permissions), when those auxiliary files are finally renamed to the definitive filename, it fails, giving out an error and exiting without any file transferred.\
  To fix this issue, I used the `--temp-dir` option to specify a local directory as the one that should be used for the temporary files. With that set up, it doesn't give any more errors.

So finally the `rsync` command worked, and the time used to update the website is now around 10 seconds, which is a lot better than a minute (considering my website might get larger, the impact can be even bigger). To automate the process I build a little script that will mount the filesystem, build the site, synchronize it with the server and unmount it again:

{{< highlight bash >}}
#!/bin/bash

HUGO_PATH="{path_to_hugo_directory}"
TEMP_DIR="{path_to_temp_directory_to_use_with_rsync}"
MOUNT_PATH="{path_to_the_mounted_directory}"
WEBDAV_FOLDER="{website_directory_in_webdav_filesystem}"

rm -rf $HUGO_PATH/public
hugo -s $HUGO_PATH --minify
mount $MOUNT_PATH
mkdir $TEMP_DIR
rsync -ruvc --progress --delete --temp-dir=$TEMP_DIR $HUGO_PATH/public/ $MOUNT_PATH/$WEBDAV_FOLDER
rmdir $TEMP_DIR
umount $MOUNT_PATH
{{< /highlight >}}

As you can see, it is a very simple script. It removes the last built of the site from the local filesystem and builds it again (using the `--minify` option to reduce file sizes), it mounts the WebDAV resource, transfers the files and then unmounts the resource again.
