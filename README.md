# Personal website

This repository is the source code for my [personal website][pw]. The site is
generated by `gensite.py`, a program based on [makesite.py][ms] (which is a very
bare-bones static site generator).

## Dependencies

To generate the site all you need is Python 3 and the markdown library (install
with `pip3 install markdown`).

## Other notes

The font used for the logo is "Libre Baskerville" in bold. The `woff2` file used
for the font only includes the needed letters for the logo ("BOacdeinorst") to
keep the file size small (2.5 KiB). To create such file, you can use the
following command:

```sh
pyftsubset LibreBaskerville-Bold.ttf \
  --unicodes=U+004F,U+0073,U+0063,U+0061,U+0072,U+0042,U+0065,U+006E,U+0064,U+0069,U+0074,U+006F \
  --output-file=<output-font-file>.woff2 --flavor=woff2
```

You might need to run `pip3 install fonttools brotli` to install the
dependencies.

## License

The contents of this repositories are licensed under the [GNU Affero General
Public License version 3][agpl] or (at your option) any later version.

More specifically, the contents of my pages (in the contents folder) are
licensed under the [Creative Commons Attribution 4.0 International
License][cc-by].

[pw]: <https://oscarbenedito.com> "Oscar Benedito's personal website"
[ms]: <https://github.com/sunainapai/makesite> "makesite by Sunaina Pai — GitHub"
[agpl]: <https://www.gnu.org/licenses/agpl-3.0.html> "GNU Affero General Public License version 3"
[cc-by]: <https://creativecommons.org/licenses/by/4.0/> "Creative Commons Attribution 4.0 International License"
