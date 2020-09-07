<!-- title: Deploying a website built with Hugo -->
<!-- slug: deploying-hugo-site -->
<!-- categories: Personal domain, Self-hosting -->
<!-- date: 2020-02-12T00:00:00Z -->

I have [previously talked][post] about creating a personal website, in this post
I will talk about hosting it. More specifically, I'm going to explain how to
host a website built with Hugo.

## Hosting without a server

If you don't have a server or don't want to be in charge of one, you can let
GitLab host your website. You can either do it with your own domain or use the
one GitLab will assign you based on your username. If you want to do it this
way, take a look at [their example][ex], you only need to add that
`.gitlab-ci.yml` file to your repository and GitLab will do the rest.

There are other services that will host a static site for free like Netlify
(which supports Hugo) or services that host a site given the HTML files such as
Neocities—in this case, you would need to run Hugo locally and upload the output
files.

## Hosting with a server

If you have a server or would like to run one, you can host your website there.
Let's see how to do it using Apache. First of all, we will install Apache and
Hugo on our server and clone our site's repository somewhere. In my case, my
Hugo directory is found in the `/srv` directory and the actual files that should
be served are in the `public` folder inside the directory[^var]. Therefore, the
directory I want to serve is `/srv/<hugo_directory>/public` (created by Hugo).

[^var]: It is also a common practice to put it under `/var/www`.

Before we begin, let's edit Apache's configuration to deny access to the default
folders. I am not sure if this is actually necessary as you will be setting up
site root directories, but I like to restrict any access and then grant it on a
per-site basis. Go to the Apache configuration file found at
`/etc/apache2/apache2.conf` and comment the lines with the following content
(put a `#` at the start of the line):

```apache
<Directory /var/www/>
  Options Indexes FollowSymLinks
  AllowOverride None
  Require all granted
</Directory>

<Directory /srv/>
  Options Indexes FollowSymLinks
  AllowOverride All
  Require all granted
</Directory>
```

That will restrict access to the specified directories (which will not be public
from now on). In order to grant access to the desired folder, we'll create a
file under `/etc/apache2/sites-available` with the site's configuration. I like
to name the files after the (sub)domain, so I would put my apache configuration
in the file `/etc/apache2/sites-available/<domain_name>.conf`, with the
following configuration:

```apache
<VirtualHost *:80>
    ServerName <domain_name>
    DocumentRoot /srv/<hugo_directory>/public
    ErrorLog ${APACHE_LOG_DIR}/error-<domain_name>.log
    CustomLog ${APACHE_LOG_DIR}/access-<domain_name>.log combined

    <Directory "/srv/<hugo_directory>/public">
        Options FollowSymLinks
        AllowOverride None
        Require all granted

        ErrorDocument 403 /404.html
        ErrorDocument 404 /404.html
    </Directory>
</VirtualHost>
```

What is happening here? We are creating a virtual host for incoming connections
on port 80 (default HTTP port) that will respond to requests to the
`<domain_name>` domain (specified on the `ServerName`). The root folder for the
domain will be `/srv/<hugo_directory>/public` (so if you access
`http://<domain_name>/blog/index.html`, it will serve with the file found at
`/srv/<hugo_directory>/public/blog/index.html`). After that, we set up the error
and access log files (the domain part of the name is not necessary, especially
if you are only hosting one service).

The second part of the file looks similar to the commented lines above, and they
actually do the same job, we just have them in this file which makes it easier
to keep track of which directories is each site depending on and their
permissions. In this case, we allow Apache to follow symbolic links and we give
access to our files to any user on the web (we won't ask for a password). On top
of that, I specified a custom 404 file (which will also be served when the
visitor is trying to access a restricted file or directory, which gives error
403).

Configuration ready! We'll need to activate it using the following command as
the root user:

```bash
a2ensite <domain_name>.conf
```

And just make sure your DNS is pointing to the server. Everything should work
now! However, we are serving our page through HTTP, we [definitely][dmsnh] want
HTTPS. It might sound unnecessary since we don't have any forms on our website
(no data to be encrypted), but HTTPS also guarantees site authenticity (protects
you against man-in-the-middle attacks) and normalizes the use of encryption on
the web.

In order to set up HTTPS, we need a certificate. I use one issued by [Let's
Encrypt][le], which are free and very easy to use (and they are renewed
automatically). To do so, I use [Certbot][cb], developed by the [EFF][eff]. To
use it, go to the Certbot's page, install it on your server and follow the
instructions on the website. Make sure you enable redirection to HTTPS!

It takes about 2 minutes to set up and now people will connect to your site
using HTTPS. You can see that a new file has been created at
`/etc/apache2/sites-available/<domain_name>-le-ssl.conf` by Certbot to configure
the HTTPS site, plus a couple of lines will be added to the configuration file
on port 80 to redirect to the encrypted site.

Your site is ready!


[post]: </blog/2019/12/your-corner-of-the-internet/> "Your corner of the Internet — Oscar Benedito"
[ex]: <https://gitlab.com/pages/hugo> "GitLab Pages Examples: Hugo — GitLab"
[dmsnh]: <https://doesmysiteneedhttps.com/> "Does my site need HTTPS?"
[le]: <https://letsencrypt.org> "Let's Encrypt"
[cb]: <https://certbot.eff.org/> "Certbot"
[eff]: <https://www.eff.org/> "Electronic Frontier Foundation"
