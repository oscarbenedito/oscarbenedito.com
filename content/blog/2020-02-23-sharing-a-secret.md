<!-- title: Sharing a secret -->
<!-- slug: sharing-a-secret -->
<!-- categories: Cryptography -->
<!-- date: 2020-02-23T00:00:00Z -->
<!-- extrafooter: <a href="/jsweblabels/" rel="jslicense" style="display: none;"></a><script id="MathJax-script" async src="/js/mathjax-3.1.0/tex-chtml.js"></script> -->

Making a backup of a secret can be tricky. For instance: I have a lot of
passwords stored in an encrypted file, which I can edit through my password
manager. The data in that file is both very sensitive and crucial. I currently
have some offline backups (which are updated every once in a while) in different
locations and one online backup in case I lose access to my passwords and I am
not able to go to one of the locations where other backups are kept.

The problem with having an online backup is that such sensitive data must be
kept away from untrusted third parties and, so far, there's no third party I
would trust with all those passwords. My solution is to distribute the trust.
The encrypted file is encrypted again multiple times with very long random
passwords. Those passwords are distributed across different services, and the
file in another one, so no one service has access to the encrypted file.

This seems like a reasonably secure system (considering the diversity of parties
that should agree to attack me/get hacked). However, a couple of days ago, I was
introduced to a much simpler and convenient method to "distribute" a secret:
[Shamir's Secret Sharing][sss].

## Shamir's Secret Sharing

Shamir's Secret Sharing was created by [Adi Shamir][as], a cryptographer who is
also the co-inventor of the—probably more widely known—[RSA algorithm][rsa]
(yes, that S stands for Shamir!). Here, I'll try to briefly explain how it
works.

Given a secret \\(S\\) (coded as a number), we want to distribute it among
\\(n\\) parties (giving each party a "share" of the secret) in such a way that
only \\(k \\leq n\\) shares are needed to retrieve the secret, but that
\\(k-1\\) shares don't grant any kind of knowledge on \\(S\\).

Shamir's method is based on the fact that given \\(n + 1\\) pairs \\((x_i,
y_i)\\) such that \\(i \\neq j \\implies x_i \\neq x_j\\), then there exists a
unique polynomial \\(p\\) of degree \\(n\\) or less that satisfies that
\\(p(x_i) = y_i\\), \\(\\forall i \\in \\{1, \\dots, n\\}\\) (and we have an
efficient method to find \\(p\\) given \\(n\\) points).

Let's put it into practice. Given a secret \\(S\\), to be shared with \\(n\\)
parties in a way that any \\(k\\) parties can retrieve it, we'll build the
following polynomial:

\\[p(x) = S + a_1 x + a_2 x^2 + ... + a_{k-1} x^{k-1},\\]

where \\(a_i\\) are random numbers, \\(\\forall i \\in \\{1, \\dots, k-1\\}\\).
Now we'll evaluate our polynomial on \\(n\\) different points (and different
from 0) to obtain \\(n\\) pairs of the form \\((x_i, p(x_i))\\). This will be
the shares of the secret. Each party will get one share. We know that \\(k\\)
shares define a unique polynomial \\(p\\) of degree \\(k-1\\), (if we find it,
we'll find \\(S\\)). On the other hand, there are an infinite amount of
polynomials of degree \\(k-1\\) that interpolate \\(k-1\\) points, so the secret
cannot be easily obtained by gaining access to \\(k-1\\) shares[^integers].

[^integers]: This is not completely true when working with positive integers,
  but it can be solved by working with finite fields.

If we want to recover the secret from \\(k\\) shares, we can interpolate the
\\(k\\) points \\((x_i, p(x_i))\\) using [Lagrange's form for the interpolation
polynomial][int][^proof]:

[^proof]: Let's quickly prove that the \\(p\\) defined in Lagrange's form
  (\\(\\bar{p}\\) from now on) is the same as the previously defined \\(p\\).
  \\(\\bar{p}\\) is clearly a polynomial of degree (at most) \\(k-1\\), since it
  is the sum of polynomials of degree \\(k-1\\), so we only need to prove that
  it interpolates the points given (we'll asume that the fact that there is only
  one polynomial of degree at most \\(k-1\\) that interpolates \\(k\\) points is
  true). That is easy to prove since \\(i \\neq j \\implies l_i(x_j) = 0\\) and
  \\(l_i(x_i) = 1\\), therefore having \\(\\bar{p}(x_i) = p(x_i) l_i(x_i) =
  p(x_i)\\).

\\[p(x) = \\sum_{i=1}^{k} p(x_i) l_i(x),\\]

where

\\[l_i(x) = \\prod_{\\begin{smallmatrix}1\\leq m\\leq k\\ m\\neq
i\\end{smallmatrix}} \\frac{x-x_m}{x_i-x_m}.\\]

Now, evaluating on \\(x = 0\\) we'll find the secret (because \\(p(0) = S\\)).

## Final notes

Now we have a method to share our secret between multiple parties and being able
to retrieve it with only some of them. This method is not too hard to code
yourself, however, there are implementations online if you would rather not do
that (make sure you are running trusted code!).


[sss]: <https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing> "Shamir's Secret Sharing — Wikipedia"
[as]: <https://en.wikipedia.org/wiki/Adi_Shamir> "Adi Shamir — Wikipedia"
[rsa]: <https://en.wikipedia.org/wiki/RSA_(cryptosystem)> "RSA — Wikipedia"
[int]: <https://en.wikipedia.org/wiki/Lagrange_polynomial> "Lagrange polynomial — Wikipedia"
